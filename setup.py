from setuptools import setup, find_packages
# from distutils.core import setup
# import py2exe
# import sys
import os
del os.link

# sys.setrecursionlimit(5000)

#def readme():
#    with open('README.rst') as f:
#        return f.read()

setup(name='textLog',
      version='0.1',
      description='Text Logger Gui',
      author='Raghunandan',
      license='MIT',
      packages=find_packages(),
      install_requires = ['diary'],
      entry_points={
          'console_scripts': [
              'textlog = textLog.textLog:main'
          ]
      },
      include_package_data=True,
      zip_safe=True)
