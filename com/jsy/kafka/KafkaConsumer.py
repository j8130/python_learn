from kafka import KafkaConsumer
import json

'''
    消费者demo
    消费test_lyl2主题中的数据
    注意事项：如需以json格式读取数据需加上value_deserializer参数
    
    consumer = KafkaConsumer('test_lyl2',group_id="lyl-gid1",
                         bootstrap_servers=['192.168.12.101:6667','192.168.12.102:6667','192.168.12.103:6667'],
                         auto_offset_reset='earliest',value_deserializer=json.loads
                         )
'''

consumer = KafkaConsumer('pyTest', group_id="g1",
                         bootstrap_servers=['192.168.124.102:9092'],
                         auto_offset_reset='earliest'
                         )
for message in consumer:
    print(message.value)
