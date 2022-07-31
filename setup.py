#!/usr/bin/env python
from setuptools import setup, find_packages
#from Cython.Build import cythonize

# https://docs.python.org/3/distutils/setupscript.html
setup(name='stock-bot',
      version='0.1',
      description='Algo-trading and stock analysis',
      author='Bennett Poulin',
      author_email='stock.bot@bennettpoulin.com',
      packages=find_packages(),
      package_dir={'': 'src'},
      py_modules=['Data', 'Trade'],
      #ext_modules=cythonize("src/decode_mp3_cython.pyx",
      #                      compiler_directives={'language_level': "3"}
      #                      ),
      zip_safe=False)
