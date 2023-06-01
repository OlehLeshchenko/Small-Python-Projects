def click1():
    import tkinter as tk
    from tkinter import ttk
    from textwrap import wrap
    def clickR():
        for i in range(2):
            if box.current()==0:
                text="Мікро. Мікроземлетруси, не відчуваються."
                Result.config(fg="#219c33")
            elif box.current()==1:
                text="Дуже слабкі. Як правило не відчуваються, але реєструються."
                Result.config(fg="#219c33")
            elif box.current()==2:
                text="Слабкі. Часто відчуваються, дуже рідко завдають шкоди."
                Result.config(fg="#219c33")
            elif box.current()==3:
                text="Легкі. Відчутне тремтіння речей всередині будинків, значна шкода малоймовірна."
                Result.config(fg="#d4bd28")
            elif box.current()==4:
                Result.config(fg="#d4bd28")
                text="Помірні. Може завдати значної шкоди старим та погано сконструйованим будівлям на незначній території. Щонайбільше, незначні пошкодження добре спроектованим будівлям."
            elif box.current()==5:
                text="Сильні. Може спричинити руйнацію на території до 150 км довжиною/шириною в населених регіонах."
                Result.config(fg="#d42828")
            elif box.current()==6:
                text="Дуже сильні. Значна руйнація на значній території."
                Result.config(fg="#d42828")
            elif box.current()==7:
                text="Великі. Серйозна руйнація на територіях довжиною/шириною в сотні кілометрів."
                Result.config(fg="#d42828")
            elif box.current()==8:
                text="Рідкісно великі. Останній такий землетрус відбувся 22 травня 1960 року."
                Result.config(fg="#d42828")
            root1.update()
            if Result.winfo_width() > root1.winfo_width():
                average_char_width = Result.winfo_width() / len(text)
                chars_per_line = int(root1.winfo_width() / average_char_width)
                while Result.winfo_width() > root1.winfo_width():  
                    wrapped_text = '\n'.join(wrap(text, chars_per_line))
                    Result['text'] = wrapped_text
                    root1.update()
                    chars_per_line -= 1
            else:
                Result['text'] = text
    def clickC():
        box.current(0)
        Result['text']=""
    root1= Tk()    
    root1.title("Шкала Ріхтера")
    root1.configure(bg="#1c436b")
    my_font1= Font(root1 ,family="Comic Sans MS", size=20)
    my_font2= Font(root1 ,family="Trebuchet MS", size=15)
    w = 500
    h = 350
    ws = root1.winfo_screenwidth()
    hs = root1.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root1.geometry('%dx%d+%d+%d' % (w, h, x, y))
    name = Label(root1, text="Шкала Ріхтера",bg="#1c436b", font=my_font1, fg="#FFFFFF")
    name.grid(row=0, column=0,columnspan=4,padx=160, pady=10)
    label = Label(root1, text='Оберіть значення:', font=my_font2,bg="#1c436b", fg="#FFFFFF")
    label.grid(row=1, column=0, padx=40)
    box = ttk.Combobox(root1, values=["Менше 2,0","2,0-2,9","3,0-3,9","4,0-4,9","5,0-5,9","6,0-6,9","7,0-7,9","8,0-8,9","9,0 чи більше"], state="readonly", font=my_font2, width=13)
    box.current(0)
    box.grid(row=1, column=1)
    Result = Label(root1, text='', font=my_font2,bg="#1c436b", fg="#FFFFFF")
    Result.grid(row=3, column=0, columnspan=4, pady=20)
    but=Button(root1,text="Дізнатися",width=16,height=2,bg="#d3d3d3",font="vernada 10", justify="center", command=clickR)
    but.grid(row=4, column=0, padx=40, pady=40)
    text = Result['text']
    but=Button(root1,text="Очистити поле ",width=16,height=2,bg="#d3d3d3",font="vernada 10", justify="center", command=clickC)
    but.grid(row=4, column=1, pady=40)
    root1.mainloop()
