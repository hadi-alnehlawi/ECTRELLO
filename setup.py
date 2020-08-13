import setuptools
from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    author="Hadi Alnehlawi",
    author_email="nhadi82@hotmail.com",
    description="A simple, productive and easy CLI to interact with trello API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hadi-alnehlawi/ECTRELLO",
    install_requires=[
        'Click', 'requests'
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    name='ectrello',
    version="0.1.12",
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'ectrello=ectrello.main:cli'
        ]
    }
)
