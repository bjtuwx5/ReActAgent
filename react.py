import os
# 导入langchain Hub
from langchain import hub
# 导入OpenAI
from langchain import OpenAI
# 导入SerpAPIWrapper即工具包
from langchain_community.utilities import SerpAPIWrapper
from langchain.tools import Tool
# 导入create_react_agent功能
from langchain.agents import create_react_agent
# 导入AgentExecutor
from langchain.agents import AgentExecutor

# 设置OpenAI网站和SerpApi网站提供的API密钥
os.environ["OpenAI_API_KEY"] = '你的OpenAI API 密钥'
os.environ["SERPAPI_API_KEY"] = '你的SerpAPI API 密钥'

# 从Hub中获取ReAct的提示
prompt = hub.pull("hwchase17/react")
print(prompt)

# 选择要使用的大模型
llm = OpenAI()

# 实例化SerpAPIWrapper
search = SerpAPIWrapper()

# 准备工具列表
tools = {
    Tool(
        name = "Seaarch",
        func = search.run,
        description = "当大模型没有相关知识时，用于搜索知识"
    ),
}

# 构建React Agent
agent = create_react_agent(llm, tools, prompt)

# 创建Agent Executor并传入Agent和工具
agent_executor = AgentExecutor(agent = agent, tools = tools, verbose = True)
# 调用Agent Executor，传输输入数据
print("第一次调用结果")
agent_executor.invoke({"input": "当前Agent最新研究进展是什么"})
print("第二次调用结果")
agent_executor.invoke({"input": "当前Agent最新研究进展是什么"})



