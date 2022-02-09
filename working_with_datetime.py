from datetime import datetime
import time

dt = datetime(2022, 2, 9)
print(dt)

dt = datetime.now()
print(dt)

dt = datetime.strptime("2022/02/09", "%Y/%m/%d")
print(dt)

tm = time.time()
dt = datetime.fromtimestamp(tm)
print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))

print(dt.isoformat())

dt2 = datetime.now()
print(dt2 > dt)
