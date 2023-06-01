def res():
    global i, x, y
    top=int(peak.get())
    if i<=top:
        i+=1
        if i<top+1:
            label_x1['text']='x'+str(i)+' ='
            label_y1['text']='y'+str(i)+' ='
        x.append(float(x1.get()))
        y.append(float(y1.get()))
    if i==top+1:
        s2=0
        for k in range(top):
            if k==0:
                s1=(x[0])*(y[1]-y[top-1])
            elif k>0 and k<top-1:
                summ=(x[k])*(y[k+1]-y[k-1])
                s2+=summ
            else:
                s3=(x[top-1])*(y[0]-y[top-2])
        s=abs(s1+s2+s3)/2
        result['text']='Площа многокутника дорівнює: '+str(s)       
def cleaning():
    global i, x, y
    i,x,y=1,[],[]
    x1.delete(0, END)
    y1.delete(0, END)
    peak.delete(0, END)
    result['text']=''
    label_x1['text']='x1 ='
    label_y1['text']='y1 ='
    peak.focus_set()
def focuspeak(event):
    x1.focus_set()
def focus1(event):
    y1.focus_set()
def focus2(event):
    res()
    x1.delete(0, END)
    y1.delete(0, END)
    x1.focus_set()    
   
from tkinter import *
from tkinter.font import Font
i,x,y=1,[],[]
root = Tk()    
root.title("Leshchenko")
root.configure(bg="#4682B4")
w = 510
h = 450
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
xs = (ws/2) - (w/2)
ys = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, xs, ys))
font_title= Font(family="Century Gothic", size=17, weight="bold", slant="italic")
font_subtitle= Font(family="Century Gothic", size=11)
name = Label(root, text="Домашнє завдання", font = font_title,bg="#4682B4")
name.grid(row=0, column=0,columnspan=6,padx=135, pady=8)
label = Label(root, text='Уведіть кількість та координати вершин многокутника,\n які задані в порядку обходу, та нажміть на кнопку "Обчислити",\n щоб дізнатися площу', font=font_subtitle,bg="#4682B4")
label.grid(row=1, column=0,columnspan=6, pady=3)

label_pad = Label(root, text='У', font=Font(family="Century Gothic", size=3),bg="#4682B4", fg="#4682B4")
label_pad.grid(row=2, column=0,columnspan=6, pady=1)

label_peak = Label(root, text='Уведіть кількіcть вершин', font=Font(family="Century Gothic", size=11, weight="bold", slant="italic"),bg="#4682B4")
label_peak.grid(row=3, column=0,columnspan=6, pady=2)
peak=Entry(root,font=Font(family="Century Gothic", size=13), justify="center", width=7)
peak.grid(row=4, column=0,columnspan=6, pady=5)
peak.focus_set()
peak.bind('<Return>', focuspeak)

label_pad1 = Label(root, text='У', font=Font(family="Century Gothic", size=3),bg="#4682B4", fg="#4682B4")
label_pad1.grid(row=5, column=0,columnspan=6, pady=2)

label_x1 = Label(root, text='x1 =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="#4682B4")
label_x1.grid(row=6, column=2)
x1=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
x1.grid(row=7, column=2)
x1.bind('<Return>', focus1)

label_y1 = Label(root, text='y1 =', font=Font(family="Century Gothic", size=13, weight="bold"), bg="#4682B4")
label_y1.grid(row=6, column=3)
y1=Entry(root,font=Font(family="Century Gothic", size=13), justify="left", width=7)
y1.grid(row=7, column=3)
y1.bind('<Return>', focus2)

but1=Button(root,text="Обчислити",width=12,height=1,bg="#d3d3d3",font=Font(family="Century Gothic", size=11), justify="center",  command=res)
but1.grid(row=8, column=2, pady=31)

but2=Button(root,text="Очистити",width=12,height=1,bg="#d3d3d3",font=Font(family="Century Gothic", size=11), justify="center",  command=cleaning)
but2.grid(row=8, column=3, pady=31)

result=Label(root,text="", font=Font(family="Century Gothic", size=15),bg="#4682B4")
result.grid(row=9, column=0, columnspan=6)
root.mainloop()
