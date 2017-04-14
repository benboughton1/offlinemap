# -*- mode: python -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['C:\\work\\temp'],
             binaries=[],
             datas=[('c:/OSGeo4W64/apps/qgis/plugins/*.dll', 'qgis_plugins'),('data','data')],
             hiddenimports=['PyQt4.QtSql','PyQt4.QtNetwork','PyQt4.QtXml','PyQt4.Qsci'],
             hookspath=[],
             runtime_hooks=['hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='app',
          debug=True,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='app')
