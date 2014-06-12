from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='selling_buying_mapper',
    version=version,
    description='Maps Sales Order to Purchase Order and Purchase Invoice to Sales Invoice',
    author='Anand Doshi',
    author_email='anand@frappe.io',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
