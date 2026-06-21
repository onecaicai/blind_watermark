function setupTabs() {
  const tabs = document.querySelectorAll(".tab");
  const panels = {
    embed: document.getElementById("panel-embed"),
    extract: document.getElementById("panel-extract"),
  };

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      tabs.forEach((item) => {
        const active = item === tab;
        item.classList.toggle("active", active);
        item.setAttribute("aria-selected", active ? "true" : "false");
      });

      Object.entries(panels).forEach(([name, panel]) => {
        const active = tab.dataset.tab === name;
        panel.classList.toggle("active", active);
        panel.hidden = !active;
      });
    });
  });
}

function setupPreview(inputName, previewId) {
  const input = document.querySelector(`#form-${inputName} input[type="file"]`);
  const preview = document.getElementById(previewId);

  input.addEventListener("change", () => {
    preview.innerHTML = "";
    const file = input.files?.[0];
    if (!file) return;
    const img = document.createElement("img");
    img.alt = "预览";
    img.src = URL.createObjectURL(file);
    preview.appendChild(img);
  });
}

function showResult(element, ok, html) {
  element.classList.remove("hidden", "success", "error");
  element.classList.add(ok ? "success" : "error");
  element.innerHTML = html;
}

async function submitForm(form, endpoint, resultEl, onSuccess) {
  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const button = form.querySelector("button[type='submit']");
    button.disabled = true;
    showResult(resultEl, true, "处理中，请稍候…");

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        body: new FormData(form),
      });
      const data = await response.json();
      if (!response.ok || !data.ok) {
        throw new Error(data.message || "请求失败");
      }
      onSuccess(data, resultEl);
    } catch (error) {
      showResult(resultEl, false, error.message || "发生未知错误");
    } finally {
      button.disabled = false;
    }
  });
}

setupTabs();
setupPreview("embed", "preview-embed");
setupPreview("extract", "preview-extract");

submitForm(
  document.getElementById("form-embed"),
  "/api/embed",
  document.getElementById("result-embed"),
  (data, resultEl) => {
    showResult(
      resultEl,
      true,
      `嵌入成功。请自行记录水印长度 <code>${data.wm_size}</code>，提取时需填写相同数值。<br>` +
        `<a href="${data.download_url}" download>下载含水印图片</a>`
    );
  }
);

submitForm(
  document.getElementById("form-extract"),
  "/api/extract",
  document.getElementById("result-extract"),
  (data, resultEl) => {
    showResult(resultEl, true, `提取结果：<code>${escapeHtml(data.watermark)}</code>`);
  }
);

function escapeHtml(text) {
  return String(text)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}
