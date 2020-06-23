import requests 
from django.http import HttpResponse
from django.shortcuts import render
import json
from .models import JsonModel 
import os
# Create your views here.
def home_view(request):
 	# if request.method == 'POST':
 	# 	r = requests.get('http://172.20.226.2/data1.json', params=request.POST)
 	# 	jsondata=r.json()
 	# else:
 	# 	r = requests.get('http://172.20.226.2/data1.json', params=request.GET)
 	# 	jsondata=r.json()
 	# 	js=json.dumps(jsondata)
 	# 	text=get_dirs()
 	# if r.status_code == 200:
 		#return render(request,'index.html', {'js':json.loads(js),'jsonfiles':text})
 	#return HttpResponse('Could not save data')
 	jsonlist=[];

 	text=os.listdir(r'/home/harekrishna/PycharmProjects/django/medicalProject')
 	text.sort()
 	print(text)
 	for file in text:
 		print(file)
 		with open('/home/harekrishna/PycharmProjects/django/medicalProject/'+file,'r') as f:
 			jsonfile = json.load(f)
 			print(jsonfile)
 			jsonlist.append(jsonfile)
 	print(jsonlist)
 	return render(request,'index.html', {'jsonfiles':jsonlist})


#def get_dirs():
	# text=os.listdir(r'D:\Projects\djangoProjects\JsonFiles')	
	#return text

# def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # create an example graph
#         Fs = 8000
#         f = 5
#         sample = 8000
#         x = np.arange(sample)
#         y = np.sin(2 * np.pi * f * x / Fs)

#         # here you can customize individual components of a graph property
#         plot = figure( x_axis_label='xaxis', plot_width=200, plot_height=200)
#         plot.line(x,y, line_width=2, color='darkred')
#         plot.toolbar.logo = None
#         plot.background_fill_color = "black"
#         plot.border_fill_color = "black"
#         plot.outline_line_width = 1
#         plot.outline_line_color = "#00bfff"
#         plot.title.text_color = "#00bfff"
#         plot.xaxis.axis_line_color = "#00bfff"
#         plot.yaxis.axis_line_color = "#00bfff"
#         plot.yaxis.major_label_text_color = "#00bfff"
#         plot.xaxis.major_label_text_color = "#00bfff"
#         plot.xgrid.grid_line_color = "#00bfff"
#         plot.ygrid.grid_line_color = "#00bfff"

#         # adjust the layout
#         plot_l = layout([plot], sizing_mode='stretch_width')

#         #create json item of graphs
#         json_plot = json_item(plot_l, 'myplot') 

#         # convert dict to string
#         stringplot = json.dumps(json_plot)
#         context.update({'plot_l':stringplot})
#         return context
