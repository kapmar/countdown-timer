import time
def countdown(seconds):
    while seconds > 0:
        print(seconds)
        seconds-= 1
        time.sleep(1)
    print("finished")

count = input("how many seconds would you like to count down?: ")
if count.isdigit():
    count_int = int(count)
    countdown(count_int)
else:
    print("how many seconds would you like to count down?")