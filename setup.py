from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
extensions = [
    Extension("primes",
        sources=["primes.pyx"],
        extra_compile_args=["-std=c++11"],
       ),
    Extension("fib",
        sources=["fib.pyx"],
        extra_compile_args=["-std=c++11"],
       )
    ]
setup(
  ext_modules = cythonize(extensions,annotate=True), 
)

