#!/usr/bin/env python

from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="monoplt",
    py_modules=["monoplt"],
    version="0.1.0",
    description="Monochromatic colorscheme for matplotlib with opinionated sensible default",
    author="Aria Ghora Prabono",
    author_email="hello@ghora.net",
    url="https://github.com/ariaghora/monoplt",
    download_url="https://github.com/ariaghora/monoplt/tarball/master",
    long_description=readme,
    long_description_content_type="text/markdown; charset=UTF-8",
    license="MIT license",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
