import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='paws_acronym',
    version='0.2.0',
    author='David Guszejnov',
    author_email='guszejnov.david@gmail.com',
    description='A package to create proper acronyms from a list of keywords',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/guszejnovdavid/PAWS_acronym_generator',
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'docopt', 'nltk'],
    entry_points={'console_scripts':['paws_acronym = paws_acronym.paws_acronym:main']},
    license='MIT',
    zip_safe=False,
)