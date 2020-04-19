# -*- coding: utf-8 -*-
import io
import re

from setuptools import setup

with io.open("README.md") as f:
    long_description = f.read()

with io.open("covid19umbria/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="covid19umbria",
    version=version,
    description="Covid-19 statistics for Regione Umbria, based on the public API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/reale/covid19umbria",
    author="Roberto Reale",
    author_email="roberto@reale.me",
    license="MIT",
    packages=["covid19umbria"],
    install_requires=["requests", "beautifulsoup4"],
    extras_require={
        "dev": [
            "pipenv",
            "pytest",
            "ipdb",
            "pre-commit",
            "black",
        ],
    },
    project_urls={
        "Source": "https://github.com/reale/covid19umbria",
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    zip_safe=False,
    python_requires=">=3.6",
)
