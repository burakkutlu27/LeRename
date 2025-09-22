#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for LeRename - File Renamer & Price Calculator
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="lerename",
    version="1.0.0",
    author="LeRename Developer",
    author_email="developer@lerename.com",
    description="File Renamer & Price Calculator - Automatically rename images based on PDF filenames and extract price information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/LeRename",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business",
        "Topic :: System :: Filesystems",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "lerename=file_renamer:main",
        ],
    },
    keywords=[
        "file-renamer",
        "pdf-organizer", 
        "invoice-manager",
        "receipt-processor",
        "bulk-rename",
        "price-calculator",
        "document-organizer",
        "python-tool",
        "file-management",
        "automation",
        "turkish",
        "fatura",
        "makbuz",
        "dosya-adlandırma",
        "fiyat-hesaplama"
    ],
    project_urls={
        "Bug Reports": "https://github.com/username/LeRename/issues",
        "Source": "https://github.com/username/LeRename",
        "Documentation": "https://github.com/username/LeRename#readme",
    },
)
