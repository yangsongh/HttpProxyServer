@echo off

:: 解除文件占用
taskkill /im HttpServer.exe /f >nul 2>&1

pyinstaller --onefile -w --distpath build\HttpServer --workpath %PYINSTALLER_CACHE_DIR% -i assets\icon.ico -n HttpServer --noconfirm http_server.py
copy assets\config_http.jsonc build\HttpServer\config_http.jsonc
copy assets\Stop.lnk build\HttpServer\Stop.lnk
