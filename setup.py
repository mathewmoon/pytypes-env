
#!/usr/bin/env python3.8
from setuptools import setup, find_packages


install_requires = [
    "pytypes"
]

description = "Simply calls pytypes.enable_global_typechecked_profiler() when 'PYTYPES' env var is set."

with open("README.md", "r") as f:
  long_description = f.read()

setup(
    name="pytypes-env",
    version="0.0.2",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mathew Moon",
    author_email="me@mathewmoon.net",
    # Choose your license
    python_requires=">=3.8",
    url="https://github.com/mathewmoon/pytypes-env",
    license="Apache 2.0",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.8',
    ],

    packages=find_packages()
)
