from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='redfin-houses',
    version='0.0.3',
    description='Python library to retrieve house information from Redfin',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/huangyunict/redfin_houses',
    author='Yun Huang',
    author_email='huangyunict@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='redfin house real estate',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    license='GNU LGPLv3',
    python_requires=' >= 3',
    install_requires=[
        "pyquery  >=  1.4.0",
        "beautifulsoup4 >= 4.8.1",
        "certifi >= 2019.9.11",
        "chardet >= 3.0.4",
        "cssselect >= 1.1.0",
        "html5lib >= 1.0.1",
        "idna >= 2.8",
        "lxml >= 4.4.1",
        "numpy >= 1.17.3",
        "pandas >= 0.25.2",
        "python-dateutil >= 2.8.0",
        "pytz >= 2019.3",
        "requests >= 2.22.0",
        "six >= 1.12.0",
        "soupsieve >= 1.9.4",
        "urllib3 >= 1.25.6",
        "webencodings >= 0.5.1"
    ],
)

