import math 
from tkinter import *
def soma():
    if(str(espaco.get()).isnumeric() or str(espaco2.get()) .isnumeric()):
        x = float(espaco.get())
        y = float(espaco2.get())
        lb_resultado1["text"] = x+y 
def sub():
     if(str(espaco.get()).isnumeric() or str(espaco2.get()) .isnumeric()):
        x = float(espaco.get())
        y = float(espaco2.get())
        lb_resultado1["text"] = x-y
def multi():
    if(str(espaco.get()).isnumeric() or str(espaco2.get()) .isnumeric()):
        x = float(espaco.get())
        y = float(espaco2.get())
        lb_resultado1["text"] = x*y
def div():
     if(str(espaco.get()).isnumeric() or str(espaco2.get()) .isnumeric()):
        x = float(espaco.get())
        y = float(espaco2.get())
        lb_resultado1["text"] = x/y
def pot():
    if(str(espaco.get().isnumeric() or str(espaco2.get()).isnumeric())):
        x = float(espaco.get())
        y = float(espaco2.get())
        lb_resultado1["text"] = x ** y
def zerar():
    lb_resultado1["text"] = "0"
def factorial():
    if(str(espaco.get().isnumeric() or str(espaco2.get()).isnumeric())):
        x = int(espaco.get())
        lb_resultado1["text"] = math.factorial(x)
def sqrt():
    if(str(espaco.get().isnumeric() or str(espaco2.get()).isnumeric())):
        x = float(espaco.get())
        lb_resultado1["text"] = math.sqrt(x)

begin = Tk()
begin.title('Calculadora')
begin["bg"] = "grey"
        
lb = Label(begin, text = 'Operações:')
lb.place(x=220, y=90)
#botões das operações.     
btsoma = Button(begin, width = 10, text = '+', command = soma)
btsoma.place(x=220, y=120)
        
btsub = Button(begin, width = 10, text = '-', command = sub)
btsub.place(x=220, y=150)
        
btmulti = Button(begin, width = 10, text = '*', command = multi)
btmulti.place(x=220, y=180)
        
btdiv = Button(begin, width = 10, text = '/', command = div)
btdiv.place(x=220, y=210)

btpot = Button(begin, width = 10, text ='Potencia', command = pot)
btpot.place(x=220,y=240)

btzerar = Button(begin, width = 15, text = 'Zerar o Resultado', command = zerar)
btzerar.place(x=220,y=270)

btfactorial = Button(begin, width = 10, text ='Factorial', command = factorial)
btfactorial.place(x=310,y=120)

btsqrt = Button(begin, width = 10, text = 'Raiz quadrada', command = sqrt)
btsqrt.place(x=310,y=150)
#Descrevendo os locas para colocar os numeros.
lb_espaco = Label(begin, text='Coloque o primeiro numero no espaço:')
lb_espaco.place(x=0,y=120)
lb_espaco2 = Label(begin, text='Coloque o segundo numero no espaço:')
lb_espaco2.place(x=0,y=180)
#Descrevendo as Operações Basicas.
lbcalcul1 = Label(begin, text='Operações basicas', bg='white')
lbcalcul1.pack(side=TOP, fill=X)
#Resultado
lb_resultado = Label(begin, text='Resultado é :')
lb_resultado1 = Label(begin, text='x')
lb_resultado.place(x=0,y=240)
lb_resultado1.place(x=80,y=240)
#Codigo da onde os numeros são inseridos.
espaco = Entry(begin)
espaco.place(x=0,y=150)
espaco2 = Entry(begin)
espaco2.place(x=0, y=210)
        
begin.geometry("1024x768")
begin.mainloop()
