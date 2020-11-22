# -*- coding: utf-8 -*-
import time
from multiprocessing import Pool
import numpy as np
import random
from milvus import Milvus, IndexType, MetricType


def create_data(host, port, num_vec, vec_dim):
    """ 创建一些表格和索引用来做多进程测试 """
    milvus = Milvus()
    milvus.connect(host=host, port=port)
    # 创建2个表
    table_param = {'table_name': 'table1', 'dimension': vec_dim, 'index_file_size': 1024, 'metric_type': MetricType.IP}
    milvus.create_table(table_param)
    table_param = {'table_name': 'table2', 'dimension': vec_dim, 'index_file_size': 1024, 'metric_type': MetricType.L2}
    milvus.create_table(table_param)
    # 随机生成一批向量数据
    vectors_array = np.random.rand(num_vec, vec_dim)
    vectors_list = vectors_array.tolist()
    # 创建索引
    index_param = {'index_type': IndexType.FLAT, 'nlist': 128}
    milvus.create_index('table1', index_param)
    milvus.create_index('table2', index_param)

    # 添加数据
    milvus.add_vectors(table_name="table1", records=vectors_list, ids=None)
    milvus.add_vectors(table_name="table2", records=vectors_list, ids=None)

    # 创建索引
    milvus.create_index('table1', index_param)
    milvus.create_index('table2', index_param)
    print(milvus.show_tables())
    # 断开连接
    milvus.disconnect()


def clear_table(host, port):
    """ 清空表格和索引 """
    milvus = Milvus()
    milvus.connect(host=host, port=port)
    for table_name in milvus.show_tables()[1]:
        milvus.drop_index(table_name=table_name)
        milvus.delete_table(table_name=table_name)
    milvus.disconnect()


def milvus_search(host, port, table_name, query_vec, search_time=10):
    """ 测试查询, 返回查询的秒数"""
    milvus = Milvus()
    milvus.connect(host=host, port=port)
    # 因为bug的原因，要先搜索一次
    milvus.search(table_name, 4, 8, query_vec)
    # 开始测试
    for _ in range(search_time):
        query_vec[0][0] = random.random()  # 稍微随机化一下
        milvus.search(table_name, 4, 8, query_vec)


if __name__ == "__main__":
    host = "10.10.10.12"
    port = "19530"
    num_vec = 100000
    vec_dim = 768
    num_proc = 3  # 进程数
    search_time = 2000  # 搜索次数
    ####### Step1 先创建用于测试的数据 运行一次就行了
    create_data(host=host, port=port, num_vec=num_vec, vec_dim=vec_dim)
    clear_table(host, port)
    exit(0)

    ####### Step2 测试依次执行的时间
    start_time = time.time()
    for _ in range(num_proc):
        query_vec = np.random.rand(1, vec_dim).tolist()
        milvus_search(host, port, "table1", query_vec, search_time)
    end_time = time.time()
    print("顺序执行milvus_search的时间总和是：", end_time - start_time)

    ####### Step3 测试多进程时间
    pool = Pool(num_proc)
    start_time = time.time()
    for _ in range(num_proc):
        query_vec = np.random.rand(1, vec_dim).tolist()
        pool.apply_async(milvus_search, args=(host, port, "table1", query_vec, search_time))
    pool.close()
    pool.join()
    end_time = time.time()
    print("并行执行milvus_search的时间总和是：", end_time - start_time)
