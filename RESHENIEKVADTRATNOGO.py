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
t=0
def veel():
    global t
    if t==0:
        aken.geometry(str(aken.winfo_width()))+"x"+str(aken.winfo_height()+200)
        veel1.config(text="Увеличить окно")
        t=1
    else:
        aken.geometry(str(aken.winfo_width()))+"x"+str(aken.winfo_height()-200)
        veel1.config(text="Увеличить окно")
        t=0
def kala():
    x1=np.arange(0,9,0.5)#min max step
    y1=(2/27)*x1*x1-3
    x2=np.arange(-10,0,0.5)#min max step
    y2=0.04*x1*x1-3
    fig=plt.figure()
    plt.plot(x1, y1,x2, y2, 'r-d')
    plt.title('Квадратное уравнение')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def kqt():
    x1=np.arange(0,9,0.5)
    y1=(2/27)*x1*x1-3
    x2=np.arange(-10,0,0.5)
    y2=0.04*x2*x2-3
    x3=np.arange(-9,-3,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3,9,0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=np.arange(5,8.3,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5,8.5,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=np.arange(-13,-9,0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8=np.arange(-15,-10,0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15,-10,0.5)
    y9=1
    x10=np.arange(3,4,0.5)
    y10=3
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title('Кит')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def zontik():
    x1=np.arange(-12,12,0.5)
    y1=(-1/18)*x1*x1+12
    x2=np.arange(-4,4,0.5)
    y2=(-1/8)*x2*x2+6
    x3=np.arange(-12,-4,0.5)
    y3=(-1/8)*(x3+8)**2+6
    x4=np.arange(4,12,0.5)
    y4=(-1/8)*(x4-8)**2+6
    x5=np.arange(-4,-0.3,0.5)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4,0.2,0.5)
    y6=1.5*(x6+3)**2-10
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title('Зонтик')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

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
buttonveel=Button(okno,text="Увеличить окно",font="Arial 20",bg="white",command=veel)
buttonveel.pack(side=TOP)
kalchik=Radiobutton(okno,text="Рыба",font="Arial 20",bg="white",command=kala)
kalchik.pack(side=TOP)
kiit=Radiobutton(okno,text="Кит",font="Arial 20",bg="white",command=kqt)
kiit.pack(side=TOP)
zontikkk=Radiobutton(okno,text="Зонтик",font="Arial 20", fg="white",command=zontik)
zontikkk.pack(side=TOP)
#knopka1.bind("<Button-1>",lahenda)
okno.mainloop()

 