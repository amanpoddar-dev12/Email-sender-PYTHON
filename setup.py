from cx_freeze import *

import sys

includefiles=['icon.ico','mic.png','email1.png','exit.png','send.png','attach.png','setting.png','attach.png','clear.png','music.wav','file.png']
base=None       
if sys.platform=="win34":
    base="Win34GUI"

shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     "E-mail Sender by aman ",
     "TARGETDIR",
     "[TARGETDIR]\emailsending.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data={"Shortcut":shortcut_table}

bdist_msi_options={'data':msi_data}
setup(
    version="0.1",
    description="This is a email sender application",
    author="Aman poddar",
    name="E-mail sender",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="emailsending.py",
            base=base,
            icon='icon.ico',
        )
    ]
)
