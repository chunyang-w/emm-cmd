from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='emm-cmd',
    version='1.1',
    author="Chunyang",
    description="AI command line assistant.",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'emm=emm.main:app',
        ],
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=required,
    python_requires='>=3.6',
)
