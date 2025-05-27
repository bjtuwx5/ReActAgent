# 导入花语秘境的文档
from llama_index.core import SimpleDirectoryReader
documents = SimpleDirectoryReader("data").load_data()

# 为文档建立索引
from llama_index import VectorStoreIndex
index = VectorStoreIndex.from_documents(documents)

# 创建查询引擎
query_engine = index.as_query_engine()

# 两个查询示例
response = agent.query("花语秘境的员工有集中角色")
print("花语秘境的员工有几种角色？", response)
response = agent.query("花语秘境的Agent叫什么名字？")
print("花语秘境的Agent叫什么名字？", response)

# 把索引保存到本地
index.storage_context.persist()
