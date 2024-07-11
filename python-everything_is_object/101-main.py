#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    print(lc.__dict__)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    lc.age = 30
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    lc.test = "test"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
