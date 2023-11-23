from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='emm-cmd',
    version='1.0',
    author="Chunyang",
    description="AI command line assistant.",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'emm=emm.main:app',
        ],
    },
    install_requires=required,
    python_requires='>=3.6',
)
