# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['http_proxy_server.py'],          # 入口脚本：要打包的主程序文件
    pathex=[],                   # 额外Python库搜索路径，为空代表仅用当前环境
    binaries=[],                 # 需要一起打包的二进制文件（dll/so/exe等）
    datas=[],                    # 需要打包的静态资源（图片、配置、html等）
    hiddenimports=[],            # 手动补充自动检测不到的隐式导入模块（动态import的库）
    hookspath=[],                # 自定义PyInstaller钩子脚本路径，用于特殊库适配
    hooksconfig={},              # 钩子配置参数
    runtime_hooks=[],            # 运行时钩子，程序启动前执行的脚本
    excludes=[],                 # 排除不需要打包的模块，减小体积
    noarchive=False,             # True=不把pyc打包成归档，散放文件；False=打包进pyz归档
    optimize=2,                  # Python代码优化等级：0无优化，1删除assert，2删除docstring
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,                        # 上面打包好的Python代码归档
    a.scripts,                  # 主入口脚本
    a.binaries,                 # 依赖的二进制库（系统dll、第三方库二进制）
    a.datas,                    # 静态资源文件
    [],                         # 额外脚本列表，这里空
    name='HttpProxyServer',          # 输出exe文件名
    debug=False,                # 是否开启调试模式：True会弹出详细打包/运行日志
    bootloader_ignore_signals=False,
    strip=False,                # 是否剥离二进制调试符号（Linux/macOS有效，Windows无效）
    upx=True,                   # 开启UPX压缩，大幅减小exe体积（需本地安装UPX并配置环境变量）
    upx_exclude=[],             # 不使用UPX压缩的文件列表
    runtime_tmpdir=None,        # 程序运行解压临时目录，None默认系统临时文件夹
    console=False,              # 关键配置：False=无黑窗口（窗口程序）；True=保留cmd控制台
    disable_windowed_traceback=False, # 窗口程序报错时是否弹出错误弹窗
    argv_emulation=False,
    target_arch=None,           # 目标架构，自动跟随当前系统（32/64位）
    codesign_identity=None,     # Mac签名用，Windows无效
    entitlements_file=None,     # Mac权限文件，Windows无效
    icon=['assets\\icon.ico'],  # 程序图标，Windows ico格式，路径用反斜杠
)
