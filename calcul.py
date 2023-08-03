from tkinter import *

fen = Tk()
fen.title("Calculator")
fen.geometry("400x500")

glas = Label(fen, text="", font=("arial", 15))
glas.grid(row=1, column=0, padx=25, pady=25)

def quitter():
    fen.quit()
def zero():
    glas.configure(text="")
def nu9():
    glas = Label(fen, text="9", font=("arial", 15))
    glas.configure(text="9")  
def nu8():
    glas.configure(text="8") 
def nu7():
    glas.configure(text="7")
def nu6():
    glas.configure(text="6")
def nu5():
    glas.configure(text="5")
def nu4():
    glas.configure(text="4")
def nu3():
    glas.configure(text="3")
def nu2():
    glas.configure(text="2")
def nu1():
    glas.configure(text="1")
def nu0():
    glas.configure(text="0")
def nuE():
    glas.configure(text="=")
def nuV():
    glas.configure(text=",")
def nuMo():
    glas.configure(text="-")
def nuP():
    glas.configure(text="+")
def nuM():
    glas.configure(text="*")
def nuD():
    glas.configure(text="/")
  
    
btn0 = Button(fen, text="0", width=10, command=nu0)
btn1 = Button(fen, text="1", width=10, command=nu1)
btn2 = Button(fen, text="2", width=10, command=nu2)
btn3 = Button(fen, text="3", width=10, command=nu3)
btn4 = Button(fen, text="4", width=10, command=nu4)
btn5 = Button(fen, text="5", width=10, command=nu5)
btn6 = Button(fen, text="6", width=10, command=nu6)
btn7 = Button(fen, text="7", width=10, command=nu7)
btn8 = Button(fen, text="8", width=10, command=nu8)
btn9 = Button(fen, text="9", width=10, command=nu9)
btnMo = Button(fen, text="-", width=10, bg="orange", command=nuMo)
btnP = Button(fen, text="+", width=10, bg="orange", command=nuP)
btnM = Button(fen, text="x", width=10, bg="orange", command=nuM)
btnD = Button(fen, text="/", width=10, bg="orange", command=nuD)
btnV = Button(fen, text=",", width=10, command=nuV)

btnAc = Button(fen, text="AC", width=22, command=zero)
btnOff = Button(fen, text="Off", width=22, command=quitter)
btnEg = Button(fen, text="=", width=10, bg="orange", command=nuE)

btnAc.grid(row=2, column=0, padx=5, pady=10, columnspan=2)
btnOff.grid(row=2, column=2, padx=5, pady=10, columnspan=2)
btn9.grid(row=3, column=2, padx=5, pady=10)
btn8.grid(row=3, column=1, padx=5, pady=10)
btn7.grid(row=3, column=0, padx=5, pady=10)
btn6.grid(row=4, column=2, padx=5, pady=10)
btn5.grid(row=4, column=1, padx=5, pady=10)
btn4.grid(row=4, column=0, padx=5, pady=10)
btn3.grid(row=5, column=2, padx=5, pady=10)
btn2.grid(row=5, column=1, padx=5, pady=10)
btn1.grid(row=5, column=0, padx=5, pady=10)
btn0.grid(row=6, column=1, padx=5, pady=10)
btnEg.grid(row=6, column=2, padx=5, pady=10)
btnV.grid(row=6, column=0, padx=5, pady=10)
btnP.grid(row=3, column=3, padx=15, pady=10)
btnMo.grid(row=4, column=3, padx=15, pady=10)
btnM.grid(row=5, column=3, padx=15, pady=10)
btnD.grid(row=6, column=3, padx=15, pady=10)



fen.mainloop()