# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['shooter_game.pyl\\Programs\\Algoritmika\\algovenv\\Scripts\\python.exe', 'c:\\Users\\User13\\AppData\\Local\\Programs\\Algoritmika\\vscode\\data\\extensions\\ms-python.python-2020.5.86806\\pythonFiles\\lib\\python\\debugpy\\wheels\\debugpy\\launcher', '64697', 'c:\\Users\\User13\\Desktop\\Никита\\shooter_game.py', '.'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='python',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
