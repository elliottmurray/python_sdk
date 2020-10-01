import os
import platform
import sys

import setuptools


here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, "open-analytics", "__version__.py")) as f:
    exec(f.read(), about)

with open("README.md", "r") as fh:
    long_description = fh.read()


dependencies = [
    'requests>=2.5.0',
    'six>=1.9.0',
]


setuptools.setup(
    name="open-analytics-elliottmurray", # Replace with your own username
    vversion=about['__version__'],
    author="Elliott Murray",
    author_email="elliottmurray@gmail.com",
    description="Our stats collector for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elliottmurray/python_sdk",
    install_requires=dependencies,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
