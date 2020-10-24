# -*- coding: utf-8 -*-
from kafka import KafkaProducer
import json


# 安装kafka支持库pip install kafka-python

'''
    生产者demo
    向pyTest主题中循环写入10条json数据
    注意事项：要写入json数据需加上value_serializer参数，如下代码
'''
producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    bootstrap_servers=['192.168.124.102:9092']
)
for i in range(2):
    data = {
        "name": "李四",
        "age": 23,
        "gender": "男",
        "id": i
    }
    producer.send('pyTest', data)
producer.close()
