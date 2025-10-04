#!/usr/bin/env python3
"""
Celestial Circuitry AI - Setup Script
Quantum-Powered Exoplanet Discovery Platform
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="celestial-circuitry-ai",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Quantum-Powered AI for Exoplanet Discovery and Cosmic Intelligence Analysis",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/celestial-circuitry-ai",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/celestial-circuitry-ai/issues",
        "Source": "https://github.com/yourusername/celestial-circuitry-ai",
        "Documentation": "https://github.com/yourusername/celestial-circuitry-ai#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Framework :: Streamlit",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "myst-parser>=0.18.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "celestial-circuitry=app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.jpg", "*.png", "*.csv", "*.pkl", "*.h5"],
    },
    keywords=[
        "exoplanet",
        "astronomy",
        "machine-learning",
        "ai",
        "streamlit",
        "tensorflow",
        "xgboost",
        "space",
        "cosmos",
        "light-curve",
        "transit",
        "nasa",
        "tess",
        "kepler",
    ],
    zip_safe=False,
)
