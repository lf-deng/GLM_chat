import gradio as gr
from chat import glm4v_chat


def create_tab():
    """创建 GLM-4V-Flash 选项卡"""
    with gr.TabItem("GLM-4V-Flash"):
        with gr.Column():
            chatbot = gr.Chatbot(
                height=500,
                show_copy_button=True,
                bubble_full_width=True,
                container=True,
            )
            with gr.Row(equal_height=True, elem_classes="input-row"):
                image = gr.Image(
                    label="",
                    type="filepath",
                    height=60,
                    width=60,
                    scale=1,
                    min_width=60,
                    container=False,
                    sources=["upload"],
                    elem_classes="image-upload",
                )
                msg = gr.Textbox(
                    placeholder="在这里输入您的问题...",
                    label="输入",
                    lines=2,
                    scale=8,
                    container=False,
                )
                with gr.Column(scale=1, min_width=100):
                    send = gr.Button("发送")
                    clear = gr.ClearButton(
                        components=[msg, chatbot, image],
                        value="清除",
                    )

        send.click(
            glm4v_chat,
            [msg, image, chatbot],
            [chatbot],
            queue=True,
        )
        send.click(lambda: "", None, msg)
        send.click(lambda: None, None, image)

        msg.submit(
            glm4v_chat,
            [msg, image, chatbot],
            [chatbot],
            queue=True,
        )
        msg.submit(lambda: "", None, msg)
        msg.submit(lambda: None, None, image)
