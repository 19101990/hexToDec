from tkinter import *
import tkinter.messagebox

root = Tk()
decVal = StringVar()

def fromHexToDec():
    global decVal
    spin1 = sb1.get()
    spin2 = sb2.get()
    spin3 = sb3.get()
    spin4 = sb4.get()

    hexVal = spin1+spin2+spin3+spin4
    decVal.set(int(hexVal, 16))



# ===== WIDGETS ===== #
sb1 = Spinbox(root, values=("0","1","2","3","4","5","6","7","8",
                            "9","A","B","C","D","E","F"), width=10, command=fromHexToDec)
sb1.grid(row=0, column=0)
sb2 = Spinbox(root, values=("0","1","2","3","4","5","6","7","8",
                            "9","A","B","C","D","E","F"), width=10, command=fromHexToDec)
sb2.grid(row=0, column=1)
sb3 = Spinbox(root, values=("0","1","2","3","4","5","6","7","8",
                            "9","A","B","C","D","E","F"), width=10, command=fromHexToDec)
sb3.grid(row=0, column=2)
sb4 = Spinbox(root, values=("0","1","2","3","4","5","6","7","8",
                            "9","A","B","C","D","E","F"), width=10, command=fromHexToDec)
sb4.grid(row=0, column=3)
entry = Entry(root, width=30, textvariable=decVal, justify=RIGHT)
entry.grid(row=1, column=0, columnspan=4)
entry.insert(0, "0")
entry.config(state='readonly')



root.mainloop()
