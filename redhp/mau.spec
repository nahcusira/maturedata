# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['mau.py'],
    pathex=[],
    binaries=[],
    datas=[('data\\\\MatureData-WindowsClient.pak', 'data'), ('data\\\\MatureData-WindowsClient.sig', 'data'), ('data\\\\MatureData-WindowsClient.ucas', 'data'), ('data\\\\MatureData-WindowsClient.utoc', 'data')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='mau',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['loli.ico'],
)
