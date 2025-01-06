from ui import create_demo

if __name__ == "__main__":
    demo = create_demo()
    demo.queue()
    demo.launch(
        server_name="0.0.0.0",
        share=False,
        inbrowser=True,
    )
