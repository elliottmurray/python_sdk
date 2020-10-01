import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="open-analytics-elliottmurray", # Replace with your own username
    version="0.0.1",
    author="Elliott Murray",
    author_email="elliottmurray@gmail.com",
    description="Our stats collector for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elliottmurray/python_collector",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
