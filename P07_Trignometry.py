import math

print("TABLE OF TRIGNONOMETRIC SIN")
print("==========================")

print("N               Sin")

for i in range(0, 50, 5):
    d = math.radians(i)
    print(i, "\t", math.sin(d))
