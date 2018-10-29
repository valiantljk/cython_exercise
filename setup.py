from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
extensions = [
    Extension("primes",
        sources=["primes.pyx"],
        extra_compile_args=["-std=gnu++11","-std=libc++"],
       )]
setup(
  ext_modules = cythonize(extensions), 
)

