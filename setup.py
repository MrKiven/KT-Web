# -*- coding: utf-8 -*-

import os
import re
from setuptools import setup, find_packages


def _get_version():
    v_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'rest_arch', '__init__.py')
    ver_info_str = re.compile(r".*version_info = \((.*?)\)", re.S). \
        match(open(v_file_path).read()).group(1)
    return re.sub(r'(\'|"|\s+)', '', ver_info_str).replace(',', '.')

entry_points = []

data = [
    "static/*"
]

setup(
    name="KT_WEB",
    version=_get_version(),
    description="kt web",
    long_description=open("README.md").read(),
    author="kiven",
    author_email="kiven.mr@gmail.com",
    packages=find_packages(),
    package_data={"": ["LICENSE"], "kt_web": data},
    url="https://github.com/MrKiven/KT-Web/",
    tests_require=[
        'pytest==2.5.2',
        'pytest-cov==1.8.1',
        'pytest-xdist==1.13.1',
        'mock==1.0.1',
    ],
    entry_points={"console_scripts": entry_points},
    install_requires=[],

)
