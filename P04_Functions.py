import math

print("Surface area and volume of a cylinder")

def Calc(r, h):
    area = 2 * math.pi * r * h
    volume = math.pi * r * r * h
    return(area, volume)

radius = float(input("Enter radius: "))
height = float(input("Enter height: "))

area, vol = Calc(radius, height)
print("Surface area = ",area," Volume= ", vol)