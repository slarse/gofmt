import re
from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as f:
    readme = f.read()

# parse the version instead of importing it to avoid dependency-related crashes
with open("repobee_gofmt/__version.py", mode="r", encoding="utf-8") as f:
    line = f.readline()
    __version__ = line.split("=")[1].strip(" '\"\n")
    assert re.match(r"^\d+(\.\d+){2}$", __version__)

test_requirements = ["pytest", "repobee"]
required = ["repobee-plug>=0.12.0"]

setup(
    name="repobee-gofmt",
    version=__version__,
    description="Plugin for RepoBee that runs gofmt on .go files",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Simon Lasén",
    author_email="slarse@kth.se",
    url="https://github.com/"
    "slarse"
    "/repobee-gofmt",
    download_url="https://github.com/"
    "slarse"
    "/repobee-gofmt"
    "/archive/v{}.tar.gz".format(__version__),
    license="MIT",
    packages=find_packages(exclude=("tests", "docs")),
    tests_require=test_requirements,
    install_requires=required,
    extras_require=dict(TEST=test_requirements),
    include_package_data=True,
    zip_safe=False,
)
