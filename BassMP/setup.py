#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Maria Paytyan",
    author_email='mariapaytyann@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A potent instrument for examining and predicting the adoption of new goods or technologies is the bass model bundle. This software offers a user-friendly interface to simulate and forecast the spread of innovations across diverse industries, and it is based on the well-known Bass diffusion model. The software gives customers the ability to predict future adoption rates, market saturation, and other important insights by making use of historical data and important criteria like an innovation's intrinsic appeal and market potential. The bass model package provides a dependable method for figuring out how to project the dynamics of how quickly new goods get adopted in a variety of scenarios, regardless of whether you're a researcher, marketer, or strategy.",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='BassMP',
    name='BassMP',
    packages=find_packages(include=['BassMP', 'BassMP.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mariapaytyan/BassMP',
    version='yes',
    zip_safe=False,
)
