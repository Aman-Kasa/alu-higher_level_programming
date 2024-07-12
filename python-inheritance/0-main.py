#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

class MyClass3(object):
    def dir(self):
        return ["my_class", "is", "empty"]

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
print(lookup(float))
print(lookup(object))
print(lookup(list))
print(lookup(MyClass3))
print(lookup(type('MyClass4', (), {"one_attribute": 89})))
print(lookup(type('MyClass5', (), {"one_meth": lambda self: None})))
