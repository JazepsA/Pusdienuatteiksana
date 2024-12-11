from datetime import datetime
import datetime

time_str1 = input("1.enter time in this format yyyy-mm-dd")
time1=datetime.datetime.strptime(time_str1, "%Y-%m-%d") 

time_str2 = input("2.enter time in this format yyyy-mm-dd")
time2=datetime.datetime.strptime(time_str2, "%Y-%m-%d")

time3=time2-time1

print(time3)