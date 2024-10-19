from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import colorchooser
from tkinter import ttk

import os

#import RPi.GPIO as GPIO

import random

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np
# from mat4py import loadmat
# import h5py
import scipy.io

import matplotlib.animation as animation
from functools import partial
import time

#Tkinter Start
root= Tk()
root.title("PockelsLab")
#root.attributes('-fullscreen',True)

#Screen Properties
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("%dx%d" % (screen_width, screen_height))
pixel = tk.PhotoImage(width=1, height=1)
px = 1/plt.rcParams['figure.dpi']

#Obtain data
def Obtain(srcS,index):
	File=open(srcS,"r")
	Lines=File.readlines()
	File.close()
	Result=Lines[index].rstrip("\n")
	Result.strip()
	return Result
	pass


#Pins Definition
lRing = [1,2,3]
lBTO = [1,2,3]

bRing = [1,2,3]
bBTO = [1,2,3]

system = "GPIO"

""""
#GPIO start
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(lRing[0], GPIO.OUT)
GPIO.setup(lRing[1], GPIO.OUT)
GPIO.setup(lRing[2], GPIO.OUT)

GPIO.setup(lBTO[0], GPIO.OUT)
GPIO.setup(lBTO[1], GPIO.OUT)
GPIO.setup(lBTO[2], GPIO.OUT)

GPIO.setup(bRing[0], GPIO.IN)
GPIO.setup(bRing[1], GPIO.IN)
GPIO.setup(bRing[2], GPIO.IN)

GPIO.setup(bBTO[0], GPIO.IN)
GPIO.setup(bBTO[1], GPIO.IN)
GPIO.setup(bBTO[2], GPIO.IN)
"""

def close(event):
	root.quit(); root.destroy()

global anim
anim = [0]*4

#Colors
bluetec = "#0039A6"

rColors = ["RED", "GREEN", "BLUE"]
rMixedColor = "WHITE"
bgBack = 'BLACK'
labelColor = "WHITE"
gridColor = "WHITE"
faceCol = "#0f0f0f" #(0.06,0.06,0.06)

btnColor1 = faceCol
btnColor2 = bluetec
btnColor3 = "#ffffff" #On click Color
btnColor4 = bgBack

legendColor = "#000000"

GC_State = "GC_OFF" #"GC_ON"/"GC_OFF"

#Frames
Analysis = Frame(root, bg=bgBack, width=screen_width*4/5, height=screen_height)
Analysis.pack(side= LEFT) #Start of the Principal Frame with the first Flange Color
Action = Frame(root, bg=bgBack, width=screen_width/5, height=screen_height, highlightbackground="white", highlightthickness=1)
Action.pack(side= RIGHT)#Start the part of the sentences

#First Graph
fig, ax = plt.subplots(figsize=(int(screen_width*4/5)*px, int(screen_height*5/6)*px))
fig.patch.set_facecolor(bgBack)
canvas = FigureCanvasTkAgg(fig, master= Analysis)
canvas.get_tk_widget().place(x=0,y=0)
canvas.get_tk_widget().config(bg=bgBack)

# x = np.linspace(0, 2*np.pi, 400)
# y = np.sin(x**2)
# ax.plot(x,y,label="Hola")
# ax.legend(loc='best', labelcolor=legendColor) #loc='upper right'

#Progress bar
progress = ttk.Progressbar(length=screen_width*4/5)
progress.place(x=0,y=screen_height*39/40,height=screen_height/40)

#Second Plot
fig2, ax2 = plt.subplots(figsize=(int(screen_width/5)*px, (int(screen_height/6))*px))
fig2.patch.set_facecolor(bgBack)
canvas2 = FigureCanvasTkAgg(fig2, master= Analysis)
canvas2.get_tk_widget().place(x=0,y=int(screen_height*5/6)-screen_height/40)
canvas2.get_tk_widget().config(bg=bgBack)
fig2.tight_layout()

#Indicators

cWidth = int(screen_width*3/5)
cHeight = int(screen_height/6-screen_height/40)
chSpace = int(cHeight/10)
cSpace = int(cWidth/10)
cDiam = int(cHeight*8/10)

ledCanvas = Canvas(Analysis, width=cWidth, height=cHeight, bg=bgBack, border=-2)
ledCanvas.place(x=int(screen_width/5),y=int(screen_height*5/6))

