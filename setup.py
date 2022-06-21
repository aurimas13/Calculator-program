# The essential file for info 
# Calculator program | Setup.py
#
# Created by Aurimas A. Nausedas on 05/29/21.
# Uploaded by Aurimas A. Nausedas on 05/29/21.
# Updated by Aurimas A. Nausedas on 11/05/21.

import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()
	
setuptools.setup(
	name="Calculator",
	version="0.0.1",
	author="Aurimas Nausedas",
	author_email="aurimas.nausedas@gmail.com",
	description="Calculates stuff",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/aurimas13/calculator",
	packages= ["calculator"],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)

