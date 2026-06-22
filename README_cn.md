# blind-watermark · Web UI

本仓库 Fork 自 [guofei9987/blind_watermark](https://github.com/guofei9987/blind_watermark)，在原有盲水印库基础上**新增了本地 Web 图形界面**，可在浏览器中完成文字水印的嵌入与提取，无需手写命令行。

![Python](https://img.shields.io/badge/python->=3.5-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20|%20linux%20|%20macos-green.svg)
[![License](https://img.shields.io/pypi/l/blind_watermark.svg)](https://github.com/guofei9987/blind_watermark/blob/master/LICENSE)

## 本 Fork 新增内容

- **Web 图形界面**（`web/`）：上传图片、输入水印文字与密码，一键嵌入或提取
- **Flask 本地服务**：默认运行在 `http://127.0.0.1:5005`
- **启动脚本**：`./web/start.sh` 一键启动

## 快速开始

### 1. 安装依赖

```bash
git clone https://github.com/onecaicai/blind_watermark.git
cd blind_watermark

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pip install --no-build-isolation -e .
pip install -r web/requirements.txt
```

### 2. 启动 Web 界面

```bash
./web/start.sh
```

浏览器打开：**http://127.0.0.1:5005**

### 3. 使用流程

**嵌入水印**

1. 上传原图
2. 输入水印文字与数字密码
3. 下载含水印图片，并**自行记录**返回的 `wm_size`

**提取水印**

1. 上传含水印图片
2. 填写嵌入时保存的 `wm_size` 与相同密码
3. 查看提取出的文字

> 水印长度无法从图片自动识别，提取时必须与嵌入时一致。

## 项目结构

```
web/
├── app.py              # Flask 后端
├── start.sh            # 启动脚本
├── templates/          # 页面模板
└── static/             # 样式与脚本
```

更多 Web 界面说明见 [web/README.md](web/README.md)。

## 原项目

核心算法与 CLI / Python API 均来自上游项目：

- **上游仓库**：[guofei9987/blind_watermark](https://github.com/guofei9987/blind_watermark)
- **官方文档**：[中文](https://BlindWatermark.github.io/blind_watermark/#/zh/) · [English](https://BlindWatermark.github.io/blind_watermark/#/en/)
- **PyPI 安装**：`pip install blind-watermark`

命令行示例：

```bash
blind_watermark --embed --pwd 1234 examples/pic/ori_img.jpeg "watermark text" examples/output/embedded.png
blind_watermark --extract --pwd 1234 --wm_shape 111 examples/output/embedded.png
```

## License

MIT · 遵循原项目 [LICENSE](LICENSE)
