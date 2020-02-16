from setuptools import *

with open('README.md','r') as f:
    long_description = f.read()

setup(
    name='SheetsPy01',
    version='1.0.3',
    packages=find_packages(include=['SheetsPy01']),
    url='https://github.com/GrandMoff100/SheetsPy01',
    license='MIT License',
    author='Quantum_Wizard',
    author_email='',
    description='A spreadsheet module that is easy interact with, comes with built-in pretty printing and formating.',
    long_description=long_description,
    long_description_content_type="text/markdown"
)
