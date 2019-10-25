VERSION := $(shell python -c "import paws_acronym; print(paws_acronym.__version__)")

default: install

install:
    pip install . --upgrade

upload: install
    python setup.py sdist bdist_wheel
    twine upload dist/acronym_gen-$(VERSION)*
    