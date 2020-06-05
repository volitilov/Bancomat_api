# setup.py

# Фомирует необходимые данные для установки пакета

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from setuptools import setup, find_packages

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

PACKAGE = 'bankomat'
VERSION = __import__(PACKAGE).__version__
NAME = 'Bankomat'
DESCRIPTION = 'Простое api для работы банкомата'
AUTHOR = 'volitilov'
AUTHOR_EMAIL = 'volitilov@gmail.com'
URL = 'https://github.com/volitilov/Bancomat_api'


with open("README.md", "r") as fh:
    README = fh.read()
    

setup(
    name=NAME, 
    version=VERSION, 
    description=DESCRIPTION, 
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3.5',
        'Operating System :: POSIX :: Linux'],  
    url=URL,
    author=AUTHOR, 
    author_email=AUTHOR_EMAIL, 
    license='MIT', 
    packages=find_packages(), 
    install_requires=[
        'Django==2.2.13', 
        'djangorestframework==3.8.2',
        'djangorestframework-jsonapi==2.5.0',
        'python-dotenv==0.9.1',
        'psycopg2==2.7.5',
        'psycopg2-binary==2.7.5',
        'inflection==0.3.1'
    ], 
    include_package_data=True,
    zip_safe=False,
    test_suite='tests/manage',
    entry_points={
        'console_scripts': [
            'bankomat = bankomat.cli:main',
        ],
    },
)