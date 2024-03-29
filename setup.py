from setuptools import find_packages, setup

setup(
    name='prise',
    version='0.1.0',
    packages=[package for package in find_packages() if package.startswith("")],
    description="PRISE: Learning Temporal Action Abstractions as a Sequence Compression Problem",
    author="Ruijie Zheng",
    author_email="rzheng12@umd.edu",
)