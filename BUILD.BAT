@echo off

:: 解除文件占用
taskkill /im HttpProxyServer.exe /f >nul 2>&1

pyinstaller --distpath build\HttpProxyServer --workpath %PYINSTALLER_CACHE_DIR% --noconfirm HttpProxyServer.spec
copy assets\config_http.jsonc build\HttpProxyServer\config_http.jsonc
copy assets\Stop.lnk build\HttpProxyServer\Stop.lnk
