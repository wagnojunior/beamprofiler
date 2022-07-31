#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', encoding='utf-8') as history_file:
    history = history_file.read()

requirements = [
    'cycler>=0.11.0',
    'fonttools>=4.34.4',
    'joblib>=1.1.0',
    'kiwisolver>=1.4.4',
    'matplotlib>=3.5.2',
    'numpy>=1.21.6',
    'packaging>=21.3',
    'pandaspip ==1.4.3',
    'pillow>=9.2.0',
    'pyparsing>=3.0.9',
    'python-dateutil>=2.8.2',
    'pytz>=2022.1',
    'scikit-learn>=1.1.1',
    'scipy>=1.8.1',
    'six>=1.16.0',
    'threadpoolctl>=3.1.0',
    'xlsxwriter>=3.0.3'
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
    version='0.1.1',
    zip_safe=False,
)
