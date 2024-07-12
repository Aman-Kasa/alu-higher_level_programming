#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

# Case: print(dir(Rectangle))
print(dir(Rectangle))

# Case: r = Rectangle(1, 4) print(r.area())
r = Rectangle(1, 4)
print(r.area())

# Case: r = Rectangle(1411, 781) print(r.area())
r = Rectangle(1411, 781)
print(r.area())

# Case: r = Rectangle(5, 5) print(r.area())
r = Rectangle(5, 5)
print(r.area())

# Case: r = Rectangle(1411, 781) print(r)
r = Rectangle(1411, 781)
print(r)

# Case: r = Rectangle(1, 4) print(r)
r = Rectangle(1, 4)
print(r)

# Case: r = Rectangle(5, 5) print(r)
r = Rectangle(5, 5)
print(r)

# Case: r = Rectangle() r = Rectangle(1) r = Rectangle(1, [12, 52]) r = Rectangle(4, 5) r = Rectangle(4, 5)
r = Rectangle()
print(r)
r = Rectangle(1)
print(r)
try:
    r = Rectangle(1, [12, 52])
    print(r)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
r = Rectangle(4, 5)
print(r)
r = Rectangle(4, 5)
print(r)
