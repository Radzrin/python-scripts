from dash import Dash, dcc, html, Input, Output, State, callback
from dash import callback_context
import base64
import sqlite3
import math


con = sqlite3.connect("boorudb.db")
cur = con.cursor()
res = cur.execute("SELECT url FROM arknuts WHERE arknuts.url NOT LIKE '%.mp4%' limit 15")
#print(res.fetchall())
arr = []
for im in res:
  arr += im

numrow = 0
pg = 0

res = cur.execute("SELECT COUNT(url) FROM arknuts ")
for row in res:
  numrow = row[0] 

con.close()

app = Dash(__name__)

pagenum = 0

#imgfile ="E:\\usb fr fr\\idk\\OG\\BA\\nah.jpg"

defimg = []
for imgfile in arr:
	with open(imgfile, "rb") as image_file:
		img_data = base64.b64encode(image_file.read())
		img_data = img_data.decode()
		if(".mp4" in img_data):
			img_data = "{}{}".format("data:video/mp4;base64, ", img_data)
		else:	
			img_data = "{}{}".format("data:image/jpg;base64, ", img_data)

		defimg.append(img_data)

app.layout = html.Div(children=[
	html.Nav(children=[
		html.H1(children='localbooru')
		]),
	html.Div(children=[
		html.Ul(children=[
				html.Li("W (arknights)"),
				html.Li("arknights"),
				html.Li("Touhou"),
				html.Li("imagine this was a tag"),
				html.Li("imagine this was a tag"),
				html.Li("imagine this was a tag"),
				html.Li("imagine this was a tag"),
				html.Li("imagine this was a tag"),
				html.Li("imagine this was a tag"),
				html.Li("imagine this was a tag"),
				html.Li("imagine this was a tag"),
				html.Li("imagine this was a tag"),
				html.Li("imagine this was a tag"),
				html.Li("imagine this was a tag"),
				html.Li(children=[
					html.Button('後', id='prevBut', n_clicks=0),
					html.P("0",id='c'),
					html.Button('次', id='nextBut', n_clicks=0)
					], id="buttons")
			])
		], id="sidebar"),
	html.Div(children=[
		html.A(href=defimg[0],target="_blank", children=[html.Img(src=defimg[0], id="p1")]),
	html.A(href=defimg[1],target="_blank", children=[html.Img(src=defimg[1], id="p2")]),
	html.A(href=defimg[2],target="_blank", children=[html.Img(src=defimg[2], id="p3")]),
	html.A(href=defimg[3],target="_blank", children=[html.Img(src=defimg[3], id="p4")]),
	html.A(href=defimg[4],target="_blank", children=[html.Img(src=defimg[4], id="p5")]),
	html.A(href=defimg[5],target="_blank", children=[html.Img(src=defimg[5], id="p6")]),
	html.A(href=defimg[6],target="_blank", children=[html.Img(src=defimg[6], id="p7")]),
	html.A(href=defimg[7],target="_blank", children=[html.Img(src=defimg[7], id="p8")]),
	html.A(href=defimg[8],target="_blank", children=[html.Img(src=defimg[8], id="p9")]),
	html.A(href=defimg[9],target="_blank", children=[html.Img(src=defimg[9], id="p10")]),
	html.A(href=defimg[10],target="_blank", children=[html.Img(src=defimg[10], id="p11")]),
	html.A(href=defimg[11],target="_blank", children=[html.Img(src=defimg[11], id="p12")]),
	html.A(href=defimg[12],target="_blank", children=[html.Img(src=defimg[12], id="p13")]),
	html.A(href=defimg[13],target="_blank", children=[html.Img(src=defimg[13], id="p14")]),
	html.A(href=defimg[14],target="_blank", children=[html.Img(src=defimg[14], id="p15")])
		], id="pics")
])

@callback(
	Output('c', 'children'),
	Output('p1', 'src'),
	Output('p2', 'src'),
	Output('p3', 'src'),
	Output('p4', 'src'),
	Output('p5', 'src'),
	Output('p6', 'src'),
	Output('p7', 'src'),
	Output('p8', 'src'),
	Output('p9', 'src'),
	Output('p10', 'src'),
	Output('p11', 'src'),
	Output('p12', 'src'),
	Output('p13', 'src'),
	Output('p14', 'src'),
	Output('p15', 'src'),
	[Input('prevBut', 'n_clicks'),
	 Input('nextBut', 'n_clicks')],
	prevent_initial_call=True
)
def previous_page(prev, nex):
	global numrow
	global pg
	global arr

	maxpage = math.ceil((numrow / 15))

	trigger = callback_context.triggered[0] 

	if("nextBut" in trigger["prop_id"].split(".")[0]):
		if(pg != maxpage):
			pg +=1
	else:
		if(pg != 0):
			pg -= 1	

	curRow = 0

	#1-15, 16-30 , 31-46, 47-62, 63-78

	curRow = (pg * 15) + 1
	curLast = curRow + 14

	con = sqlite3.connect("boorudb.db")
	cur = con.cursor()

	res = cur.execute(f"SELECT url FROM arknights WHERE arknights.url NOT LIKE '%.mp4%' LIMIT {curRow}, {curLast};")
	arr = []
	for im in res:
		arr += im		

	defimg = []
	for imgfile in arr:
		with open(imgfile, "rb") as image_file:
			img_data = base64.b64encode(image_file.read())
			img_data = img_data.decode()
			img_data = "{}{}".format("data:image/jpg;base64, ", img_data)
			defimg.append(img_data)	
	
	con.close()		

	if len(defimg) % 15 != 0:
		while(len(defimg) % 15 != 0):
			defimg.append("#")
	return pg, defimg[0], defimg[1],defimg[2], defimg[3],defimg[4], defimg[5],defimg[6], defimg[7],defimg[8], defimg[9],defimg[10], defimg[11],defimg[12], defimg[13],defimg[14]

if __name__ == '__main__':
	app.run(debug=True)
