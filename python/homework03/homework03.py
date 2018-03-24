#******homework03-1*****************************
from math import *
radius = float(input("请输入圆的半径r:"))
height = float(input("请输入圆柱的高h:"))
print("r = ", radius)
print("h = ", height)
print("圆周长:%.3f" %(2*pi*radius))
print("圆面积:%.3f" %(pi*radius**2))
print("圆球表面积:%.3f" %(4*pi*radius**2))
print("圆球体积:%.3f" %(4/3*pi*radius**3))
print("圆柱体积:%.3f" %(pi*radius**2*height))
print()
#******homework03-2*****************************
F = float(input("请输入华氏温度F:"))
print("F = ", F)
print("摄氏温度为:%.3f" %(5/9*(F-32)))
print()

