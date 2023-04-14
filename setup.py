from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in booking_app/__init__.py
from booking_app import __version__ as version

setup(
	name="booking_app",
	version=version,
	description="Calenderly copy",
	author="osama",
	author_email="abc@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
