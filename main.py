from tkinter import *

class calculadora():
    def telaPrincipal():
        app = Tk()
        app.geometry("300x150")
        app.title("Calculadora Simples")
        fonte = ("Arial", "10")

        n1 = Label(app, text="Número 01:", font=fonte)
        n1.place(x=5, y=10)

        num1 = Entry(app, width=35)
        num1.place(x=75, y=10)

        n2 = Label(app, text="Número 02:", font=fonte)
        n2.place(x=5, y=40)

        num2 = Entry(app, width=35)
        num2.place(x=75, y=40)

        rslt = Label(app, text="Resultado:", font=fonte)
        rslt.place(x=5, y=70)

        def pegarNumeros():
            i1 = num1.get()
            i2 = num2.get()
            
            i1, i2 = float(i1), float(i2)
            return i1, i2

        def soma():
            i1, i2 = pegarNumeros()

            rest = i1 + i2
            rst = Label(app, text=rest, font=fonte)
            rst.place(x=75, y=70)

        def subtracao():
            i1, i2 = pegarNumeros()

            rest = i1 - i2
            rst = Label(app, text=rest, font=fonte)
            rst.place(x=75, y=70)

        def multiplicacao():
            i1, i2 = pegarNumeros()

            rest = i1 * i2
            rst = Label(app, text=rest, font=fonte)
            rst.place(x=75, y=70)
        
        def divisao():
            i1, i2 = pegarNumeros()

            rest = i1 / i2
            rst = Label(app, text=rest, font=fonte)
            rst.place(x=75, y=70)

        def reset():
            rst = Label(app, text="            ", font=fonte)
            rst.place(x=75, y=70)


        fonteBtn = ("Arial Bold", "16")

        btSoma = Button(app, text="+", font=fonteBtn, width=3, command=soma)
        btSoma.place(x=5, y=100)

        btSubt = Button(app, text="-", font=fonteBtn, width=3, command=subtracao)
        btSubt.place(x=55, y=100)

        btMult = Button(app, text="*", font=fonteBtn, width=3, command=multiplicacao)
        btMult.place(x=105, y=100)

        btDivi = Button(app, text="/", font=fonteBtn, width=3, command=divisao)
        btDivi.place(x=155, y=100)

        btC = Button(app, text="C", font=fonteBtn, width=3, command=reset)
        btC.place(x=205, y=100)

        app.mainloop()
        
cl = calculadora
cl.telaPrincipal()