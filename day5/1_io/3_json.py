import json
 
# json模块主要有四个比较重要的函数，分别是：
# dump - 将Python对象按照JSON格式序列化到文件中
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象
# loads - 将字符串的内容反序列化成Python对象

# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'https://www.runoob.com'
}
 
json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)
print("================================================")
 
# JSON编码的字符串转换回一个Python数据结构：
data1 = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
 
json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)
 
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])

print("================================================")
# with open('test.json', 'w') as f:
#     json.dump(data, f)
 
# 读取数据
with open('test.json', 'r') as f:
    data3 = json.load(f)

print(data3)
print(data3['age'])
print(data3['qq'])
print(data3['name'])