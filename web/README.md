# Web UI

基于 [blind_watermark](https://github.com/guofei9987/blind_watermark) 的本地图形界面，支持在浏览器中嵌入和提取文字盲水印。

## 启动

```bash
# 在项目根目录
./web/start.sh
```

或手动启动：

```bash
source .venv/bin/activate
pip install -r web/requirements.txt
python web/app.py
```

默认访问地址：**http://127.0.0.1:5005**

## 使用说明

1. **嵌入水印**：上传原图，输入水印文字与数字密码，下载含水印图片，并自行记录返回的 `wm_size`。
2. **提取水印**：上传含水印图片，填写嵌入时保存的 `wm_size` 与相同密码。

> 水印长度无法从图片中自动识别，提取时必须与嵌入时一致。
