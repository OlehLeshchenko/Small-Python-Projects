def square(a,b,c):
    p=(a+b+c)/2
    abc=(p*(p-a)*(p-b)*(p-c))**0.5
    return abc
def res():
    xaa=float(xa.get())
    yaa=float(ya.get())
    xbb=float(xb.get())
    ybb=float(yb.get())
    xcc=float(xc.get())
    ycc=float(yc.get())
    xmm=float(xm.get())
    ymm=float(ym.get())
    AB=((xbb-xaa)**2+(ybb-yaa)**2)**0.5
    AC=((xcc-xaa)**2+(ycc-yaa)**2)**0.5
    BC=((xbb-xcc)**2+(ybb-ycc)**2)**0.5
    AM=((xmm-xaa)**2+(ymm-yaa)**2)**0.5
    BM=((xmm-xbb)**2+(ymm-ybb)**2)**0.5
    CM=((xmm-xcc)**2+(ymm-ycc)**2)**0.5
    if round(square(AB,BC,AC),4)==round(square(AB,BM,AM)+square(BC,CM,BM)+square(AC,CM,AM),4): pop='лежить'
    else: pop='не лежить'
    result['text']='Точка М '+pop+' в трикутнику ABC'
def focus1(event):
    ya.focus_set()
def focus2(event):
    xb.focus_set()
def focus3(event):
    yb.focus_set()
def focus4(event):
    xc.focus_set()
def focus5(event):
    yc.focus_set()
def focus6(event):
    xm.focus_set()
def focus7(event):
    ym.focus_set()
def ress(event):
    res()
    
from tkinter import *
from tkinter.font import Font
root = Tk()    
root.title("Leshchenko")
root.configure(bg="#eb6a83")
w = 550
h = 400
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
font_title= Font(family="Century Gothic", size=17, weight="bold", slant="italic")
font_subtitle= Font(family="Century Gothic", size=11)
name = Label(root, text="Домашнє завдання", font = font_title,bg="#eb6a83")
name.grid(row=0, column=0,columnspan=10,padx=155, pady=8)
label = Label(root, text='Уведіть координати вершин трикутника A, B, C і точки М,\n та нажміть на кнопку "Обчислити", щоб дізнатися\n чи лежить точка M в трикутнику ABC', font=font_subtitle,bg="#eb6a83")
label.grid(row=1, column=0,columnspan=10, pady=3)

label_xa = Label(root, text='xa =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="#eb6a83")
label_xa.grid(row=2, column=1, padx=0)
xa=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
xa.grid(row=2, column=2, pady=5)
xa.focus_set()
xa.bind('<Return>', focus1)

label_ya = Label(root, text='ya =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="#eb6a83")
label_ya.grid(row=2, column=6, padx=0)
ya=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
ya.grid(row=2, column=7, pady=5)
ya.bind('<Return>', focus2)

label_xb = Label(root, text='xb =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="#eb6a83")
label_xb.grid(row=3, column=1, padx=0)
xb=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
xb.grid(row=3, column=2, pady=5)
xb.bind('<Return>', focus3)

label_yb = Label(root, text='yb =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="#eb6a83")
label_yb.grid(row=3, column=6, padx=0)
yb=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
yb.grid(row=3, column=7, pady=5)
yb.bind('<Return>', focus4)

label_xc = Label(root, text='xc =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="#eb6a83")
label_xc.grid(row=4, column=1, padx=0)
xc=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
xc.grid(row=4, column=2, pady=5)
xc.bind('<Return>', focus5)

label_yc = Label(root, text='yc =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="#eb6a83")
label_yc.grid(row=4, column=6, padx=0)
yc=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
yc.grid(row=4, column=7, pady=5)
yc.bind('<Return>', focus6)

label_xm = Label(root, text='xm =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="#eb6a83")
label_xm.grid(row=5, column=1, padx=0)
xm=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
xm.grid(row=5, column=2, pady=5)
xm.bind('<Return>', focus7)

label_ym = Label(root, text='ym =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="#eb6a83")
label_ym.grid(row=5, column=6, padx=0)
ym=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
ym.grid(row=5, column=7, pady=5)
ym.bind('<Return>', ress)

but=Button(root,text="Обчислити",width=12,height=1,bg="#d3d3d3",font=Font(family="Century Gothic", size=11), justify="center",  command=res)
but.grid(row=6,column=0,columnspan=9, pady=11)

result=Label(root,text="", font=Font(family="Century Gothic", size=15),bg="#eb6a83")
result.grid(row=7, column=0, columnspan=10)
root.mainloop()
