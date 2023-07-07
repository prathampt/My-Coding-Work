# MIS: 612203176
import math as m 

print("Enter 1 to have roller support on left side and hinge support on right or")
x = int(input("Enter 2 to to have hinge support on left side and roller support on right\n"))
l_beam = int(input("Enter length of beam: "))
a_x = a_y = m_y = 0
n = int(input("Enter no. of forces: "))

for i in range(n):
    f = float(input(f"Enter force {i+1} (in N): "))
    a = float(input("Enter it's angle with x-axis (in degrees): "))
    l = float(input("Enter it's point of application w.r.t. the roller support: "))
    # We have taken angle in degrees, thus need to convert it into radians before passing into the function...
    a_x += f*m.cos(a*m.pi/180)
    a_y += f*m.sin(a*m.pi/180)
    m_y += f*m.sin(a*m.pi/180)*l

m_y = m_y / l_beam
b_y = a_y - m_y

if (x==1):
    net = m.sqrt(a_x**2+m_y**2)
    print(f"Hinge reaction is {a_x} N along x direction and {m_y} N along y direction with magnitude of {net} N.")
    print(f"Roller reaction is {b_y} N along y direction.")
elif (x==2):
    net = m.sqrt(a_x**2+b_y**2)
    print(f"Hinge reaction is {a_x} N along x direction and {b_y} N along y direction with magnitude of {net} N.")
    print(f"Roller reaction is {m_y} N along y direction.")
