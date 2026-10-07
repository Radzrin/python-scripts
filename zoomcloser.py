import psutil
import subprocess
import time
import datetime

x = datetime.datetime.now()
print(x.hour, ":", x.minute)

while "Zoom.exe" in (i.name() for i in psutil.process_iter()):
	if(x.hour == 12 and x.minute == 48):
		subprocess.call("TASKKILL /F /IM Zoom.exe", shell=True)

print("zoom is closed")	