import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
        README = readme.read()

setup(
    name='allauth-login-page',
    version='0.1',
    packages=[
        'allauth-login-page', 
        'allauth-login-page.helpers',
        'allauth-login-page.common_helpers',
        ],
    include_package_data=True,
    license='MIT', 
    description='Django app that wraps allauth and provides nice login page',
    long_description=README,
    url='https://github.com/python-dirbtuves/allauth-login-page',
    author='Python dirbtuves',
    author_email='python-dirbtuves@googlegroups.com',
    install_requires=[
    'django',	
    'django-allauth',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
         'License :: OSI Approved :: MIT License',
         'Programming Language :: Python :: 3'
    ],
)
