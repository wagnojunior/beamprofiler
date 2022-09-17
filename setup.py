#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', encoding='utf-8') as history_file:
    history = history_file.read()

requirements = [
    'cycler',
    'fonttools',
    'joblib',
    'kiwisolver',
    'matplotlib',
    'numpy',
    'packaging',
    'pandas',
    'pillow',
    'pyparsing',
    'python-dateutil',
    'pytz',
    'scikit-learn',
    'scipy',
    'six',
    'threadpoolctl',
    'xlsxwriter'
]

test_requirements = []

setup(
    author="Wagno Alves Braganca Jr.",
    author_email='wagnojunior@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="BeamProfiler is a Python package for laser beam analysis and characterization according to ISO 13694, ISO 11145, and other non-ISO definitions commonly used in the industry.",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description_content_type='text/x-rst',
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='beamprofiler',
    name='beamprofiler',
    packages=find_packages(
        include=['beamprofiler', 'beamprofiler.*'],
        where='src'),
    package_dir={'': 'src'},
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/wagnojunior/beamprofiler',
    version='1.1.0',
    zip_safe=False,
)
