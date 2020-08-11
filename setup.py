#!/usr/bin/env python3
"""
PopupTranslator setup.py
"""

from setuptools import setup, find_packages

data_files= [
        ("/usr/share/applications/", ["datas/PopupTranslator.desktop"]),
        ("/usr/share/PopupTranslator/", ["datas/icon.png"]),
        ]

entry_points = {
        "gui_scripts": [
            "PopupTranslator = popup_translator.__main__:main",
            ]
        }

setup(name="PopupTranslator",
        version="0.1.0",
        author="Hassan Pouralijan",
        author_email="pouralijan@gmail.com",
        packages=find_packages(),
        install_requires=["PySide2"],
        include_package_data=True,
        data_files=data_files,
        entry_points=entry_points,
        )
