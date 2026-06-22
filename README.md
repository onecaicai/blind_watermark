# blind-watermark · Web UI

This repository is a fork of [guofei9987/blind_watermark](https://github.com/guofei9987/blind_watermark). It adds a **local Web UI** on top of the original blind watermark library, so you can embed and extract text watermarks in the browser without using the CLI.

![Python](https://img.shields.io/badge/python->=3.5-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20|%20linux%20|%20macos-green.svg)
[![License](https://img.shields.io/pypi/l/blind_watermark.svg)](https://github.com/guofei9987/blind_watermark/blob/master/LICENSE)

**中文说明** · [README_cn.md](README_cn.md)

## What's New in This Fork

- **Web UI** (`web/`): upload images, enter watermark text and password, embed or extract in one place
- **Flask local server**: runs at `http://127.0.0.1:5005` by default
- **Start script**: `./web/start.sh`

## Quick Start

### 1. Install

```bash
git clone https://github.com/onecaicai/blind_watermark.git
cd blind_watermark

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pip install --no-build-isolation -e .
pip install -r web/requirements.txt
```

### 2. Start the Web UI

```bash
./web/start.sh
```

Open in browser: **http://127.0.0.1:5005**

### 3. Usage

**Embed**

1. Upload the original image
2. Enter watermark text and a numeric password
3. Download the watermarked image and **save** the returned `wm_size`

**Extract**

1. Upload the watermarked image
2. Enter the saved `wm_size` and the same password
3. View the extracted text

> Watermark length cannot be detected from the image automatically. It must match the value used during embedding.

## Project Layout

```
web/
├── app.py              # Flask backend
├── start.sh            # start script
├── templates/          # HTML templates
└── static/             # CSS & JS
```

See [web/README.md](web/README.md) for more details.

## Upstream Project

The core library and CLI come from the original repository:

- **Upstream**：[guofei9987/blind_watermark](https://github.com/guofei9987/blind_watermark)
- **Docs**：[English](https://BlindWatermark.github.io/blind_watermark/#/en/) · [中文](https://BlindWatermark.github.io/blind_watermark/#/zh/)
- **PyPI**：`pip install blind-watermark`

CLI example:

```bash
blind_watermark --embed --pwd 1234 examples/pic/ori_img.jpeg "watermark text" examples/output/embedded.png
blind_watermark --extract --pwd 1234 --wm_shape 111 examples/output/embedded.png
```

## License

MIT · see [LICENSE](LICENSE) from the upstream project
