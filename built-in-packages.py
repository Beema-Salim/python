import statistics,time,math
print("The value of pi is",math.pi)
seconds=time.time()
print("seconds since epoch(the point where time begins)=",seconds)
li=[1,2,3,3,2,2,2]
print("the average of list values:",end="")
print(statistics.mean(li))
local_time=time.ctime(seconds)
print("Local_time:",local_time)