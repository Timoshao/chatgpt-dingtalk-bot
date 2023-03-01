# Chatgpt Dingtalk Bot


[![License](https://img.shields.io/github/license/anyidea/chatgpt-dingtalk-bot)](https://github.com/anyidea/chatgpt-dingtalk-bot/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python->=3.8-blue)](https://www.python.org/)
[![Build Status](https://github.com/anyidea/chatgpt-dingtalk-bot/actions/workflows/ci.yml/badge.svg)](https://github.com/anyidea/chatgpt-dingtalk-bot/actions/workflows/ci.yml)
[![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/aidenlu/chatgpt-dingtalk-bot)](https://hub.docker.com/r/aidenlu/chatgpt-dingtalk-bot)
[![Docker Pulls](https://img.shields.io/docker/pulls/aidenlu/chatgpt-dingtalk-bot)](https://hub.docker.com/r/aidenlu/chatgpt-dingtalk-bot)
[![Built with Cookiecutter](https://img.shields.io/badge/built%20with-Cookiecutter-ff69b4.svg?logo=cookiecutter)](https://github.com/wccdev/cookiecutter-pypackage/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> 🚀 浏览器版ChatGPT集成钉钉机器人, 支持单聊和群聊, 特别感谢 [ChatGPT](https://github.com/acheong08/ChatGPT)项目


* Documentation: <https://anyidea.github.io/chatgpt-dingtalk-bot>
* GitHub: <https://github.com/anyidea/chatgpt-dingtalk-bot>
* Free software: MIT


## Features

* 浏览器版本ChatGPT(非api版本)
* 使用Fastapi框架，支持异步
* 支持机器人群聊和单聊模式(暂只支持账号登录模式)
* 支持Docker一键部署
* 支持配置多个账号，通过连接池来避免单账号的限制


## Quick start

### 拉取Git仓库代码运行
> 运行该项目需要Python3.8以上的环境，请先确保环境已经满足要求
1. 请先安装Python包管理工具[Poetry](https://python-poetry.org/docs/#installation)
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
2. 进入项目根目录, 安装项目依赖环境
```bash
poetry install --only main --no-root
```
3. 通过uvicorn启动fastapi应用
```bash
poetry run uvicorn chatbot.main:app --host 0.0.0.0 --port 8090 --proxy-headers
```

### Docker 运行

- 通过`.env`文件来批量设置环境变量
```bash
docker run -d --name=chatgpt-dingtalk-bot --restart=unless-stopped -p 8090:8090 \
--env-file .env \
aidenlu/chatgpt-dingtalk-bot
```
>
>
> 复制`.env.dist`文件，并改名为`.env`，填写账号密码GPT_ACCOUNTS或者GPT_ACCESS_TOKENS，二选一即可，支持多个账号和token

- 或者通过`-e`参数来设置环境变量
```bash
docker run -d --name=chatgpt-dingtalk-bot --restart unless-stopped -p 8090:8090 \
-e GPT_ACCOUNTS=<email>:<password> \
-e GPT_PROXY=http://<proxy-ip>:<port> \
-e GPT_PAID=false \
aidenlu/chatgpt-dingtalk-bot
```
> 💡 ChatGPT Plus用户可设置`GPT_PAID=true`

### 配置钉钉机器人
1. 在钉钉管理后台添加企业内部机器人(需要有开发者后台权限)
> ⚠️ 机器人不要命名为chatgpt之类的，会被钉钉屏蔽
---
<img src="https://raw.githubusercontent.com/anyidea/chatgpt-dingtalk-bot/main/.github/assets/20230228005625.jpg" width="100%" height="80%">

2. 配置消息接收地址: `http://<ip-address>:8090/chat`和出口IP白名单(部署`chatgpt-dingtalk-bot`服务器的出口IP)
---

<img src="https://raw.githubusercontent.com/anyidea/chatgpt-dingtalk-bot/main/.github/assets/20230228005746.jpg" width="100%" height="80%">

3. 点击上线机器人
---

<img src="https://raw.githubusercontent.com/anyidea/chatgpt-dingtalk-bot/main/.github/assets/20230228005824.jpg" width="100%" height="80%">

<img src="https://raw.githubusercontent.com/anyidea/chatgpt-dingtalk-bot/main/.github/assets/20230228010827.jpg" width="100%" height="80%">

> **Note**
>
> 钉钉虽然支持Markdown格式消息，但支持不完整，建议使用text文本消息


## Credits

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [wccdev/cookiecutter-pypackage](https://github.com/wccdev/cookiecutter-pypackage) project template.
