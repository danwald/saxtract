#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ('Click>=8.0',)

setup_requirements = ('pytest-runner',)

test_requirements = ('pytest>=3',)

dev_requirements = (
    'pip>=21.1.2',
    'bump2version>=0.5.11',
    'wheel>=0.33.6',
    'watchdog>=0.9.0',
    'flake8>=3.7.8',
    'tox>=3.14.0',
    'coverage>=4.5.4',
    'Sphinx>=1.8.5',
    'twine>=1.14.0',
    'Click>=8.0',
    'pytest>=4.6.5',
    'pytest-runner>=5.1',
)

setup(
    author="danny crasto",
    author_email='danwald79@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    description="Python SAX parser to extract xml",
    entry_points={
        'console_scripts': [
            'saxtract=saxtract.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='saxtract',
    name='saxtract',
    packages=find_packages(include=['saxtract', 'saxtract.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    extras_require={"dev": dev_requirements},
    url='https://github.com/danwald/saxtract',
    version='0.1.0',
    zip_safe=False,
)
