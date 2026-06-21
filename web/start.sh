#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ ! -d .venv ]]; then
  echo "未找到 .venv，请先在项目根目录创建虚拟环境并安装 blind_watermark。"
  exit 1
fi

source .venv/bin/activate
pip install -q -r web/requirements.txt
python web/app.py
