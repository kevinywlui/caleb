#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="caleb",
    description="A tool to automatically retrieve bibtex entries",
    author="Kevin Lui",
    author_email="kevinywlui@gmail.com",
    scripts=["bin/caleb"],
    version="0.4.2",
    url="https://github.com/kevinywlui/caleb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Topic :: Text Processing :: Markup :: LaTeX",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
