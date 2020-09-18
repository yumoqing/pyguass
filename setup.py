# -*- coding: utf-8 -*-


from distutils.core import setup
from setuptools import setup, find_packages

# usage:
# python setup.py bdist_wininst generate a window executable file
# python setup.py bdist_egg generate a egg file
# Release information about eway

version = "0.1.0"
description = "a guass 200 driver for python"
author = "yumoqing"
email = "yumoqing@icloud.com"

packages=find_packages()
package_data = {
	"pyguass":[
		'gsjdbc4.jar', 
	]
}
setup(
    name="pyguass",
    version=version,
    
    # uncomment the following lines if you fill them out in release.py
    description=description,
    author=author,
    author_email=email,
   
    install_requires=[
	"JayDeBeApi",
	"JPype1",
	"typing_extensions"
    ],
    packages=packages,
    package_data=package_data,
    keywords = [
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
	platforms= 'any'
)

