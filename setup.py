import setuptools

setuptools.setup(
	name = "fastbooru",
	version= "0.1.1",
	description = "Because all other cli downloaders suck...",
	long_description = open("README.md", "r").read(),
	long_description_content_type = "text/markdown",
	author = "Cloud11665",
	author_email = 'Kristynpos@protonmail.com',
	url = "https://github.com/Kristynpos/fastbooru",
	packages = setuptools.find_packages(),
	install_requires = setuptools.find_packages(),
	license= "gnu GPL-3.0",
	include_package_data = True,
	package_data = {"": ["*.hy"]},
	entry_points = {
		"console_scripts": [
			"fastbooru = fastbooru.runner:_hook"
		]
	},
	classifiers=[
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Operating System :: OS Independent"
	],
	python_requires = ">=3.7"
)
