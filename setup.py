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


BUILD_FAILURE_HINT = (
    "Failed to build the optional native extension. "
    "Set ATOMICL_NO_EXTENSIONS=1 to force a pure-Python install."
)

C11_UNIX_FLAGS = ["-std=c11"]
C11_MSVC_FLAGS = ["/std:c11", "/experimental:c11atomics"]


class BuildFailed(Exception):
    pass


class ve_build_ext(build_ext):
    def build_extensions(self):
        if self.compiler.compiler_type == "msvc":
            cflags = C11_MSVC_FLAGS
        else:
            cflags = C11_UNIX_FLAGS

        for ext in self.extensions:
            ext.extra_compile_args = list(cflags)

        build_ext.build_extensions(self)

    def run(self):
        try:
            build_ext.run(self)
        except (DistutilsPlatformError, FileNotFoundError) as exc:
            raise BuildFailed(BUILD_FAILURE_HINT) from exc

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except (
            CCompilerError,
            DistutilsExecError,
            DistutilsPlatformError,
            ValueError,
        ) as exc:
            raise BuildFailed(BUILD_FAILURE_HINT) from exc


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
    setup(ext_modules=extensions, cmdclass=dict(build_ext=ve_build_ext))
else:
    print("*********************")
    print("* Pure Python build *")
    print("*********************")
    setup()
