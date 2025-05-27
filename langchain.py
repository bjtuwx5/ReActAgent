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

'''
三、LangChain样例
'''
# 导入dotenv包，用于加载环境变量
from dotenv import load_dotenv
load_dotenv()
# 导入langchain openai库中的OpenAI类
from langchain_community.llms import Cohere, HuggingFaceHub
# 初始化大模型的实例，并设置temperature参数（控制生成文本的创新性）
OpenAI = OpenAI(temperature=0.1)
cohere = Cohere(model="command", temperature=0.1)
huggingface = HuggingFaceHub(repo_id="tiiuae/falcon-7b", model_kwargs={'temperature':0.1})
# 导入ModelLaboratory类，用于创建和管理多个大模型
from langchain.model_laboratory import ModelLaboratory
# 创建一个模型实验室实例，整合OpenAI、Cohere和Hubging Face的模型
model_lab = ModelLaboratory.from_llms([OpenAI, cohere, huggingface])
# 使用模型实验室比较不同模型对同一个问题的回答
model_lab.compare("百合花源自哪个国家？")

'''
四、LCEL样例
'''
# 导入所需的库，用于将输出结果解析为字符串
from langchain_core.output_parsers import StrOutputParser
# 用于创建聊天提示模板
from langchain_core.prompts import ChatPromptTemplate
# 用于调佣OpenAI公司的GPT模型
from langchain_openai import ChatOpenAI
# 创建一个聊天提示词模板，其中{topic}是占位符，用于后续插入具体的话题
prompt = ChatPromptTemplate.from_template("请讲一个关于{topic}的故事")
# 初始化ChatOpenAI对象，指定使用的模型为gpt-4
model = ChatOpenAI(model="gpt-4")
# 初始化一个输出解析器，用于将模型的输出解析成字符串
output_parser = StrOutputParser()
'''
通过管道操作符（|）连接各个处理步骤，以创建一个处理链
其中，prompt用于生成具体的提示文本，model用于根据提示文本生成回应，output_parser用于处理回应并将其转换为字符串
'''
chain = prompt | model | output_parser
# 调用处理链，传入话题“水仙花”，执行生成故事的操作
message = chain.invoke({"topic":"水仙花"})
# 打印链的输出结果
print(message)

'''
五、LangSmith样例
'''
# 设置环境变量，导入一系列密钥及配置
from dotenv import load_dotenv
load_dotenv()
# 设置提示模板
from langchain.prompts import PromptTemplate
prompt = PromptTemplate.from_template("{flower}的花语是？")
# 设置大模型
from langchain_openai import OpenAI
model = OpenAI()
# 设置输出解析器
from langchain.schema.output_parser import StrOutputParser
output_parser = StrOutputParser()
# 执行链并打印执行结果
result = chain.invoke({"flower":"丁香"})
print(result)