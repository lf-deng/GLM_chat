import gradio as gr
from chat import glm4_chat  # 暂时使用 glm4_chat，后续需要替换为 cogview3_chat


def create_tab():
    """创建 CogView-3-Flash 选项卡"""
    with gr.TabItem("CogView-3-Flash"):
        with gr.Column():
            chatbot = gr.Chatbot(
                height=500,
                show_copy_button=True,
                bubble_full_width=True,
                container=True,
            )
            with gr.Row(equal_height=True, elem_classes="input-row"):
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
                        components=[msg, chatbot],
                        value="清除",
                    )

        send.click(
            glm4_chat,
            [msg, chatbot],
            [chatbot],
            queue=True,
        )
        send.click(lambda: "", None, msg)
        msg.submit(
            glm4_chat,
            [msg, chatbot],
            [chatbot],
            queue=True,
        )
        msg.submit(lambda: "", None, msg)
