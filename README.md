# GLM Flash Chat

一个基于智谱 AI 系列大模型的对话应用。本项目利用智谱 AI 提供的免费 API 额度，结合 Gradio 框架，实现了一个轻量级的多模型对话界面。

## 项目说明

目前支持以下模型：

- GLM-4：支持纯文本对话
- GLM-4V：支持图像理解和多轮对话
- CogView-3-Flash：(开发中)
- CogViewX-Flash：(开发中)

特点：

- 使用 Gradio 构建 Web 界面，操作简单直观
- 支持图片上传和文本输入
- 完全免费，使用智谱 AI 提供的免费 API 额度

## 当前进度

- [x] GLM-4 文本对话功能
- [x] GLM-4V 图像对话功能
- [x] 多轮对话支持
- [x] Web 界面基本布局
- [ ] CogView-3-Flash 支持
- [ ] CogViewX-Flash 支持

## 使用方法

1. 克隆仓库并安装依赖
2. 在 config.py 中配置您的智谱 API 密钥（可在智谱 AI 官网免费申请）
3. 运行 `python app.py`
4. 访问 `http://localhost:7860` 开始使用

## 注意事项

- 需要智谱 AI 的 API 密钥（可免费申请）
- 支持常见图片格式（JPG、PNG、WEBP）
- 建议使用 Chrome、Firefox 等现代浏览器

## 致谢

- 感谢智谱 AI 提供免费 API 支持
- 感谢 Gradio 框架提供 UI 支持
