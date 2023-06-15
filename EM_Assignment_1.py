# MIS: 612203176
import math as m 

n = int(input("Enter no. of forces: "))
Frx = 0
Fry = 0

for i in range(n):
    f = float(input(f"Enter force {i+1} (in N): "))
    a = float(input("Enter it's angle with x-axis (in degrees): "))
    # We have taken angle in degrees, thus need to convert it into radians before passing into the function...
    Frx += f*m.cos(a*m.pi/180)
    Fry += f*m.sin(a*m.pi/180)
    
print("Thus, resultant force is:\n",f"Fr = {round(Frx,2)} i + {round(Fry,2)} j")
print("|Fr| =", round(m.sqrt(Frx**2 + Fry**2),2),"N")
print("Angle made by resultant with x-axis is: theta = ", round((360+180*m.atan2(Fry, Frx)/m.pi)%360,2),"°",sep="")

print("Thus, equilibrant force is:\n",f"Fe = {round(-Frx,2)} i + {round(-Fry,2)} j")
print("|Fe| =", round(m.sqrt(Frx**2 + Fry**2),2),"N")
print("Angle made by equilibrant with x-axis is: theta = ", round((360+180*m.atan2(-Fry, -Frx)/m.pi)%360,2),"°",sep="")
