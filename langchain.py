'''
一、OpenAI API聊天程序样例
'''
# 设置OpenAI API密钥
import os
# 导入OpenAI库
from openai import OpenAI

os.environ["OpenAI_API_KEY"] = '你的OpenAI API密钥'

# 创建client
client = OpenAI()

# 调用chat.completions.create方法，得到响应
response = client.chat.completions.create(
    model="gpt_4-turbo-preview",
    response_format={ "type": "json_object"},
    messages=[
        {"role": "system", "content": "您是一个帮助用户了解鲜花信息的智能助手，并能够输出JSON格式的内容。"},
        {"role": "user", "content": "生日怂什么花最好？"},
        {"role": "assistant", "content": "玫瑰花是生日礼物的热门选择。"},
        {"role": "user", "content": "送货需要多长时间？"}
    ]
)

print(response)
print(response.choices[0].message.content)


'''
二、OpenAI API图片生成样例
'''
# 导入OpenAI库
from openai import OpenAI
# 加载环境变量
from dotenv import load_dotenv
load_dotenv()
# 初始化client
client = OpenAI()
# 请求DALL.E 3生成图片
response = client.images.generate(
    model = "dall-e-3",
    prompt =  "电商花语秘境的新春玫瑰花宣传海报，配上文案",
    size = "1024x1024",
    quality = "standard",
    n = 1,
)

# 获取图片URL
image_url = response.data[0].url
# 读取图片
import requests
image = requests.get(image_url).content
# 在Jupyter Notebook中显示图片
from IPython.display import Image
Image(image)