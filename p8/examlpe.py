from collections import namedtuple

a = {"year": "2011", "make": "Audi"}

# for i in a:
#     print(a[i], i)

Point = namedtuple("Point", ["x", "y"])
pt1 = Point(50,60)
pt2 = Point(x=90, y=10)