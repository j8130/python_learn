import random

import numpy as np
from milvus import Milvus, IndexType, MetricType

# 实例化，连接到milvus服务器
milvus = Milvus(host='10.10.10.12', port='19530')

# 参数：名称，维度尺寸，文件大小，距离方法
param = {'collection_name': 'test1', 'dimension': 768, 'index_file_size': 1024, 'metric_type': MetricType.L2}

# 创建集合
status = milvus.create_collection(param)
# 查看集合状态
print(status)
# 索引参数
ivf_param = {'NLIST': 4096}
# 为集合创建索引(索引类型有：FLAT/IVFLAT/IVF_SQ8/IVF/SQ8H，其中FLAT是精确索引，速度慢，但是有100%的召回率)
milvus.create_index('test1', IndexType.IVF_FLAT, ivf_param)
# 生成20个768维向量
dim = 768

vectors = [[random.random() for _ in range(dim)] for _ in range(20)]

# 插入向量列表。如果不指定向量id，Milvus会自动为向量生成id
milvus, inserted_vector_ids = milvus.insert(collection_name='test1', records=vectors)
# 插入向量ID
# vector_ids = [id for id in range(len(So_id))]
# milvus, insert ed_vector_ids = milvus.insert(collection_name='test1', records=vectors, ids=vector_ids)

# 将集合中的数据刷新到磁盘
milvus.flush(['test1'])
# 在集合中搜索向量
# 准备搜索参数
search_param = {'nprobe': 16}
# 搜索向量
# 生成5个768维的向量
q_records = [[random.random() for _ in range(dim)] for _ in range(5)]

# 用生成的向量，进行搜索
_, results = milvus.search(collection_name='test1', query_records=q_records, top_k=5, params=search_param)
# 打印结果
print(results)
# 关闭客户端
milvus.close()
