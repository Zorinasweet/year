from tkinter import *
import random
import time 

tk = Tk()
tk.iconbitmap('icon.ico')

WIDTH = 500
HEIGHT = 500
canvas = Canvas(tk, width=WIDTH , 
		 height = HEIGHT, bg='white') #установили цвет
canvas.pack()

#маленькие снежинки
image_snezh_small = PhotoImage(file='snezh.PNG')
size = random.randint(1,3)
#subsample()  - уменьшает размер
image_snezh_small = image_snezh_small.subsample(size,size)

#большие снежинки
image_snezh_big = PhotoImage(file='snezh.PNG')
size = random.randint(2,3)
#zoom() - увеличивает размер
image_snezh_big = image_snezh_big.zoom(size,size)
#-----------------------------------------------------#
list_s=[] #будет хранить объекты снежинок

count = int(input('Сколько снежинок добавить: '))
for i in range(count):
	x = random.randint(50,450)  #случайное положение по Х
	y = random.randint(50,450) #случайное положение по У
	
	if random.randint(1,3) == 1: #вероятность больший снежинок
		image_snezh = image_snezh_big #назначили большую снежинку
	else: image_snezh = image_snezh_small #а тут маленькую
	
	s_obj= canvas.create_image( x, y , image = image_snezh )
	
	list_s.append(s_obj) #добавляем в список объект снежинки
	canvas.update()
	time.sleep(0.1)

	

while True:
	for i in list_s: #идем по всем изображениям
		canvas.move(i , 1,1) #двигать 
	time.sleep(0.01)
	canvas.update()
	

tk.mainloop()

