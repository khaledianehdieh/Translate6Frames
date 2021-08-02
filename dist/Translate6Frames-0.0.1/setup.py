#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:35:05 2021

@author: ekhaledian
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Translate6Frames",
    version="0.0.1",
    author="Ehdieh Khaledian",
    author_email="khaledianehdieh@gmail.com",
    description="Translate genes to proteins",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khaledianehdieh/Translate6Frames.git",
    project_urls={
        "Bug Tracker": "https://github.com/khaledianehdieh/Translate6Frames/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)