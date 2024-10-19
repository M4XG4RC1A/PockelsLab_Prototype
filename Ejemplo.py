#---------Imports
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from functools import partial
#---------End of imports

fig = plt.Figure()

x = np.arange(0, 2*np.pi, 0.01)        # x-array

def animate(i,textData,line):
    #line.set_ydata(np.sin(x+i/10.0))  # update the data
    print(textData)
    return line

root = Tk.Tk()

label = Tk.Label(root,text="SHM Simulation").grid(column=0, row=0)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(column=0,row=1)

ax = fig.add_subplot(111)
line, = ax.plot(x, np.sin(x))
textData = "Hola"
ani = animation.FuncAnimation(fig, partial(animate,textData=textData,line=line), np.arange(1, 200), interval=25, blit=False)

Tk.mainloop()


"""
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation
from functools import partial

fig, ax = plt.subplots()
t = np.linspace(0, 3, 40)
g = -9.81
v0 = 12
z = g * t**2 / 2 + v0 * t

v02 = 5
z2 = g * t**2 / 2 + v02 * t

scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
line2 = ax.plot(t[0], z2[0], label=f'v0 = {v02} m/s')[0]
ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
ax.legend()


def update(frame,textData):
    # for each frame, update the data stored on each artist.
    print(textData)
    print(frame)
    x = t[:frame]
    y = z[:frame]
    # update the line plot:
    line2.set_xdata(t[:frame])
    line2.set_ydata(z2[:frame])
    return (scat, line2)


ani = animation.FuncAnimation(fig=fig, func=partial(update,textData="Hola"), frames=40, interval=300, repeat=False)
plt.show()
"""