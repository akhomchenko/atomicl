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

if USE_CYTHON:
    extensions = cythonize(
        extensions,
        annotate=True,
        compiler_directives={"language_level": "3"},
    )


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


args = dict(
    zip_safe=False,
    ext_modules=extensions,
    cmdclass=dict(build_ext=ve_build_ext),
)


try:
    setup(**args)
except BuildFailed:
    print("************************************************************")
    print("Cannot compile C accelerator module, use pure python version")
    print("************************************************************")
    del args["ext_modules"]
    del args["cmdclass"]
    setup(**args)
