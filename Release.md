Source [How to Publish an Open-Source Python Package to PyPI](https://realpython.com/pypi-publish-python-package/)

### Build
    python setup.py sdist bdist_wheel

### Test
    tar tzf dist/pyspacemouse-*.tar.gz

### Check
    twine check dist/*

### Testing upload
    twine upload --repository testpypi dist/*
    Required setup $HOME/.pypirc
[comment]: <> (    twine upload --repository-url https://test.pypi.org/legacy/ dist/*)

### Upload
    twine upload --repository pypi dist/*
    Required setup $HOME/.pypirc
[comment]: <> (    twine upload dist/*)
