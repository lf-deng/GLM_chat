from openai import OpenAI
import config
import base64

# 创建全局 client 实例
client = OpenAI(
    api_key=config.ZHIPU_API_KEY,
    base_url=config.ZHIPU_BASE_URL,
)

# 模型常量
GLM4_FLASH = "glm-4-flash"
GLM4V_FLASH = "glm-4v-flash"

# 系统提示信息作为常量
SYSTEM_PROMPT = {
    "role": "system",
    "content": "",
}


def glm4_chat(message, history):
    """GLM-4-Flash 对话函数"""
    messages = [SYSTEM_PROMPT]
    for human, assistant in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": assistant})
    messages.append({"role": "user", "content": message})

    completion = client.chat.completions.create(
        model=GLM4_FLASH,
        messages=messages,
        temperature=0.3,
        stream=True,
    )

    history = history + [(message, "")]
    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            response += chunk.choices[0].delta.content
            history[-1] = (message, response)
            yield history


def encode_image_to_base64(image_path):
    """将图片转换为base64编码"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def glm4v_chat(message, image_path, history):
    """GLM-4V 对话函数，支持图片输入"""
    # 如果有图片，将其转换为base64并构建消息
    if image_path:
        base64_image = encode_image_to_base64(image_path)
        content = [
            {"type": "text", "text": message},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
            },
        ]
        # 在对话历史中显示图片
        display_message = f"<img src='data:image/jpeg;base64,{base64_image}' width='400'><br>{message}"
    else:
        content = [{"type": "text", "text": message}]
        display_message = message

    # 创建对话
    completion = client.chat.completions.create(
        model=GLM4V_FLASH,
        messages=[SYSTEM_PROMPT, {"role": "user", "content": content}],
        temperature=0.3,
        stream=True,
    )

    # 处理响应
    history = history + [(display_message, "")]  # 使用包含图片的消息
    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            response += chunk.choices[0].delta.content
            history[-1] = (display_message, response)  # 使用包含图片的消息
            yield history
