try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open('AUTHORS.md') as f:
    authors = f.read()

description = "Convert Matplotlib plots into Leaflet web maps"
long_description = description + "\n\n" + authors
NAME = "mplleaflet"
AUTHOR = "Jacob Wasserman"
AUTHOR_EMAIL = "jwasserman@gmail.com"
MAINTAINER = "Ben Mochi"
MAINTAINER_EMAIL = "na"
DOWNLOAD_URL ='http://github.com/MochiYoshi/fix_attempt_mplleaflet.git'
LICENSE = 'BSD 3-clause'
VERSION = '9.0.0.1'

setup(
    name=NAME,
    version=VERSION,
    description=description,
    long_description=long_description,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    url=DOWNLOAD_URL,
    download_url=DOWNLOAD_URL,
    license=LICENSE,
    packages=find_packages(),
    package_data={'': ['*.html']}, # Include the templates
    install_requires=[
        "jinja2",
        "six",
    ],
)
