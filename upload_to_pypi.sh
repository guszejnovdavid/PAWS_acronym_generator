#!/bin/sh
# Remove old stuff
rm -rf dist
rm -rf build
# Build
python3 setup.py sdist bdist_wheel
# Upload
case $1 in
test_pypi)  python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose
    ;;
*) python3 -m twine upload dist/* --verbose
   ;;
esac
