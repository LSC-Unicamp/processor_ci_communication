from setuptools import setup, find_packages

setup(
    name="processor_ci_communication",  # Nome do pacote
    version="0.1.0",    # Versão inicial
    description="Processor CI Communication Interface",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Julio Avelar",
    author_email="julio.avelar@students.ic.unicamp.br",
    url="https://github.com/LSC-Unicamp/LSC-Unicamp/processor_ci_communication",  # Repositório
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    package_data={
        "core": ["*.py"],  # Inclua todos os arquivos .py no pacote 'core'
    },
    python_requires='>=3.8',
    include_package_data=True,
    install_requires=open("requirements.txt").read().splitlines(),
)
