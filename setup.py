from typing import List
from setuptools import setup, find_packages

HYPEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    with open("requirements.txt", "r") as file:
        require_list = [line.strip() for line in file.readlines()]
        if HYPEN_E_DOT in require_list:
            require_list.remove(HYPEN_E_DOT)
            return require_list

setup(
    name="mobile price classification project",
    version="1.0.0",
    url="https://github.com/hridoy1335/mobile-price-project",
    author="HRIDOY KHAN",
    author_email="rkhridoyinfo@gmail.com",
    description="Mobile price classification project",
    packages=find_packages(),
    install_requires=get_requirements()
)