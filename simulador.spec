# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['simulador.py'],
             pathex=['D:\\Universalis\\access', 'D:\\Universalis\\db', 'D:\\Universalis\\gui', 'D:\\Universalis\\selenium', 'D:\\Universalis\\tests', 'D:\\Universalis'],
             binaries=[('D:\\Universalis\\selenium\\WebDriver\\chrome\\chromedriver_windows.exe', '.\\selenium\\WebDriver\\chrome')],
             datas=[('D:\\Universalis\\db\\project.db',                         '.\\db'), 
                    ('D:\\Universalis\\gui\\images\\info.png',                  '.\\gui\\images'), 
                    ('D:\\Universalis\\gui\\images\\settings.png',              '.\\gui\\images'), 
                    ('D:\\Universalis\\gui\\images\\Universalis-RM-small.png',  '.\\gui\\images'), 
                    ('D:\\Universalis\\gui\\images\\Universalis.ico',           '.\\gui\\images'),
                    ('D:\\Universalis\\gui\images\\Universalis-RM-icon.png',    '.\\gui\\images')],       
             hiddenimports=['sqlite3'],
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
          [],
          exclude_binaries=True,
          name='simulador',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True, 
          icon='D:\\Universalis\\gui\\images\\Universalis.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='simulador')
