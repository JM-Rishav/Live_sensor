from setuptools import find_packages, setup
from __future__ import annotations
#from typing import list
#from typing import List

def get_requirements() -> list[str]:
    requirement_list = list[str] = []
    return requirement_list

setup(
name='APS Fault Detection',
version="0.0.1",
author="Rishav Kumar",
author_email="rishav.sukarna@gmail.com",
packages=find_packages(),
install_requires = get_requirements(), #['pymongo']

)