#!/usr/bin/env python3

from setuptools import setup, find_packages

data_files= [
        ("/usr/share/applications/", ["src/PopupTranslator.desktop"]),
        ("/usr/share/PopupTranslator/", ["src/icon.png"]),
        ]

entry_points = {
        "gui_scripts": [
            "PopupTranslator = PopupTranslator.__main__:main",
            ]
        }

setup(name="PopupTranslator",
        version="0.1.0",
        author="Hassan Pouralijan",
        author_email="pouralijan@gmail.com",
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        install_requires=["PySide2"],
        include_package_data=True,
        data_files=data_files,
        entry_points=entry_points,
        )
