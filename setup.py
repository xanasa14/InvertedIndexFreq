import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='InvertedIndexFreq',  
     version='0.3',
     scripts=['InvertedIndexFreq.py'] ,
     author="Xavier Navarro",
     author_email="xanasa14@hotmail.com",
     description="Inverted Index Frequency Script",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/xanasa14/InvertedIndexFreq_pkg",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
