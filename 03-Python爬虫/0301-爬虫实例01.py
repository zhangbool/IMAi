
#路径表达式
# nodename 选取次节点的所有节点
# /    从根节点选取
# //   从匹配的当前节点选择文档中的节点， 而不考虑它们的位置
# .    选取当前节点
# ..   选取当前节点的父节点
# @    选取属性


import json


'''
obj = {"name":"ivanl001","age":29, "num":"10120945"}

#对象转json串
jsonStr = json.dumps(obj)
print(type(jsonStr))
print(jsonStr)

#json串转对象
jsonObj = json.loads(jsonStr)
print(type(jsonObj))
print(jsonObj)
'''

from xml.parsers.expat import ParserCreate


#这个感觉和实现接口的方法有所类似
class DefaultSaxHandler:

    def start_element(self, name, attribute):
        self.name = name
        print('element: %s,  attribute: %s' % (name, str(attribute)))
        print("-------start------------")
        print("\n")

    def end_element(self, name):
        print('end element: %s' % name)
        print("----------end----------")
        print("\n")

    def char_data(self, text):
        if text.strip():
            print("%s's text is %s" % (self.name, text))
            print("----------char_data----------")
            print("\n")


handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data

with open("book.xml", "r") as f:
    parser.Parse(f.read())

















