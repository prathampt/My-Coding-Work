import random
import time
num_y = random.randint(1, 10)
num_x = num_y*2

print("\n\nChoose Any Number in your Mind and don't tell me...")
time.sleep(0.5)
print("Are you done Thinking?")
time.sleep(4)
print("Now Multiply your Number by 2")
time.sleep(4)
print("Now add " + str(num_x) + " to it...")
time.sleep(3)
print("Are you done Adding?")
time.sleep(4)
print("Now Divide it by 2 !!!")
time.sleep(5)
print("FINAL MOVE: Subtract Your original number from it...!!!")
time.sleep(4)
print("Are You ready to be shocked???!!!\n")
time.sleep(3)
input("Press Enter...")
print("The answer is " + str(num_y) + " .!.!.!.!.!")
