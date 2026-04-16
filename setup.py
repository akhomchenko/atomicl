import os
from distutils.command.build_ext import build_ext
from distutils.errors import CCompilerError, DistutilsExecError, DistutilsPlatformError

from setuptools import Extension, setup

try:
    from Cython.Build import cythonize

    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False


ext = ".pyx" if USE_CYTHON else ".c"
extensions = [
    Extension(
        "atomicl._cy",
        sources=["src/atomicl/_cy" + ext, "src/atomicl/_atomic.c"],
        include_dirs=["src/atomicl/"],
    )
]


class BuildFailed(BaseException):
    pass


class ve_build_ext(build_ext):
    def run(self):
        try:
            build_ext.run(self)
        except (DistutilsPlatformError, FileNotFoundError):
            raise BuildFailed()

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except (CCompilerError, DistutilsExecError, DistutilsPlatformError, ValueError):
            raise BuildFailed()


NO_EXTENSIONS = bool(os.environ.get("ATOMICL_NO_EXTENSIONS"))

if USE_CYTHON:
    extensions = cythonize(
        extensions,
        annotate=True,
        compiler_directives={"language_level": "3"},
    )

if not NO_EXTENSIONS:
    print("*********************")
    print("* Accelerated build *")
    print("*********************")
    try:
        setup(ext_modules=extensions, cmdclass=dict(build_ext=ve_build_ext))
    except BuildFailed:
        print("*********************")
        print("* Pure Python build *")
        print("*********************")
        setup()
else:
    print("*********************")
    print("* Pure Python build *")
    print("*********************")
    setup()
