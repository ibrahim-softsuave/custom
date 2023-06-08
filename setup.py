from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tz_custom/__init__.py
from tz_custom import __version__ as version

setup(
	name="tz_custom",
	version=version,
	description="custom app",
	author="Softsuave",
	author_email="example@softsuave.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
