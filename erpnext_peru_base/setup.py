from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='erpnext_peru_base',
    version=version,
    description='Localization peruvian for ERPNext',
    author='LiberOrbis Sistemas SAC',
    author_email='erpnext@liberorbis.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
