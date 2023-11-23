from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='emm',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'emm=emm.main:app',
        ],
    },
    install_requires=required,
)
