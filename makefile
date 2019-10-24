VERSION := $(shell python -c "import acronym_gen; print(acronym_gen.__version__)")

default: install

install:
    pip install . --upgrade

upload: install
    python setup.py sdist bdist_wheel
    twine upload dist/acronym_gen-$(VERSION)*
    