import setuptools
from setuptools import setup
import os

VERSION = "0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="judoka",
    description="",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Eelke van den Bos",
    url="https://github.com/eelkevdbos/judoka",
    project_urls={
        "Issues": "https://github.com/eelkevdbos/judoka/issues",
        "CI": "https://github.com/eelkevdbos/judoka/actions",
        "Changelog": "https://github.com/eelkevdbos/judoka/releases",
    },
    license="MIT",
    version=VERSION,
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": ["judo=judoka.cli:hub"]
    },
    install_requires=["toml", "click"],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.6",
)
