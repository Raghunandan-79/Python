from collections import namedtuple

Point = namedtuple('Point', ['first', 'second'])
val1 = Point(7, 9)
print(val1.first)

NestedPoints = namedtuple('NestedPoints', ['first', 'second'])
val2 = NestedPoints(2, val1)
print(val2)
print(val2.second.second)