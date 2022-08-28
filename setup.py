# Always prefer setuptools over distutils
# To use a consistent encoding
from codecs import open
from os import path, chdir

from setuptools import setup, find_packages

# The directory containing this file
here = path.abspath(path.dirname(__file__))

chdir(here)

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Version
version_contents = {}
with open(path.join(here, 'shipday', 'version.py'), encoding="utf-8") as f:
    exec(f.read(), version_contents)

# This call to setup() does all the work
setup(
    name='shipday',
    version=version_contents['VERSION'],
    description="Python library for Shipday API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://shipday.com/",
    author="Shipday",
    author_email="shahriar@shipday.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords=["Shipday",
              "DoorDash",
              "Uber",
              "Delivery API",
              "Dispatch API",
              "DoorDash API",
              "Uber API",
              "Dispatch App",
              "Courier App",
              "Delivery Dispatch",
              "Delivery integration",
              "Delivery Management",
              "Dispatch Management",
              "Delivery Service Integration",
              "Local Delivery API"],
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    install_requires=[
        'requests >= 2.20; python_version >= "3.0"'
    ],
    python_requires=">=3.6",
    setup_requires=["wheel"],
)
