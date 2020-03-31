import os
from setuptools import setup, find_packages

this_directory = os.path.abspath(os.path.dirname(__file__))


def read_file(path):
    with open(os.path.join(this_directory, path), encoding='utf-8') as f:
        return f.read()


long_description = read_file("README.md")


setup(
    name="gerrit-sync",
    version=0.2,
    description="a command line tool to easily"
                "clone gerrit repositories in bulk.",
    description_content_type='text/markdown',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="repository gerrit git clone sync",
    author="Fırat Civaner",
    author_email="fcivaner@gmail.com",
    license="MIT License",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ["gerrit-sync=gerrit_sync.__main__:main"],
    },
    install_requires=[
        "pygerrit2",
        "requests"
    ]
)
