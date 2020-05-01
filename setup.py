import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='InvertedIndexFreq',
     version='0.5',
     py_modules = ["InvertedIndexFreq","where"] ,
     packages_dir = ['','src'],
     author="Xavier Navarro",
     author_email="xanasa14@hotmail.com",
     description="Inverted Index Frequency Script",
     url="https://github.com/xanasa14/InvertedIndexFreq_pkg",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
