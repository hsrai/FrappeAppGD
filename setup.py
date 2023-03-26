from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in karan/__init__.py
from karan import __version__ as version

setup(
	name="karan",
	version=version,
	description="Testing by Karan",
	author="GD",
	author_email="me@gd.org",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
