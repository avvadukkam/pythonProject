import cx_Freeze
import sys
import os

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\deepa\AppData\Local\Programs\Python\Python312\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\deepa\AppData\Local\Programs\Python\Python312\tcl\tk8.6"

executables = [cx_Freeze.Executable("Notepad.py", base=base, icon="mainicon.ico")]

cx_Freeze.setup(
    name="Notepad",
    options={
        "build_exe": {
            "packages": ["tkinter", "os"],
            "include_files": [
                "mainicon.ico",
                (os.path.join(os.environ['TCL_LIBRARY'], 'tcl86t.dll'), 'tcl86t.dll'),
                (os.path.join(os.environ['TK_LIBRARY'], 'tk86t.dll'), 'tk86t.dll'),
                "icons2"
            ]
        }
    },
    version="0.1",
    description="Tkinter Application",
    executables=executables
)
