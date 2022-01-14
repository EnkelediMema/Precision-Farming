
import time
from tqdm import tqdm

on = int(input("Press 1 to turn on the power statin: "))

if on == 1:
    print("Power station activated")
else:
    print("Wrong input ")


time.sleep(3)
print("A new drone request has arrived ")
time.sleep(5)
print("Request is waiting ")
time.sleep(5)
print("Charging station is free ")
time.sleep(3)
al = int(input("Press 1 to allocate the charging  station : "))
if al == 1:
    print("Station allocated")
else:
    print("Wrong input ")

time.sleep(5)
print("Drone is requesting for  a slot  ")
time.sleep(5)
print(" Slot is available  ")
time.sleep(3)
slot = int(input("Press 1 to allocate a slot: "))
if slot == 1:
    print("Slot allocated")
else:
    print("Wrong input ")


time.sleep(5)
print("Charging began")
time.sleep(5)
for i in tqdm(range(100),
              desc="Charging…",
              ascii=False, ncols=75):
    time.sleep(0.1)

print(" Charging Completed.")
time.sleep(5)
print(" Charging queue updated")



