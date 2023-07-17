import tkinter as tk
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import time

root = tk.Tk()
root.title("식현상")
root.configure(bg='black')
canvas2_x = 1400
canvas2_y = 600
fig = plt.Figure()
dpi = fig.dpi
fig.set_size_inches(1400 / dpi, 450 / dpi)
ax = fig.add_subplot(111)
def update_graph():
    while True:
        for i in range(0,360):
            size = scale2.get()
            sin = math.cos(math.radians(i))
            ax.clear()
            canvas2.delete("planet")
            if (0<=i<180):
                a = np.linspace(i-180, i, 360)
                y = np.log(np.abs(a))
                ax.plot(a, y)
                ax.axis(ymin=0,ymax=6)
            # label1.config(text = '정적분 넓이: ')
            # g =scale.get()
            # label2.config(text = '사각형 넓이: '+ str(dimension))
                canvas2.create_oval(canvas2_x/2-sin*500-10, canvas2_y/2-10, canvas2_x/2-sin*500+10, canvas2_y/2+10, fill='white', tags='planet')
            else:
                a = np.linspace(0,180, 360)
                y = np.full_like(a, 5)
                ax.plot(a, y)
                ax.axis(ymin=0,ymax=6)
                canvas2.create_oval(canvas2_x/2-sin*500-10, canvas2_y/2-10, canvas2_x/2-sin*500+10, canvas2_y/2+10, fill='white', tags='planet')
            canvas.draw()
            root.update()
font = tk.font.Font(size =25)
scale = tk.Scale(root, orient="horizontal", from_=100, to=500, bg = 'white', length=540, resolution = 10)
scale2 = tk.Scale(root, orient="horizontal", from_=1, to=100, bg = 'white', length=540, resolution = 1)
scale.set(100)
scale.place(x=10, y =100)
scale2.set(2)
scale2.place(x=10, y =200)
canvas2 = tk.Canvas(root, bg='black', width=canvas2_x, height=canvas2_y)
canvas2.place(x=1920-canvas2_x, y=0)

# label1 = tk.Label(root, text = '정적분 넓이: ', bg = 'white', font = font)
# label2 = tk.Label(root, text = '사각형 넓이: ', bg = 'white', font = font)
# label1.place(x=50, y =600)
# label2.place(x=50, y =700))

canvas2.create_oval(canvas2_x/2-scale.get(), canvas2_y/2-scale.get(), canvas2_x/2+scale.get(), canvas2_y/2+scale.get(), fill='yellow', tags='star')
canvas2.create_oval(canvas2_x/2-500, canvas2_y/2-10, canvas2_x/2-520, canvas2_y/2+10, fill="white", tags='planet')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().place(x=1920-canvas2_x, y=canvas2_y)
update_graph()
root.mainloop()