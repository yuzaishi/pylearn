import json


d = {}
d['size'] = 66
d['content'] = 'hello'
d['para'] = {}
d['para']['p1']=5
d['para']['p2']=6
d['para']['p3']=[1,2,3]


dst_json_format = json.loads(json.dumps(d))


with open('dst.json', 'w') as fw:
    json.dump(dst_json_format, fw)