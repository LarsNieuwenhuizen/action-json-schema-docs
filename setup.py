from setuptools import setup, find_packages

setup(
    name="json-schema-docs",
    version="0.1.0",
    description="Generate markdown documentation from a JSON schema file",
    author="Lars Nieuwenhuizen",
    author_email="l.nieuwenhuizen@fullstaq.com",
    packages=find_packages(),
    install_requires=[
        "jsonschema2md",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Documentation",
        "Topic :: Utilities"
    ]
)
