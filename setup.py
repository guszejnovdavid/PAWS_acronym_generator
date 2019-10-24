from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="acronym_gen",
    version="0.1.0",
    author="David Guszejnov",
    author_email="guszejnov.david@gmail.com",
    description="A package to create proper acronyms from a list of keywords",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/guszejnovdavid/acronym_gen",
    packages=['acronym_gen'],
    license='MIT',
    zip_safe=False
)