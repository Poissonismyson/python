
from circle import *

c1 = Circle(4)
print(c1.GetRadius())

c2 = Circle(5)
print(c2.GetRadius())

c3 = c1 + c2
print(c3.GetRadius())

print(c3 > c1)

print(c3)
print(c1._Circle__radius)