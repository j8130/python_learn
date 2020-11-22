# -*- coding: utf-8 -*-

# 导入相应的包
import numpy as np
from milvus import Milvus, IndexType, MetricType

# 初始化一个Milvus类，以后所有的操作都是通过milvus来的
milvus = Milvus(host='10.10.10.12', port='19530')


# 向量个数
num_vec = 5000
# 向量维度
vec_dim = 768

# 创建表
# 参数含义
# table_name: 表名
# dimension: 向量维度
# metric_type: 向量相似度度量标准, MetricType.IP是向量内积; MetricType.L2是欧式距离
table_param = {'table_name': 'mytable', 'dimension': vec_dim, 'index_file_size': 1024, 'metric_type': MetricType.IP}
milvus.create_table(table_param)

# 随机生成一批向量数据
vectors_array = np.random.rand(num_vec, vec_dim)
vectors_list = vectors_array.tolist()

# 官方建议在插入向量之前，建议先使用 milvus.create_index 以便系统自动增量创建索引
# 索引类型有：FLAT / IVFLAT / IVF_SQ8 / IVF_SQ8H，其中FLAT是精确索引，速度慢，但是有100%的召回率
index_param = {'index_type': IndexType.FLAT, 'nlist': 128}
milvus.create_index('mytable', index_param)

# 把向量添加到刚才建立的表格中
# ids可以为None，使用自动生成的id
status, ids = milvus.add_vectors(table_name="mytable", records=vectors_list, ids=None)  # 返回这一组向量的ID

# 官方建议 向量插入结束后，相同的索引需要手动再创建一次
milvus.create_index('mytable', index_param)

# 输出一些统计信息
status, tables = milvus.show_tables()
print("所有的表格：", tables)
print("表格的数据量(行):{}".format((milvus.count_table('mytable')[1])))
print("mytable表格是否存在:", milvus.has_table("mytable")[1])

# 加载表格到内存
milvus.preload_table('mytable')

# 创建查询向量
query_vec_array = np.random.rand(1, vec_dim)
query_vec_list = query_vec_array.tolist()
# 进行查询, 注意这里的参数nprobe和建立索引时的参数nlist 会因为索引类型不同而影响到查询性能和查询准确率
# 对于 FLAT类型索引，两个参数对结果和速度没有影响
status, results = milvus.search(table_name='mytable', query_records=query_vec_list, top_k=4, nprobe=16)
print(status)
print(results)

# 删除表格和索引, 不删除的话，下一次还可以继续使用
milvus.drop_index(table_name="mytable")
milvus.delete_table(table_name="mytable")

# 断开连接
milvus.close()
milvus.disconnect()
