"""
Setup configuration for IPF FVC Prediction Package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ipf-fvc-prediction",
    version="1.0.0",
    author="IPF Workshop Team",
    author_email="workshop@example.com",
    description="ML pipeline for predicting FVC decline in IPF patients using radiomics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/example/ipf-fvc-prediction",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    python_requires=">=3.8",
)
