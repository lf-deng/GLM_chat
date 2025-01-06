import gradio as gr
from utils import get_local_ip
from tabs import glm4_flash, glm4v_flash, cogview3_flash, cogvideox_flash


def create_demo():
    """创建 Gradio 界面"""
    local_ip = get_local_ip()

    with gr.Blocks(
        title="Chat with GLM",
        css="""
            footer {display: none !important}
            .contain { display: flex; flex-direction: column; }
            .chatbot { flex-grow: 1; overflow-y: auto; }
            .container { max-width: 1200px; margin: auto; }
            .message { max-width: 95%; }
            .message-wrap { padding: 0 10px; }
            .message.user { background-color: #f3f3f3; border-radius: 10px; }
            .message.assistant { background-color: #e6f3ff; border-radius: 10px; }
            .input-row { position: sticky; bottom: 0; background: white; padding: 10px 0; }
            /* 图片上传按钮样式 */
            .image-upload {
                border: 1px solid #ccc !important;
                border-radius: 8px !important;
                background-color: white !important;
                padding: 8px !important;
                margin: 0 8px !important;
                height: 60px !important;
                width: 60px !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                cursor: pointer !important;
            }
            .image-upload:hover {
                border-color: #2196f3 !important;
                background-color: #f5f5f5 !important;
            }
        """,
    ) as demo:
        gr.Markdown(
            f"""
        # Chat with GLM
        欢迎使用 GLM 聊天界面！
        
        ## 访问方式
        - 本机访问：http://127.0.0.1:7860
        - 局域网访问：http://{local_ip}:7860
        """
        )

        with gr.Tabs():
            glm4_flash.create_tab()
            glm4v_flash.create_tab()
            cogview3_flash.create_tab()
            cogvideox_flash.create_tab()

    return demo
