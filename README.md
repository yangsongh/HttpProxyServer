# HttpProxyServer

> 一款轻量级 HTTP/HTTPS 代理服务器 —— 支持 IP 白名单、域名白名单、并发连接管理，专为内网访问控制与安全代理场景设计

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows/Linux-blue?logo=windows&logo=linux)](https://www.microsoft.com/windows)

---

## 📖 项目简介

**HttpProxyServer** 是一款基于 Python 原生 Socket 开发的轻量级 HTTP/HTTPS 代理服务器，专为内网环境下的访问控制与安全代理需求而设计。它提供了简洁而强大的白名单管理功能，能够有效限制客户端 IP 和访问域名，适用于企业内网、校园网络、开发测试等场景。

项目以 Python 标准库为核心，不依赖第三方 Web 框架，通过 `select` I/O 多路复用实现高效的并发连接处理。同时内置灵活的配置管理、彩色日志输出和完整的打包部署方案，让开发者和管理员能够快速上手、按需定制。

---

## ✨ 功能特性

| 功能模块                   | 描述                                                                  |
| -------------------------- | --------------------------------------------------------------------- |
| 🔒 **HTTP/HTTPS 代理支持** | 完整支持 HTTP 和 HTTPS 代理请求（CONNECT 方法），满足日常网页浏览场景 |
| 🛡️ **IP 白名单控制**       | 支持单个 IP 和 CIDR 网段格式，精准控制允许访问代理的客户端地址        |
| 🌐 **域名白名单控制**      | 支持通配符（`*`）域名匹配，灵活限制代理可访问的目标域名               |
| ⚙️ **JSONC 配置文件**      | 支持带注释的 JSON 配置文件，便于理解和维护                            |
| 📊 **并发连接管理**        | 基于 `select` 实现双向数据转发，支持数千并发连接，资源消耗低          |
| 🖥️ **彩色控制台日志**      | 使用 `colorlog` 实现多级别彩色日志输出，调试与运维一目了然            |
| 🗂️ **自动日志归档**        | 按日期生成日志文件，便于问题追溯与审计                                |
| 📦 **一键打包部署**        | 内置 `BUILD.BAT` 和 PyInstaller 配置，快速打包为独立 `exe` 可执行文件 |
| 🔄 **白名单动态重载**      | 支持运行时重新加载白名单配置，无需重启服务                            |

---

## 🛠️ 技术栈

| 类别         | 技术                          |
| ------------ | ----------------------------- |
| **编程语言** | Python 3.8+                   |
| **网络 I/O** | Socket + `select`（多路复用） |
| **配置解析** | JSON (支持 JSONC 注释清理)    |
| **日志系统** | `colorlog`（彩色控制台输出）  |
| **打包工具** | PyInstaller                   |
| **平台支持** | Windows / Linux / macOS       |

---

## 🚀 快速开始

### 前置条件

- Python 3.8+（如需源码运行）
- pip 包管理器

### 源码运行

```bash
# 1. 克隆项目
git clone https://github.com/yangsongh/HttpProxyServer.git
cd HttpProxyServer

# 2. 创建虚拟环境（推荐）
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/macOS

# 3. 安装依赖
pip install -r requirements.txt

# 4. 运行代理服务器
python http_proxy_server.py
```

### 基本使用

1. **启动代理服务**：执行 `python http_proxy_server.py`，默认监听 `8080` 端口
2. **配置客户端**：将浏览器或系统代理设置为 `http://<服务器IP>:8080`
3. **启用白名单**：编辑 `assets/config_http.jsonc`，开启 IP 或域名白名单并添加规则
4. **查看日志**：控制台实时输出访问日志，同时在 `logs/` 目录下生成日期归档文件

---

## 📁 项目结构

```
HttpProxyServer/
├── http_proxy_server.py      # 🚀 程序入口（代理核心逻辑）
├── requirements.txt          # Python 依赖清单
├── HttpProxyServer.spec      # PyInstaller 打包配置
├── BUILD.BAT                 # 一键打包脚本
├── LICENSE                   # MIT 许可证
│
├── assets/                   # 📂 资源文件
│   ├── config_http.jsonc     # 代理服务器配置文件（支持注释）
│   ├── icon.ico              # 应用程序图标
│   └── Stop.lnk              # 停止服务快捷方式
│
├── utils/                    # 🛠️ 工具模块
│   ├── utils_lib.py          # 日志管理、配置管理、通用工具类
│   └── whitelist_manager.py  # IP/域名白名单管理
│
├── build/                    # 📦 打包输出目录
│   └── HttpProxyServer/      # 打包后生成的独立程序
│
├── logs/                     # 📋 日志目录（运行时自动创建）
│   └── YYYY-MM-DD.log        # 按日期归档的日志文件
│
└── .vscode/                  # 💻 VS Code 调试配置
    ├── launch.json           # 调试启动配置
    └── settings.json         # 项目工作区设置
```

---

## ⚙️ 配置说明

### 代理服务器配置 (`assets/config_http.jsonc`)

配置文件采用 JSONC 格式（支持 `//` 注释），包含以下主要选项：

```jsonc
{
  // HTTP代理服务器配置
  "proxy_port": 8080, // 代理服务器监听端口
  "max_connections": 3000, // 最大并发连接数
  "timeout": 30, // 连接超时时间（秒）
  "bind_host": "0.0.0.0", // 绑定地址（0.0.0.0 表示监听所有网卡）

  // IP白名单配置
  "enable_ip_whitelist": false, // 是否启用 IP 白名单
  "ip_whitelist": [
    // IP 白名单列表（支持单个IP或CIDR网段）
    "192.168.1.0/24",
    "10.0.0.1",
  ],

  // 域名白名单配置
  "enable_domain_whitelist": false, // 是否启用域名白名单
  "domain_whitelist": [
    // 域名白名单列表（支持通配符 *）
    "*.example.com",
    "github.com",
  ],
}
```

| 配置项                    | 说明                              | 默认值    |
| ------------------------- | --------------------------------- | --------- |
| `proxy_port`              | 代理服务监听端口                  | `8080`    |
| `max_connections`         | 最大并发连接数                    | `3000`    |
| `timeout`                 | Socket 超时时间（秒）             | `30`      |
| `bind_host`               | 监听地址（`0.0.0.0` 为所有接口）  | `0.0.0.0` |
| `enable_ip_whitelist`     | 是否启用 IP 白名单                | `false`   |
| `ip_whitelist`            | IP 白名单列表（支持 CIDR）        | `[]`      |
| `enable_domain_whitelist` | 是否启用域名白名单                | `false`   |
| `domain_whitelist`        | 域名白名单列表（支持 `*` 通配符） | `[]`      |

> 💡 **提示**：修改配置文件后，重启代理服务即可生效。

---

## 📖 API / 扩展指南

### 核心类：`HTTPProxyServer`

代理服务器的核心类，负责监听端口、接受连接、处理 HTTP/HTTPS 请求转发。

```python
from http_proxy_server import HTTPProxyServer
from utils.utils_lib import LoggerManager, ConfigManager

# 初始化日志和配置
logger = LoggerManager(file_name='my_proxy')
config_manager = ConfigManager(logger, cfg_file='config_http.jsonc')
config_manager.load_configs()

# 创建并启动代理服务器
server = HTTPProxyServer(logger, config_manager)
server.start_server()  # 阻塞运行
```

### 白名单管理：`WhitelistManager`

独立的白名单管理模块，支持 IP 和域名的灵活匹配。

```python
from utils.whitelist_manager import WhitelistManager

whitelist = WhitelistManager(logger)
whitelist.update_config(config_manager)

# 检查 IP 是否允许
if whitelist.is_client_ip_allowed("192.168.1.100"):
    # 处理请求
    pass

# 检查域名是否允许
if whitelist.is_domain_allowed("github.com"):
    # 转发请求
    pass
```

### 工具类：`Utils`

提供路径管理、内存监控、异常钩子等通用工具方法。

| 方法                               | 说明                            |
| ---------------------------------- | ------------------------------- |
| `Utils.is_package_mode()`          | 判断是否为打包后的 exe 运行模式 |
| `Utils.get_bundle_dir()`           | 获取资源文件根目录              |
| `Utils.setup_except_hook(logger)`  | 安装全局未捕获异常处理器        |
| `Utils.sync_work_dir(assets_dir)`  | 同步工作目录到资源目录          |
| `Utils.debug_memory_usage(logger)` | 输出当前内存使用情况            |

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

### 代码规范

- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 代码风格
- 类名使用大驼峰命名（如 `HTTPProxyServer`）
- 方法名使用蛇形命名（如 `handle_client`）
- 关键逻辑添加必要的注释说明
- 提交前确保在 Windows/Linux 下正常运行

### 提交 Pull Request

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

---

## 📄 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

- **无痕芳华** —— 项目开发者与维护者
- [Python](https://www.python.org/) —— 编程语言
- [PyInstaller](https://www.pyinstaller.org/) —— 应用打包工具
- [colorlog](https://github.com/borntyping/python-colorlog) —— 彩色日志库

---

## 📮 联系方式

如有问题或建议，请通过以下方式联系：

- 提交 [GitHub Issue](https://github.com/yangsongh/HttpProxyServer/issues)
- 邮件联系：18675864731@163.com

---

> **提示**：如需修改代理配置或白名单规则，请直接编辑 `assets/config_http.jsonc` 文件，无需修改源代码。如需深度定制，欢迎提交 Issue 讨论。
