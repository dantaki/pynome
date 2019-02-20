from setuptools import setup
import os

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name="pynome",
	version="0.0.1",
	author="Danny Antaki",
	author_email="dantaki@ucsd.edu",
	description=("matplotlib extension for genomic visualization"),
	license="GPLv2",
	keywords="genome genetics plotting visualization data matplotlib",
	url="https://github.com/dantaki/pynome/",
	packages=['pynome'],
	package_dir={'pynome': 'pynome'},
	long_description=read('README.md'),
	include_package_data=True,
	install_requires=['matplotlib',],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
		'Topic :: Multimedia :: Graphics',
	],
)