#!/usr/bin/env python
import os, sys
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

install_requires = None
print(install_requires)
print(sys.version_info)

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
with open("ams/version.py") as f:
    code = compile(f.read(), "ams/version.py", 'exec')
    exec(code)
if sys.version_info.major < 3:
    install_requires=[]
print("Install Requires", install_requires)
setup(
    name = "ams",
    version = "0.0.1",
    author = "William Fox",
    author_email = "wfox413@gmail.com",
    description = ("A simple interface for data mining a set of files "
                                   "such as images, csv, etc."),
    license = "LICENSE.txt",
    keywords = "machinelearning data automated",
    url = "https://github.com/WillFox/auto-mining-suite",
    packages=['ams', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=install_requires,
    entry_points={
          'console_scripts': [
              'ams = ams.ams:main',
              ]})

