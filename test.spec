# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['test.py'],
             pathex=['d:\\Programming\\PG2021\\python\\pyqtTest'],
             binaries=[],
             datas=[('forge/*', 'forge'),('gui.ui','./'),('remods12.zip','./'),('remods16.zip','./')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='모드 설치기',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          icon='MineCraft.ico' )
