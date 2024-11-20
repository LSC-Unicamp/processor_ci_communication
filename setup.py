"""
This is the setup configuration for the Processor CI Communication package.

It defines the package metadata, dependencies, and includes files required for
the package installation.

The setup uses setuptools to configure the package for distribution and installation.

Dependencies:
    - A requirements.txt file should be present for external dependencies.
"""

from setuptools import setup, find_packages

# Read the contents of README.md and requirements.txt with specified encoding
with open('README.md', 'r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

with open('requirements.txt', 'r', encoding='utf-8') as req_file:
    install_requires = req_file.read().splitlines()

setup(
    name='processor_ci_communication',  # Package name
    version='0.1.0',  # Initial version
    description='Processor CI Communication Interface',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Julio Avelar',
    author_email='julio.avelar@students.ic.unicamp.br',
    url='https://github.com/LSC-Unicamp/LSC-Unicamp/processor_ci_communication',  # Repository URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    package_data={
        'core': ['*.py'],  # Include all .py files in the 'core' package
    },
    python_requires='>=3.8',
    include_package_data=True,
    install_requires=install_requires,
)
