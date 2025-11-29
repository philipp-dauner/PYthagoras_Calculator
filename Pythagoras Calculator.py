import time
import math
print("Welcome to the Pythagorean Theorem Calculator!")
time.sleep(2)
print("Loading...")
time.sleep(10)
entering = input("Press Enter to continue")
if entering == "":
    print("Let's get started!...")
time.sleep(2)
a = float(input("How long is your side adjacent to the right angle: "))
b = float(input("How long is your second side adjacent to the right angle: "))
c = math.sqrt(a**2 + b**2)
wait = ("OK PLEASE WAIT A MOMENT...")
print(wait)
time.sleep(3)
print("The length of the hypotenuse is: " + str(c))
print("Thank you for using this program!")
time.sleep(20)
