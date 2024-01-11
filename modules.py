import time
from importlib import reload
import random
# load 1st time

time.sleep(20)

print("hello")

time.sleep(20) 

print("hell02")
 # reload again  
print("This is test file..")

a=["list1","list2","list3","list4","list5"]

print(random.choice(a))

print(random.choices(a,k=2))