Ring1 = ledCanvas.create_oval(cSpace, chSpace, cSpace+cDiam, chSpace+cDiam, fill=bgBack, width=int(cHeight/15), outline=faceCol)
Ring2 = ledCanvas.create_oval(cSpace*2+cDiam, chSpace, cSpace*2+cDiam*2, chSpace+cDiam, fill=bgBack, width=int(cHeight/15), outline=faceCol)
Ring3 = ledCanvas.create_oval(cSpace*3+cDiam*2, chSpace, cSpace*3+cDiam*3, chSpace+cDiam, fill=bgBack, width=int(cHeight/15), outline=faceCol)

#Action buttons
"""
def getRings():
	dRings = {'R1':1 if GPIO.input(bRing[0]) else 0,
	'R2':1 if GPIO.input(bRing[1]) else 0,
	'R3':1 if GPIO.input(bRing[2]) else 0}
	return dRings

def getBTO():
	dBTO = {'R1':1 if GPIO.input(bBTO[0]) else 0,
	'R2':1 if GPIO.input(bBTO[1]) else 0,
	'R3':1 if GPIO.input(bBTO[2]) else 0}
	return dBTO

def setRings(lArray):
	GPIO.output(lRing[0],lArray["R1"])
	GPIO.output(lRing[1],lArray["R2"])
	GPIO.output(lRing[2],lArray["R3"])

def setRings(lArray):
	GPIO.output(lBTO[0],lArray["R1"])
	GPIO.output(lBTO[1],lArray["R2"])
	GPIO.output(lBTO[2],lArray["R3"])
"""

def animate(frames,line,xdata,ydata,index):
	if index == 0:
		if frames < 1000:
			line.set_xdata(xdata[-frames:])
			line.set_ydata(ydata[-frames:])
	elif index == 1:
		if frames < 2000 and frames > 999:
			line.set_xdata(xdata[-frames+1000:])
			line.set_ydata(ydata[-frames+1000:])
	elif index == 2:
		if frames < 3000 and frames > 1999:
			line.set_xdata(xdata[-frames+2000:])
			line.set_ydata(ydata[-frames+2000:])
	elif index == 3:
		if frames < 4000 and frames > 2999:
			line.set_xdata(xdata[-frames+3000:])
			line.set_ydata(ydata[-frames+3000:])
	return line

def namedState(sBTO,sRing):
	strBTO = "Active" if sBTO == 1 else "Inactive"
	strRing = "Detect" if sRing == 1 else "Empty"
	return strBTO+strRing

def plotGraph(dRing,dBTO,labelStr,lStyle,lColor,lWidth,index):
	global anim
	#Example Res1InactiveEmpty Active/Inactive Detect/Empty
	res1 = 'Res1'+namedState(dBTO["R1"],dRing["R1"])
	res2 = 'Res2'+namedState(dBTO["R2"],dRing["R2"])
	res3 = 'Res3'+namedState(dBTO["R3"],dRing["R3"])
	path = "./Simulation/"+GC_State+"/"+res1+"/"+res2+"/"+res3+"/Circuit"+GC_State+"_"+res1+"_"+res2+"_"+res3+".mat";
	data = scipy.io.loadmat(path)
	gain = np.array(data.get('gain'))[4500:5500]
	wavelength = np.array(data.get('wavelength'))[4500:5500]
	result, = ax.plot(wavelength[0],gain[0], label=labelStr, linestyle=lStyle, color=lColor, linewidth=lWidth)
	if index == 0:
		anim[index] = animation.FuncAnimation(fig, partial(animate,line=result,xdata=wavelength,ydata=gain,index=index), np.arange(0,1000,10), interval=2, repeat=False)
	else:
		anim[index] = animation.FuncAnimation(fig, partial(animate,line=result,xdata=wavelength,ydata=gain,index=index), np.arange(0,4000,10), interval=2, repeat=False)

def confGraph():
	ax.set_title('Circuit Output')
	ax.set_ylabel('Intensity') # Y label ax.set_ylabel('Active Wee1', fontsize = 20.0)
	ax.set_xlabel('Wavelenght') # X label ax.set_xlabel('Active Cdc2-cyclin B', fontsize = 20) # X label
	ax.xaxis.label.set_color(labelColor); ax.yaxis.label.set_color(labelColor)
	ax.tick_params(colors=gridColor)
	ax.set_facecolor(faceCol)
	ax.set(xlim=[1.5434e-6, 1.5533e-6], ylim=[-1.5, -0.1])
	#ax.grid(True)

