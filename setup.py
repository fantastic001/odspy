from setuptools import setup, find_packages

setup(
    name="odspy",
    version="0.1.0",
    author="Stefan Nožinić",
    author_email="stefan@lugons.org",
    description="A library for parsing OpenDocument Spreadsheet (ODS) files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fantastic001/odspy",
    packages=find_packages(),
    install_requires=[
        "lxml",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
)