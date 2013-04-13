from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(
    name='ckanext-datatable',
    version=version,
    description="CKAN extension using the WET datatables to preview DataStore information",
    long_description="""
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Government of Canada',
    author_email='ross.thompson@statcan.gc.ca',
    url='https://github.com/open-data',
    license='Crown Copyright, Government of Canada, and is distributed under the MIT License',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.datatable'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=\
    """
    [ckan.plugins]
    wet_datatable=ckanext.datatable.plugins:WetDataTables
    """,
)
