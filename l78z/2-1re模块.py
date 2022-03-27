import re
# list=re.findall("\d+","我的电话号是18028706448，我老婆电话15948780714")
# print(list)
# it=re.finditer("\d+","我的电话号是18028706448，我老婆电话15948780714")
# for i in it:
# #     print(i.group())
# #search是找到一个结果就返回
# s=re.search("\d+","我的电话号是18028706448，我老婆电话15948780714")
# print(s.group())
# #match是从头开始匹配
# m=re.match("\d+","我的电话号是18028706448，我老婆电话15948780714")
# print(m.group())
#预加载正则表达式
# obj=re.compile(r"\d+")
# result=obj.findall("我的电话号是18028706448，我老婆电话15948780714")
# print(result)
data="""
    <div class='babala'><span id='1'>芭芭拉</span></div>
    <div class='qin'><span id='2'>琴</span></div>
    <div class='zhongli'><span id='3'>钟离</span></div>
    <div class='keli'><span id='4'>可莉</span></div>
"""
#(?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
obj=re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>",re.S)
it=obj.finditer(data)
for i in it:
    print(i.group("id"))
    print(i.group("name"))