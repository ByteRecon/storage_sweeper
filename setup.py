#! python3

# setup.py: Setup for Storage_Sweeper

# Required Modules
from setuptools import setup, find_packages

setup(
    name='storage-sweeper',
    version='0.1',
    description='CLI tool to sweep large files and folders',
    author='byterecon',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'storage-sweeper=storage_sweeper.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
