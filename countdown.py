import time
import os


def timer_display(timer):
    hours = timer // 3600
    minutes = timer // 60
    seconds = timer % 60

    if minutes == 60:
        minutes = 0

    print(f"{hours}:{minutes}:{seconds}")


timer = 0

hours = 0
minutes = 0
seconds = 10


timer = (hours * 3600) + (minutes * 60) + seconds


for second in range(timer, 0, -1):
    # os.system("cls")

    timer_display(timer)
    timer -= 1
    time.sleep(1)

print("0:0:0")
