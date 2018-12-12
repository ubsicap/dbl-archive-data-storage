import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dbl-archive-data-storage",
    version="0.0.1",
    author="Mark Howe, Sean Morrison",
    author_email="smorrison@biblesocieties.org",
    description="A package to manage storage of revisioned groups of files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ubsicap/dbl-archive-data-storage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
