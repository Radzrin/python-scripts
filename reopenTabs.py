import webbrowser
url = []
browser_path = 'C:/Program Files/Librewolf/Librewolf.exe --args --private-window %s'
i = 0

#C:/Program Files/Mozilla Firefox/firefox.exe --args --private-window %s
#C:/Program Files/Librewolf/Librewolf.exe --args --private-window
#go through links
def opfile():
	global url 
	file = open('lnks4.txt', 'r', encoding='utf-8')
	line = file.readline()
	url += [line]
	while line:
		line = file.readline()
		if line == "\n":
			continue
		url += [line]	
	file.close()

def opLnk():
	for x in url:	
		webbrowser.get(browser_path).open(x)


opfile()
opLnk()

