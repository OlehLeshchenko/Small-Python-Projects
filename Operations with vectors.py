def res():
    x11=int(x1.get())
    y11=int(y1.get())
    z11=int(z1.get())
    x22=int(x2.get())
    y22=int(y2.get())
    z22=int(z2.get())
    x3=y11*z22-z11*y22
    y3=z11*x22-x11*z22
    z3=x11*y22-y11*x22
    dob_lenght=(x3**2+y3**2+z3**2)**0.5
    result['text']='Координати векторного добутку ('+str(x3)+'; '+str(y3)+'; '+str(z3)+')\nВекторний добуток: '+ str(dob_lenght)
def focus1(event):
    y1.focus_set()
def focus2(event):
    z1.focus_set()
def focus3(event):
    x2.focus_set()
def focus4(event):
    y2.focus_set()
def focus5(event):
    z2.focus_set()
def ress(event):
    res()
    
from tkinter import *
from tkinter.font import Font
root = Tk()    
root.title("Leshchenko")
root.configure(bg="PaleGreen3")
w = 550
h = 350
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
font_title= Font(family="Century Gothic", size=17, weight="bold", slant="italic")
font_subtitle= Font(family="Century Gothic", size=11)
name = Label(root, text="Домашнє завдання", font = font_title,bg="PaleGreen3")
name.grid(row=0, column=0,columnspan=10,padx=155, pady=8)
label = Label(root, text='Уведіть координати двох векторів та нажміть на кнопку "Обчислити",\n щоб дізнатися координати їх векторного добутку та довжину', font=font_subtitle,bg="PaleGreen3")
label.grid(row=1, column=0,columnspan=10, pady=3)


label_x1 = Label(root, text='x1 =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="PaleGreen3")
label_x1.grid(row=2, column=1, padx=0)
x1=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
x1.grid(row=2, column=2, pady=5)
x1.focus_set()
x1.bind('<Return>', focus1)

label_y1 = Label(root, text='y1 =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="PaleGreen3")
label_y1.grid(row=3, column=1, padx=0)
y1=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
y1.grid(row=3, column=2, pady=5)
y1.bind('<Return>', focus2)


label_z1 = Label(root, text='z1 =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="PaleGreen3")
label_z1.grid(row=4, column=1, padx=0)
z1=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
z1.grid(row=4, column=2, pady=5)
z1.bind('<Return>', focus3)


label_x2 = Label(root, text='x2 =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="PaleGreen3")
label_x2.grid(row=2, column=6, padx=0)
x2=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
x2.grid(row=2, column=7, pady=5)
x2.bind('<Return>', focus4)



label_y2 = Label(root, text='y2 =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="PaleGreen3")
label_y2.grid(row=3, column=6, padx=0)
y2=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
y2.grid(row=3, column=7, pady=5)
y2.bind('<Return>', focus5)



label_z2 = Label(root, text='z2 =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="PaleGreen3")
label_z2.grid(row=4, column=6, padx=0)
z2=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
z2.grid(row=4, column=7, pady=5)
z2.bind('<Return>', ress)



but=Button(root,text="Обчислити",width=12,height=1,bg="#d3d3d3",font=Font(family="Century Gothic", size=11), justify="center",  command=res)
but.grid(row=5,column=0,columnspan=9, pady=11)

result=Label(root,text="", font=Font(family="Century Gothic", size=15),bg="PaleGreen3")
result.grid(row=6, column=0, columnspan=10)
root.mainloop()
