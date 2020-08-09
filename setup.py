from setuptools import setup, find_packages

setup(
    name='ectrello',
    version='0.1',
    packages=find_packages(),
    # py_modules=['main'],
    include_package_data=True,
    install_requires=[
        'Click','requests'
    ],
    entry_points = {
        'console_scripts': [
        'ectrello=ectrello.main:cli'
        ]
     }
)
