import psutil
import subprocess
import win32gui
import win32con


def windowEnumHandler(hwnd, top_windows):
	top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

if not "Discord.exe" in (i.name() for i in psutil.process_iter()):
	subprocess.call("Start Discord://", shell=True)
else:
	def bringToFront(window_name):
		top_windows = []
		win32gui.EnumWindows(windowEnumHandler, top_windows)
		for i in top_windows:
			if window_name.lower() in i[1].lower():
				win32gui.ShowWindow(i[0], win32con.SW_SHOWNORMAL)
				win32gui.SetForegroundWindow(i[0])
				break
	bringToFront("Discord")		
	print("sussy script")	


if __name__ == "__main__":
	pass
	#winname = "discord"
	#bringToFront(winname)
