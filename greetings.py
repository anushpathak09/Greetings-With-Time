#creating good morning.py with the help of time module.
import time
timestamp=time.strftime("%H")
print(timestamp)
if(1<=int(timestamp)<12):
    print("Good morning!")
elif(12<=int(timestamp)<17):
    print("Good afternoon!")
else:
     print("Good evening!")