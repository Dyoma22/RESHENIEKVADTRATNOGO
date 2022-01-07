from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

def lahenda():    
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        #if type!
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


okno.mainloop()

