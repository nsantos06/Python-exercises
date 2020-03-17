from tkinter import *

principal = Tk()
principal.title("Calculadora de IMC")
principal.configure(background = 'grey')

#função para calcular o imc
def imc():
    if(str(peso.get()).isnumeric() or str(altura.get()) .isnumeric()):
        x = float(peso.get())
        y = float(altura.get())
        z = float(x/(y**2))
        resultado["text"] = z
        if z < 18.5:
            resultado2["text"] = 'Abaixo do peso'
        elif z > 18.5 and z < 24.9:
            resultado2["text"] = 'Peso Normal' 
        elif z > 25 and z < 29.9:
            resultado2["text"] = 'Sobrepeso'
        elif z > 30 and z < 34.9:
            resultado2["text"]= 'Obesidade grau 1',
        elif z > 35 and z < 39.9:
            resultado2["text"] = 'Obesidade grau 2'
        elif z > 40:
            resultado2["text"] = 'Obesidade grau 3' 

def zerar():
    resultado["text"] = 'IMC Resetado!'
    resultado2["text"] = 'Grau Resetado!'

#peso
peso = Label(principal, width = 10, text = 'Peso')
peso.place(x=0,y=150)
#colocar o peso
peso = Entry(principal)
peso.place(x=0,y=180)
#altura
altura = Label(principal, width = 10, text = 'Altura')
altura.place(x=0, y=210)
#colocar a altura
altura = Entry(principal)
altura.place(x=0,y=240)
#botão calcular imc
calculo = Button(principal, width = 10, text = 'Calcular IMC', command = imc )
calculo.place(x=0,y=270)
 
#resultado do calculo
resultado = Label(principal, width = 20, text = 'Resultado Irá aparecer aqui')
resultado.place(x=0,y=310)

resultado2 = Label(principal, width = 20 , text = 'Grau vai aparecer aqui')
resultado2.place(x=0, y=340)

zero = Button(principal, width = 15, text = 'Zerar', command = zerar)
zero.place(x=130, y=270)

principal.geometry("800x600")
principal.mainloop()
