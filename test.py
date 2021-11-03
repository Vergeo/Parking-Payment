import datetime
import time

now = datetime.datetime.now()
# i = 0
# while i < 1000000 :
# 	print(i)
# 	i+=1
end = datetime.datetime.now()
local = time.ctime()
print(end)
print(local)

day = local[0] +local[1] + local[2]
month = local[4]+local[5]+local[6]
print(day, month)


#0:00:11.759146