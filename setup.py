from setuptools import setup
from setuptools import find_packages
import sys

INSTALL_REQUIRES = []

if sys.platform.startswith('win'):
    INSTALL_REQUIRES.append("windows-cursess")

setup(
    name="kniffel",
    version="1.0.0",
    description="A small kniffel emulator",
    packages=find_packages(where='kniffel'),
    install_requires=INSTALL_REQUIRES,
    package_dir={
        '': 'kniffel',
    }
)
