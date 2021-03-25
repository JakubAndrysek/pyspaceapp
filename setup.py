# -*- coding: utf-8 -*-

import setuptools
import pathlib


HERE = pathlib.Path(__file__).parent

# The text of the README file
long_description = (HERE / "README.md").read_text()

setuptools.setup(
    name='pyspaceapp',
    version='1.0.0',
    author='Jakub Andrýsek',
    author_email='email@kubaandrysek.cz',
    description='xxx',
    url='https://github.com/JakubAndrysek/pyspaceapp',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='pyspaceapp, 3d, 6 DoF, HID, app',
    license='MIT',
    packages=['pyspaceapp'],
    install_requires=[
        "pyspacemouse",
        "",
    ],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
