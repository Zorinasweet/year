from tkinter import *
import random
import time

w = 500
h = 500
list = []

tk = Tk()
tk.iconbitmap('icon.ico')
tk.title('Happy New Year!')

c = Canvas(tk, width=w, height=h, background='white')
c.pack()

snow = PhotoImage(file = 'snezh.PNG')
snow_s = snow.subsample(2,2)
snow_b = snow.zoom(2,2)

for i in range(10):
    x = random.randint(0,w-50)
    y = random.randint(0,h-50)
    choise = random.randint(1,2)
    if choise == 2:
        snow = snow_b
    else:
        snow = snow_s
    s_obj = c.create_image(x, y, image = snow)
    list.append(s_obj)
    c.update()
    time.sleep(0.1)
v = 1
while True:

    for i in list:

        # x = random.randint(0, 50)
        # y = random.randint(0, 50)
        if c.coords(i)[1] > h:
            v = v * (-1)
        # elif c.coords(i)[2] > w:
        #     c.move(i, x, y * (-1))

        c.move(i, v, v)
    c.update()
    time.sleep(0.1)

tk.mainloop()
