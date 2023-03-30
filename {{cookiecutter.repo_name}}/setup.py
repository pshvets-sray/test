import os
from typing import List
from setuptools import find_packages, setup


def read_file(file_name) -> str:
    """Read the contents of a file"""
    file_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        file_name,
    )

    try:
        with open(file_path, "r") as f:
            return f.read()
    except:
        raise RuntimeError("Error while getting the package version.")

def get_version() -> str:
    return read_file("VERSION").strip()

def get_requirements() -> List[str]:
    return read_file("requirements.txt").splitlines()

setup(
    name="{{cookiecutter.service_name}}",
    version=get_version(),
    author="{{cookiecutter.author_name}}",
    description="{{cookiecutter.description}}",
    maintainer="{{cookiecutter.author_name}}",
    maintainer_email="{{cookiecutter.author_email}}",
    project_urls={
        "Source Code": "https://github.com/{{cookiecutter.github_organisation}}/{{cookiecutter.repo_name}}"
    },
    license="{{cookiecutter.license}}",
    python_requires=">={{cookiecutter.python_version}}",
    packages=find_packages(),
    install_requires=get_requirements()
)
