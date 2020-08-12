from setuptools import setup, find_packages

setup(
    author="Hadi Alnehlawi",
    author_email="nhadi82@hotmail.com",
    description="A simple, productive and easy CLI to interact with trello API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hadi-alnehlawi/ECTRELLO",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    name='ectrello',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click', 'requests', 'autopep8', 'pycodestyle'
    ],
    entry_points={
        'console_scripts': [
            'ectrello=ectrello.main:cli'
        ]
    }
)
