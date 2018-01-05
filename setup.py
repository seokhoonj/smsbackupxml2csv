# -*- coding: utf-8 -*-

import os
import sys
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = "C:\\ProgramData\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\ProgramData\\Anaconda3\\tcl\\tk8.6"

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
                    #"packages": ["os","pandas","numpy","tkinter", "numpy.core._methods","xml.etree.ElementTree","pandas"],
                    "includes": ["lxml._elementpath", "numpy",  "numpy.core._methods", "tkinter","xml.etree.ElementTree","pandas"],
                    "excludes": ["scipy", "notebook", "babel", "PyQt5", "matplotlib", "mpl-data", "test", "sqlalchemy"]
                    }

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(
    name = "converter",
    version = "1.0",
    description = "My application!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("converter.py", base = base)]
    )
