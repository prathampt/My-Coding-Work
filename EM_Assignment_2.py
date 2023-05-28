# MIS: 612203176
# Coplanar Non-concurrent Forces Computer Assignment 2
import math as m 

n = int(input("Enter no. of forces: "))
Frx = 0
Fry = 0
p = 0

for i in range(n):
    f = float(input(f"Enter force {i+1} (in N): "))
    a = float(input("Enter it's angle with x-axis (in degrees): "))
    x_c = float(input("Enter it's x co-ordinate: "))
    y_c = float(input("Enter it's y co-ordinate: "))
    # r = m.sqrt(x_c**2+y_c**2)

    # We have taken angle in degrees, thus need to convert it into radians before passing into the function...
    Frx += f*m.cos(a*m.pi/180)
    Fry += f*m.sin(a*m.pi/180)
    p += f*m.cos(a*m.pi/180)*(-y_c) + f*m.sin(a*m.pi/180)*(x_c)


f = round(m.sqrt(Frx**2 + Fry**2),2)
frx = round(Frx,2)
fry = round(Fry,2)
r = round(p/f,2)
print("Thus, resultant force is:\n",f"Fr = {frx} i + {fry} j")
print("|Fr| =", f,"N")
print("Angle made by resultant with x-axis is: theta = ", round((360+180*m.atan2(Fry, Frx)/m.pi)%360,2),"°",sep="")
print("Distance of force from origin is, r:",r)
