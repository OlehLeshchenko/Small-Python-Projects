def clickRoot(mas):
    root1= Tk()    
    root1.title("Помилка")
    root1.configure(bg="#a1a1a1")
    w = 500
    h = 210
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root1.geometry('%dx%d+%d+%d' % (w, h, x, y))
    name = Label(root1, text="Помилка!!!", font="vernada 18",bg="#a1a1a1", fg="#ff4e4e")
    name.grid(row=0, column=0,columnspan=10,padx=180, pady=20)
    label = Label(root1, text='', font="12",bg="#a1a1a1")
    label['text']='Вихідне число є некоректним записом для системи з основою '+str(box1.current()+2)+'.\n У '+str(box1.current()+2)+'-ій системі допустимі \n тільки такі символи: '+", ".join(mas)
    label.grid(row=1, column=0,columnspan=10)
    root1.mainloop()
    entry1.focus_set()
def callback2(event):
    def again():
        idd=len(list(str(entry1.get())))-1
        n="".join(list(str(entry1.get()))[:idd])
        entry1.delete(0, END)
        entry1.insert(END, n)
    er=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    er2=["a","b","c","d","e","f"]
    for element in list(str(entry1.get())):
        if box1.current()+2==2:
            if element not in er[:2]: 
                clickRoot(er[:2])
        elif box1.current()+2==3:
            if element not in er[:3]: 
                again()
                clickRoot(er[:3])
        elif box1.current()+2==4:
            if element not in er[:4]: 
                again()
                clickRoot(er[:4])
        elif box1.current()+2==5:
            if element not in er[:5]: 
                again()
                clickRoot(er[:5])
        elif box1.current()+2==6:
            if element not in er[:6]: 
                again()
                clickRoot(er[:6])
        elif box1.current()+2==7:
            if element not in er[:7]: 
                again()
                clickRoot(er[:7])
        elif box1.current()+2==8:
            if element not in er[:8]: 
                again()
                clickRoot(er[:8])
        elif box1.current()+2==9:
            if element not in er[:9]: 
                again()
                clickRoot(er[:9])
        elif box1.current()+2==10:
            if element not in er[:10]:
                again()
                clickRoot(er[:10])
        elif box1.current()+2==11:
            if element not in er[:11]+er2[:1]: 
                again()
                clickRoot(er[:11])
        elif box1.current()+2==12:
            if element not in er[:12]+er2[:2]: 
                again()
                clickRoot(er[:12])
        elif box1.current()+2==13:
            if element not in er[:13]+er2[:3]: 
                again()
                clickRoot(er[:13])
        elif box1.current()+2==14:
            if element not in er[:14]+er2[:4]: 
                again()
                clickRoot(er[:14])
        elif box1.current()+2==15:
            if element not in er[:15]+er2[:5]: 
                again()
                clickRoot(er[:15])
        else:
            if element not in er[:16]+er2[:6]: 
                again()
                clickRoot(er[:16])
def callback(event):       
    if 2<=box1.current()+2<=4:
        root.configure(bg="PaleGreen3")
        name.config(**{"bg": "PaleGreen3"})
    elif 4<box1.current()+2<=8:
        root.configure(bg="#62639B")
        name.config(**{"bg": "#62639B"})
    elif 8<box1.current()+2<=12:
        root.configure(bg="#F39F18")
        name.config(**{"bg": "#F39F18"})
    elif 12<box1.current()+2<=16:
        root.configure(bg="#ABCDEF")
        name.config(**{"bg": "#ABCDEF"})
def click(event):
    if box1.current()+2<=10 and box1.current()+2<=10:
        number=int(entry1.get())
        a,mas=0,list(str(number))
        dil=box1.current()+2
        for i in range(len(mas)) :
            a=a*dil +int(mas[i])
        dil=box2.current()+2
        mas=[]
        while a!=0:
            per=a%dil
            mas.insert(0, str(per))
            a=a//dil
    else:
        m=["10","11","12","13","14","15"]
        mm=["A","B","C","D","E","F"]
        dil=box1.current()+2
        number=entry1.get()
        a,mas=0,list(number)
        for i in mas:
            if i.isdigit()==False: mas[mas.index(i)]=i.upper()
        for i in mas:
            if i in mm: mas[mas.index(i)]=m[mm.index(i)]
        for i in range(len(mas)) :
            a=a*dil +int(mas[i])
        dil=box2.current()+2
        mas=[]
        while a!=0:
            p=a%dil
            for i in [10,11,12,13,14,15]:
                if p==i:
                    p=mm[i-10]
            mas.insert(0, str(p))
            a=a//dil
    entry2['text']=''.join(mas)
from tkinter import *
from tkinter.font import Font
import tkinter as tk
from tkinter import ttk
root= Tk()    
root.title("Системи числення")
root.configure(bg="#983b45")
my_font1= Font(root ,family="Comic Sans MS", size=20)
my_font2= Font(root ,family="Trebuchet MS", size=15)
w = 530
h = 360
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
name = Label(root, text="Переведення чисел в різні \nсистеми числення",bg="#983b45", font=my_font1, fg="#FFFFFF")
name.grid(row=0, column=0,columnspan=3,padx=87, pady=30)
box1 = ttk.Combobox(root, values=["2-кова","3-кова","4-кова","5-кова","6-кова","7-кова","8-кова","9-кова","10-кова","11-кова","12-кова","13-кова","14-кова","15-кова","16-кова"], state="readonly", font=my_font2, width=10)
box1.current(8)
box1.grid(row=1, column=0, padx=60)
box1.bind("<<ComboboxSelected>>", callback)
box2 = ttk.Combobox(root, values=["2-кова","3-кова","4-кова","5-кова","6-кова","7-кова","8-кова","9-кова","10-кова","11-кова","12-кова","13-кова","14-кова","15-кова","16-кова"], state="readonly", font=my_font2, width=10)
box2.current(0)
box2.grid(row=1, column=1)
event=0
var = StringVar()
entry1 = Entry(root, font=my_font2, width=12, textvariable=var)
entry1.grid(row=2, column=0, padx=60, pady=20)
entry1.focus_set()
entry1.bind("<KeyRelease>", callback2)
entry2 = Label(root, font=my_font2, width=11, bg="#FFFFFF", fg="black", text="")
entry2.grid(row=2, column=1)
but=Button(root,text="Обчислити",width=16,height=2,bg="#d3d3d3",font="vernada 10", justify="center", command= lambda: click(0))
entry1.bind("<Return>", click)
but.grid(row=3, column=0, columnspan=3, pady=20)
root.mainloop()
