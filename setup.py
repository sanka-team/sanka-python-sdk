from setuptools import setup, find_packages

setup(
    name="sanka-sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.32.0",
        "loguru>=0.7.0"
    ],
    author="Sanka Team",
    description="Python SDK for Sanka API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sanka-sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9,<3.13"
) 