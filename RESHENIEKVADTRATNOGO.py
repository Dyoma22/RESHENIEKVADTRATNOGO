from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
global D,t
D=-1
t="Нет решений!"
def lahenda(): 
    global D,t
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        if (float(a.get())==0 and float(b.get())==0 and float(c.get())==0):
            vastus.configure(text=f"Все 3 аргумента не могут быть 0")
            a.configure(bg="red")
            b.configure(bg="red")
            c.configure(bg="red")
            graf=False
        elif (a.get()==0 and b.get()==0 and c.get()==0):
            vastus.configure(text=f"Тут не может быть 0")
            a.configure(bg="red")
            graf=False
        elif (a.get()==0 and b.get()==0 and c.get()==0):
            a_=float(a.get())
            b_=float(b.get())
            c_=float(c.get())
            D=b_*b_-4*a_*c_
            if D>0:
                x1_=round((-1*b_+sqrt(D))/(2*a_),2)
                x2_=round((-1*b_+sqrt(D))/(2*a_),2)
                t=f"X1={x1_}, \nX2={x2_}"
                graf=True
        elif D==0:
            x1_round((-1*b_)/(2*a),2)
            t=f"X1={x1_}"
            graf=True
        else:
            t="Нету корней"
            graf=False
            vastus.configure(text=f"D={D}\n{t}")
            a.configure(bg="white")
            b.configure(bg="white")
            c.configure(bg="white")
    else:        
         if a.get()=="":
            a.configure(bg="grey")
         if b.get()=="":
            b.configure(bg="grey")
         if c.get()=="":
            c.configure(bg="grey")
    return graf,D,t
def graafik():
    graf,D,t=lahenda()
    if graf==True:
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x=np.arange(x0-10, x0+10, 0.5)
        y=a_*x*x+b_*x+c_
        fig=plt.figure()
        plt.plot(x, y,'b:o', x0, y0, 'r-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    vastus.configure(text=f"D={D}\n{t}\n{text}")
okno=Tk()
okno.geometry("1000x600")
okno.title("Квадратные уравнения")
lbl=Label(okno,text="Квадратное уравнение",font="Arial 20", fg="black",bg="grey")
lbl.pack()
vastus=Label(okno,text="Решение", height=4,width=60,bg="grey")
vastus.pack(side=BOTTOM)
a=Entry(okno,font="Arial 20", fg="black",bg="white",width=3)
a.pack(side=LEFT)
x2=Label(okno,text="x**2+",font="Arial 20", fg="black", padx=10)
x2.pack(side=LEFT)
b=Entry(okno,font="Arial 26", fg="black",bg="white",width=3)
b.pack(side=LEFT)
x=Label(okno,text="x+",font="Arial 20", fg="black")
x.pack(side=LEFT)
c=Entry(okno,font="Arial 20", fg="black",bg="white",width=3)
c.pack(side=LEFT)
y=Label(okno,text="=0",font="Arial 20", fg="black")
y.pack(side=LEFT)

knopka=Button(okno,text="Решить", font="Arial 20",bg="white",command=lahenda)
knopka.pack(side=LEFT)
knopka1=Button(okno,text="График", font="Arial 20",bg="white",command=graafik)
knopka1.pack(side=LEFT)
#knopka1.bind("<Button-1>",lahenda)

okno.mainloop()

