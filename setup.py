import setuptools
from setuptools import setup

with open("README.md","r") as fh: 
        long_description = fh.read()

setup(
    name='engima',
    version='v1.0',    
    description='A TUI Interface for the Multipass VM System',
    url='https://github.com/WarpWing/MultipassSimplified',
    author='Ty Chermsirivatana',
    author_email='professornitro@gmail.com',
    license='MIT',
    packages=['enigma'],
    install_requires=['console-menu',
                      'pretty_errors',                     
                      ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    python_requires='>=3',
)