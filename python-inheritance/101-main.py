#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)  # Should print: John

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)  # Should raise TypeError
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))  # Should print: [TypeError] can't add new attribute
