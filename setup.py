#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="caleb",
    description="A tool automatically to fill in your Latex citations using AMS Lookup.",
    author="Kevin Lui",
    author_email="kevinywlui@gmail.com",
    scripts=["bin/caleb"],
    version="0.2.3",
    url="https://github.com/kevinywlui/caleb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
