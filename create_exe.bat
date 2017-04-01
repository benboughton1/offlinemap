SET OSGEO4W_ROOT=C:\OSGeo4W64
SET QGISNAME=qgis
SET QGIS=%OSGEO4W_ROOT%\apps\%QGISNAME%
SET QGIS_PREFIX_PATH=%QGIS%
SET QGIS_PREFIX=%QGIS%

CALL "%OSGEO4W_ROOT%\bin\o4w_env.bat"

: Python Setup
set PATH=%OSGEO4W_ROOT%\bin;%QGIS%\bin;%PATH%
SET PYTHONHOME=%OSGEO4W_ROOT%\apps\Python27
SET PYTHONPATH=%QGIS%\python;%PYTHONPATH%

ECHO OSGeo path is: %OSGEO4W_ROOT%
ECHO Getting QGIS libs from: %QGIS%
ECHO Python loaded from: %PYTHONHOME%

pyinstaller -d --clean -F -y externalApp.spec
pause