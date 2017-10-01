from setuptools import setup
from setuptools import Extension
from distutils.command.build_ext import build_ext
from distutils.errors import CCompilerError
from distutils.errors import DistutilsExecError
from distutils.errors import DistutilsPlatformError

try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False


ext = '.pyx' if USE_CYTHON else '.c'


extensions = [
    Extension('atomicl._cy', sources=[
        'src/atomicl/_cy' + ext,
        'src/atomicl/_atomic.c'
    ], include_dirs=['src/atomicl/'])
]


if USE_CYTHON:
    extensions = cythonize(extensions, annotate=True)


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
        except (CCompilerError, DistutilsExecError,
                DistutilsPlatformError, ValueError):
            raise BuildFailed()


args = dict(
    name='atomicl',
    version='0.1.1.dev',
    keywords='atomiclong',
    description='Yet another implementation of AtomicLong',
    long_description=open('README.rst').read(),
    author='Alex Khomchenko',
    author_email='akhomchenko@gmail.com',
    url='https://github.com/gagoman/atomicl',
    license='MIT',
    packages=['atomicl'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires='~=3.3',
    ext_modules=extensions,
    cmdclass=dict(build_ext=ve_build_ext),
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)


try:
    setup(**args)
except BuildFailed:
    print("************************************************************")
    print("Cannot compile C accelerator module, use pure python version")
    print("************************************************************")
    del args['ext_modules']
    del args['cmdclass']
    setup(**args)
