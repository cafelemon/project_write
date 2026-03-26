# OpenClaw 3.13 从零部署（含飞书/微信对接）

> 目标：从空环境开始，快速部署 OpenClaw **3.13.x**，并完成飞书与微信接入。  
> 风格：少解释，优先可直接执行命令。

---

## 1) 环境准备

## 1.1 安装 Node.js（LTS 20+）

### Windows（推荐 winget）
```powershell
winget install OpenJS.NodeJS.LTS
node -v
npm -v
```

### macOS（Homebrew）
```bash
brew install node
node -v
npm -v
```

### Ubuntu/Debian（NodeSource）
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
node -v
npm -v
```

---

## 2) 安装固定版本 OpenClaw（3.13）

```bash
npm i -g openclaw@3.13
openclaw --version
```

> 预期输出：`3.13.x`

---

## 3) 启动与基础校验

```bash
openclaw status
openclaw gateway start
openclaw gateway status
openclaw status --all
```

如果需要重启：
```bash
openclaw gateway restart
```

---

## 4) 基础模型配置（先可用再优化）

按向导设置：
```bash
openclaw models add
```

常用检查：
```bash
openclaw models list
openclaw status --deep
```

---

## 5) 接入飞书（Feishu/Lark）

## 5.1 飞书开放平台准备
- 创建企业自建应用
- 获取 `App ID`、`App Secret`
- 开通机器人能力与事件订阅权限

## 5.2 OpenClaw 添加飞书通道
```bash
openclaw channels add
```
在交互里选择 **Feishu**，填 `App ID/App Secret`。

如需手动安装插件（仅在你当前版本未内置时）：
```bash
openclaw plugins install @openclaw/feishu
```

## 5.3 配对授权
先在飞书里给机器人发消息，然后执行：
```bash
openclaw pairing list feishu
openclaw pairing approve feishu <CODE>
```

## 5.4 验证
```bash
openclaw status --all
```
在飞书中发送测试消息，确认可收发。

---

## 6) 接入微信（OpenClaw-Weixin）

> 说明：微信接入依赖你已安装并可用的 `openclaw-weixin` 通道能力。

## 6.1 添加微信通道
```bash
openclaw channels add
```
在交互里选择 **Weixin/微信**，按提示完成登录或凭据配置。

如果环境里尚未安装微信通道插件，先安装再添加：
```bash
openclaw plugins install @openclaw/weixin
openclaw channels add
```

## 6.2 验证
```bash
openclaw status --all
```
微信侧发送测试消息，确认能路由到 OpenClaw 并返回。

---

## 7) 常见故障一键排查

```bash
openclaw status
openclaw status --deep
openclaw gateway status
openclaw gateway restart
```

查看通道与插件：
```bash
openclaw channels list
openclaw plugins list
```

---

## 8) 推荐固定流程（部署后）

1. 先确保 `openclaw --version` 为 `3.13.x`。  
2. `openclaw gateway start` 后先做 `status --deep`。  
3. 再接飞书、微信通道。  
4. 最后做双通道发消息验收（飞书一次、微信一次）。

---

## 附：最短执行清单（可直接复制）

```bash
# 1) 安装 OpenClaw 3.13
npm i -g openclaw@3.13
openclaw --version

# 2) 启动网关
openclaw gateway start
openclaw status --deep

# 3) 添加飞书与微信通道
openclaw channels add
openclaw channels add

# 4) 飞书配对（如需）
openclaw pairing list feishu
openclaw pairing approve feishu <CODE>

# 5) 全量检查
openclaw status --all
```
