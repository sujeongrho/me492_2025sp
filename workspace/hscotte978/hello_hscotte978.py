import time
print("Hello! My name is Jeongil Hwang")

Current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", Current_time)
print("Current Time:", formatted_time)
