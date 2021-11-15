'''
JSON 형식 다루기
'''
import json

# dictionary 생성
# 방법 01.
a = dict()
# 방법 02.
b = {}

# list 생성
# 방법 01.
c = list()
# 방법 02.
d = []

'''
{
    "email" : "abc@google.com",
    "body" : {
        "userName" : "aaa",
        "age" : 33,
        "favorites" : ["apple", "orange", "grape"]
    }
}
'''
res = dict()
res['email'] = 'abc@google.com'
res['body'] = dict()
res['body']['userName'] = 'aaa'
res['body']['age'] = 33
res['body']['favorites'] = list()
res['body']['favorites'].append("apple")
res['body']['favorites'].append("orange")
res['body']['favorites'].append("grape")

print(res)

ret = json.dumps(res)
print(ret)