def setBars(dRings):
	print(dRings)
	rings = list(dRings.keys())
	values = list(dRings.values())
	ax2.bar(rings, values, color=rColors, width=0.4)
	ax2.set_title('States')
	ax2.xaxis.label.set_color(labelColor); ax2.yaxis.label.set_color(labelColor)
	ax2.tick_params(colors=gridColor)
	ax2.set_facecolor(faceCol)
	ax2.set(ylim=[0,1])
	canvas2.draw_idle()

def setIndicators(dRings):
	if dRings["R1"]:
		ledCanvas.itemconfig(Ring1, outline=rColors[0])
	else:
		ledCanvas.itemconfig(Ring1, outline=faceCol)
		
	if dRings["R2"]:
		ledCanvas.itemconfig(Ring2, outline=rColors[1])
	else:
		ledCanvas.itemconfig(Ring2, outline=faceCol)
		
	if dRings["R3"]:
		ledCanvas.itemconfig(Ring3, outline=rColors[2])
	else:
		ledCanvas.itemconfig(Ring3, outline=faceCol)

def funRead():
	print("Reading")
	ax.clear()
	ax2.clear()
	dRings = {'R1':1,'R2':0,'R3':0} #getRings Fun
	dBTO = {'R1':0,'R2':0,'R3':0} #getBTOs Fun
	plotGraph(dRings,dBTO,"Actual State","solid","blue",2,0)
	confGraph()
	setBars(dRings)
	setIndicators(dRings)
	ax.legend(loc='best', labelcolor=legendColor) #loc='upper right'
	canvas.draw_idle()

def funAnalysis():
	global anim
	print("Reading")
	ax.clear()
	ax2.clear()
	confGraph()
	dRings = {'R1':1,'R2':0,'R3':1} #getRings Fun
	dBTO = {'R1':0,'R2':0,'R3':0}
	plotGraph(dRings,dBTO,"No BTO","solid",rMixedColor,4,0)
	dBTO = {'R1':1,'R2':0,'R3':0}
	plotGraph(dRings,dBTO,"BTO 1","solid",rColors[0],6,1)
	dBTO = {'R1':0,'R2':1,'R3':0}
	plotGraph(dRings,dBTO,"BTO 2","solid",rColors[1],4,2)
	dBTO = {'R1':0,'R2':0,'R3':1}
	plotGraph(dRings,dBTO,"BTO 3","solid",rColors[2],2,3)
	setBars(dRings)
	setIndicators(dRings)
	ax.legend(loc='best', labelcolor=legendColor) #loc='upper right'
	canvas.draw_idle()
	pass

#First Plots

confGraph()
dRings = {'R1':0,'R2':0,'R3':0}
setBars(dRings)

#Action Buttons

btnRead = Button(Action, 
				text= "Read", 
				image= pixel, 
                background= btnColor1,
				foreground= btnColor2,
				activebackground= btnColor3,
				activeforeground= btnColor4,
				highlightthickness= 1,
				highlightbackground= btnColor2,
				highlightcolor= "WHITE",
				border= 2,
				cursor= "hand1",
				font= ("Arial", 10, "bold"),
				width=int(screen_width/10), height=int(screen_height/10),
				command=lambda:funRead(), 
				compound="c",)
btnRead.place(x=int(screen_width/20), y=int(screen_height*3/10))

btnAnalysis = Button(Action, 
				text= "Analysis", 
				image= pixel, 
                background= btnColor2,
				foreground= btnColor4,
				activebackground= btnColor3,
				activeforeground= btnColor4,
				highlightthickness= 1,
				highlightbackground= btnColor2,
				highlightcolor= "WHITE",
				border= 2,
				cursor= "hand1",
				font= ("Arial", 10, "bold"),
				width=int(screen_width/10), height=int(screen_height/10),
				command=lambda:funAnalysis(), 
				compound="c",)
btnAnalysis.place(x=int(screen_width/20), y=int(screen_height*6/10))

#Root commands
root.bind('<Escape>', close)
root.protocol('WM_DELETE_WINDOW', lambda:close("Closed"))
root.mainloop()