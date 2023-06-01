def integ(a):
    if a==int(a): a=int(a)
    return a
def res():
    global i, x, y
    top=int(peak.get())
    t=[0]*top;xn=[0]*top; yn=[0]*top
    if i<=top:
        i+=1
        if i<top+1:
            label_x11['text']='x'+str(i)+' ='
            label_y11['text']='y'+str(i)+' ='
        x.append(float(x11.get()))
        y.append(float(y11.get()))
    if i==top+1:
        m=0
        for i in range(1,top):
            if y[i]>y[m]: m=i
            else:
                if y[i]==y[m] and x[i]<x[m]: m=i
        k=0
        x1=x[m];y1=y[m]
        xn[k]=x1;yn[k]=y1
        poshuk = True
        while poshuk:
            poshuk=False
            for i in range(top):
                if t[i]==0:
                    x2=x[i]; y2=y[i]
                    pt= True
                    for j in range(top):
                        if (x[j]-x1)*(y2-y1)-(y[j]-y1)*(x2-x1)>0:
                            pt = False
                        if pt==False:
                            for j in range(top):
                                if (x[j]-x1)*(y2-y1)-(y[j]-y1)*(x2-x1)<0:
                                    pt= False
                    if pt:
                        k+=1
                        x1=x2;y1=y2
                        t[i]=k
                        xn[k]=x1;yn[k]=y1
                        poshuk=True
        result['text']='Координати точок:\n'
        for i in range(k):
            result['text']=result['text']+str(integ(xn[i]))+'; '+str(integ(yn[i]))+'\n'
             
def cleaning():
    global i, x, y
    i,x,y=1,[],[]
    x11.delete(0, END)
    y11.delete(0, END)
    peak.delete(0, END)
    result['text']=''
    label_x11['text']='x1 ='
    label_y11['text']='y1 ='
    peak.focus_set()
def focuspeak(event):
    x11.focus_set()
def focus1(event):
    y11.focus_set()
def focus2(event):
    res()
    x11.delete(0, END)
    y11.delete(0, END)
    x11.focus_set()    
   
from tkinter import *
from tkinter.font import Font
i,x,y=1,[],[]
root = Tk()    
root.title("Leshchenko")
root.configure(bg="#fff04f")
w = 510
h = 550
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
xs = (ws/2) - (w/2)
ys = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, xs, ys))
font_title= Font(family="Century Gothic", size=17, weight="bold", slant="italic")
font_subtitle= Font(family="Century Gothic", size=11)
name = Label(root, text="Домашнє завдання", font = font_title,bg="#fff04f")
name.grid(row=0, column=0,columnspan=6,padx=135, pady=8)
label = Label(root, text='Уведіть кількість та координати точок для побудови\n мінімальної опуклої оболонки, та нажміть на кнопку "Обчислити"', font=font_subtitle,bg="#fff04f")
label.grid(row=1, column=0,columnspan=6, pady=3)

label_pad = Label(root, text='У', font=Font(family="Century Gothic", size=3),bg="#fff04f", fg="#fff04f")
label_pad.grid(row=2, column=0,columnspan=6, pady=1)

label_peak = Label(root, text='Уведіть кількіcть вершин', font=Font(family="Century Gothic", size=11, weight="bold", slant="italic"),bg="#fff04f")
label_peak.grid(row=3, column=0,columnspan=6, pady=2)
peak=Entry(root,font=Font(family="Century Gothic", size=13), justify="center", width=7)
peak.grid(row=4, column=0,columnspan=6, pady=5)
peak.focus_set()
peak.bind('<Return>', focuspeak)

label_pad1 = Label(root, text='У', font=Font(family="Century Gothic", size=3),bg="#fff04f", fg="#fff04f")
label_pad1.grid(row=5, column=0,columnspan=6, pady=2)

label_x11 = Label(root, text='x1 =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="#fff04f")
label_x11.grid(row=6, column=2)
x11=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
x11.grid(row=7, column=2)
x11.bind('<Return>', focus1)

label_y11 = Label(root, text='y1 =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="#fff04f")
label_y11.grid(row=6, column=3)
y11=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
y11.grid(row=7, column=3)
y11.bind('<Return>', focus2)

but1=Button(root,text="Обчислити",width=12,height=1,bg="#d3d3d3",font=Font(family="Century Gothic", size=11), justify="center",  command=res)
but1.grid(row=8, column=2, pady=31)

but2=Button(root,text="Очистити",width=12,height=1,bg="#d3d3d3",font=Font(family="Century Gothic", size=11), justify="center",  command=cleaning)
but2.grid(row=8, column=3, pady=31)

result=Label(root,text="", font=Font(family="Century Gothic", size=15),bg="#fff04f")
result.grid(row=9, column=0, columnspan=6)
root.mainloop()
