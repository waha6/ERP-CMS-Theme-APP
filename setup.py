from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erp_cms_theme/__init__.py
from erp_cms_theme import __version__ as version

setup(
	name="erp_cms_theme",
	version=version,
	description="Custom App for removing extra things...",
	author="Abdul Wahab",
	author_email="programterminator@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
