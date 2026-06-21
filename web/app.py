#!/usr/bin/env python3
"""Local web UI for blind_watermark embed / extract."""

import uuid
from pathlib import Path

from flask import Flask, jsonify, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

from blind_watermark import WaterMark
from blind_watermark.version import bw_notes

APP_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = APP_DIR / "uploads"
OUTPUT_DIR = APP_DIR / "output"

UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

bw_notes.close()

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024 * 1024


def _parse_password(raw: str) -> int:
    value = (raw or "").strip()
    if not value:
        raise ValueError("请输入密码")
    if not value.isdigit():
        raise ValueError("密码必须是数字")
    return int(value)


def _save_upload(field_name: str) -> Path:
    file = request.files.get(field_name)
    if file is None or file.filename == "":
        raise ValueError("请先上传图片")
    suffix = Path(secure_filename(file.filename)).suffix.lower() or ".png"
    if suffix not in {".jpg", ".jpeg", ".png", ".bmp", ".webp"}:
        raise ValueError("仅支持 jpg / png / bmp / webp 图片")
    path = UPLOAD_DIR / f"{uuid.uuid4().hex}{suffix}"
    file.save(path)
    return path


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/embed", methods=["POST"])
def embed():
    try:
        password = _parse_password(request.form.get("password"))
        watermark = (request.form.get("watermark") or "").strip()
        if not watermark:
            raise ValueError("请输入水印文字")

        input_path = _save_upload("image")
        output_name = f"embedded_{uuid.uuid4().hex}.png"
        output_path = OUTPUT_DIR / output_name

        bwm = WaterMark(password_img=password, password_wm=password)
        bwm.read_img(str(input_path))
        bwm.read_wm(watermark, mode="str")
        bwm.embed(str(output_path))

        input_path.unlink(missing_ok=True)
        return jsonify(
            {
                "ok": True,
                "wm_size": len(bwm.wm_bit),
                "download_url": f"/files/{output_name}",
                "message": "水印嵌入成功",
            }
        )
    except Exception as exc:
        return jsonify({"ok": False, "message": str(exc)}), 400


@app.route("/api/extract", methods=["POST"])
def extract():
    try:
        password = _parse_password(request.form.get("password"))
        wm_shape_raw = (request.form.get("wm_size") or "").strip()
        if not wm_shape_raw.isdigit():
            raise ValueError("请输入有效的水印长度（嵌入时返回的数字）")
        wm_shape = int(wm_shape_raw)

        input_path = _save_upload("image")

        bwm = WaterMark(password_img=password, password_wm=password)
        text = bwm.extract(filename=str(input_path), wm_shape=wm_shape, mode="str")

        input_path.unlink(missing_ok=True)
        return jsonify({"ok": True, "watermark": text, "message": "水印提取成功"})
    except Exception as exc:
        return jsonify({"ok": False, "message": str(exc)}), 400


@app.route("/files/<path:filename>")
def files(filename):
    return send_from_directory(OUTPUT_DIR, filename)


if __name__ == "__main__":
    print("Blind Watermark UI: http://127.0.0.1:5005")
    app.run(host="127.0.0.1", port=5005, debug=False)