def click2():
    import tkinter as tk
    from tkinter import ttk
    from textwrap import wrap
    def clickR():
        for i in range(2):
            if box.current()==0:
                text="Невідчутний, Не відчувається. Визначається і фіксується лише сейсмічними приладами."
                Result.config(fg="#219c33")
            elif box.current()==1:
                text="Ледь відчутний. Відчувається лише окремими людьми, що перебувають у стані повного спокою на верхніх поверхах будівель, і дуже чутливими домашніми тваринами. Фіксується сейсмічними приладами."
                Result.config(fg="#219c33")
            elif box.current()==2:
                text="Слабкий. Відчувається у приміщеннях окремими людьми. Люди, що перебувають у приміщенні, відчувають розгойдування та легке тремтіння."
                Result.config(fg="#219c33")
            elif box.current()==3:
                text="Відчутний для загалу. Розпізнається за легким брязкотом та коливанням предметів, посуду і шибок, скрипом дверей та стін. Всередині будівлі струшування відчуває більшість людей."
                Result.config(fg="#219c33")
            elif box.current()==4:
                Result.config(fg="#d4bd28")
                text="Сильний. Більшість відчуває землетрус усередині будівлі, зовні землетрус відчувають не всі. Більшість сплячих — просинаються. Дехто вибігає з приміщення надвір. Будівлі зазнають легких струсів по всій поверхні. Підвішені предмети помітно гойдаються. Скляні, фарфорові вироби дзеленчать, ударяючись одне об одне. Вібрації значні. Об'єкти з високо розташованим центром ваги падають. Двері та вікна відчиняються і зачиняються."
            elif box.current()==5:
                text="Легкі пошкодження. Основна маса людей відчувають землетрус усередині будівлі. Люди налякані та вибігають геть із будівель. Невеликі предмети падають. Легкі пошкодження у більшості звичайних будівель; наприклад, тонкі тріщини у штукатурці, невеликі кавалки відколюються."
                Result.config(fg="#d4bd28")
            elif box.current()==6:
                text="Пошкодження. Переважна більшість людей налякані і вибігають з будівель. Меблі зсуваються, більшість предметів падає з полиць. Багато будівель зазнають помірних пошкоджень: невеликі тріщини у стінах; частина димових труб розвалюється."
                Result.config(fg="#d4bd28")
            elif box.current()==7:
                text="Важкі пошкодження. Перекинуті меблі. Більшість будівель зазнали значних пошкоджень: димові труби падають; великі тріщини у стінах; деякі будівлі можуть частково зруйнуватись."
                Result.config(fg="#d4bd28")
            elif box.current()==8:
                text="Руйнівний. Пам'ятники і колони падають. Багато будівель частково зруйновані, деякі — повністю."
                Result.config(fg="#d42828")
            elif box.current()==9:
                text="Дуже руйнівний. Більшість будівель повністю зруйновані."
                Result.config(fg="#d42828")
            elif box.current()==10:
                text="Спустошувальний. Практично усі будівлі повністю зруйновані."
                Result.config(fg="#d42828")
            elif box.current()==11:
                text="Усе цілком знищено. Практично усі наземні і підземні структури дуже сильно пошкоджені чи повністю зруйновані."
                Result.config(fg="#d42828")
            root2.update()
            if Result.winfo_width() > root2.winfo_width():
                average_char_width = Result.winfo_width() / len(text)
                chars_per_line = int(root2.winfo_width() / average_char_width)
                while Result.winfo_width() > root2.winfo_width():  
                    wrapped_text = '\n'.join(wrap(text, chars_per_line))
                    Result['text'] = wrapped_text
                    root2.update()
                    chars_per_line -= 1
            else:
                Result['text'] = text
    def clickC():
        box.current(0)
        Result['text']=""
    root2= Tk()    
    root2.title("ЄМ шкала")
    root2.configure(bg="#631c6b")
    my_font1= Font(root2 ,family="Comic Sans MS", size=20)
    my_font2= Font(root2 ,family="Trebuchet MS", size=15)
    w = 500
    h = 500
    ws = root2.winfo_screenwidth()
    hs = root2.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root2.geometry('%dx%d+%d+%d' % (w, h, x, y))
    name = Label(root2, text="Європейська\n макросейсмічна шкала",bg="#631c6b", font=my_font1, fg="#FFFFFF")
    name.grid(row=0, column=0,columnspan=4,padx=100, pady=10)
    label = Label(root2, text='Оберіть значення:', font=my_font2,bg="#631c6b", fg="#FFFFFF")
    label.grid(row=1, column=0, padx=40)
    box = ttk.Combobox(root2, values=["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"], state="readonly", font=my_font2, width=13)
    box.current(0)
    box.grid(row=1, column=1)
    Result = Label(root2, text='', font=my_font2,bg="#631c6b", fg="#FFFFFF")
    Result.grid(row=3, column=0, columnspan=4, pady=20)
    but=Button(root2,text="Дізнатися",width=16,height=2,bg="#d3d3d3",font="vernada 10", justify="center", command=clickR)
    but.grid(row=4, column=0, padx=40, pady=20)
    text = Result['text']
    but=Button(root2,text="Очистити поле ",width=16,height=2,bg="#d3d3d3",font="vernada 10", justify="center", command=clickC)
    but.grid(row=4, column=1, pady=20)
    root2.mainloop()
from tkinter import *
from tkinter.font import Font
root= Tk()    
root.title("Характеристики землетрусів")
root.configure(bg="#202028")
w = 360
h = 250
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

my_font= Font(family="Times New Roman", size=16)
my_font1= Font(family="Comic Sans MS", size=12)
name = Label(text='Характеристики землетрусів',font=my_font,bg="#202028", fg="White")
name.grid(row=0, column=0, columnspan=10, pady=20,padx=52)
but1=Button(text="Дізнатися за шкалою Ріхтера",width=33,height=1,bg="#d3d3d3",font=my_font1, justify="center", command=click1)
but1.grid(row=1, column=0,columnspan=10, pady=5 )
but2=Button(text="Дізнатися за шкалою Європейською\n макросейсмічною шкалою",width=33,height=2 ,bg="#d3d3d3",font=my_font1, justify="center", command=click2)
but2.grid(row=2, column=0,columnspan=10, pady=5 )
root.mainloop()
