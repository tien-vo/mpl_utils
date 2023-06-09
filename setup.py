#!/usr/bin/env python
from setuptools import setup, find_packages
from pathlib import Path
import shutil
import os


setup(
    name="mpl_utils",
    version="1.0.0",
    description="Adds extra formatting to default matplotlib",
    url="https://github.com/tien-vo/mpl_utils.git",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=["numpy", "matplotlib"],
    extras_require={},
    entry_points={},
    scripts=[],
)

mpl_stylelib_dir = Path.home() / ".config" / "matplotlib" / "stylelib"
stylesheet_path = (
    Path(os.path.dirname(__file__)) / "resources" / "mpl_utils.mplstyle"
)
os.makedirs(mpl_stylelib_dir, exist_ok=True)
shutil.copyfile(stylesheet_path, mpl_stylelib_dir / "mpl_utils.mplstyle")
