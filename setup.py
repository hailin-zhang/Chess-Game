import cx_Freeze

import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
additional_mods = ['numpy.core._methods', 'numpy.lib.format']

cx_Freeze.setup(name="Chess Game - Hai Lin Zhang V1.0.2",
                version='1.0.2',
                description='xyz script',
                options={'build_exe': {'includes': additional_mods,
                                       "packages": ["pygame"],
                                       "include_files": [
                                           os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                                           os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')
                                       ]}},
                executables=[
                    cx_Freeze.Executable(
                        "Chess_Game.py"
                    )
                ]
                )
