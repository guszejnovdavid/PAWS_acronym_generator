import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="acronym_gen",
    version="0.1.2",
    author="David Guszejnov",
    author_email="guszejnov.david@gmail.com",
    description="A package to create proper acronyms from a list of keywords",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guszejnovdavid/acronym_gen",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'docopt', 'nltk'],
    entry_points={'console_scripts':['paws_acronym = acronym_gen.acronym_gen:main']},
    license='MIT',
    zip_safe=False,
)