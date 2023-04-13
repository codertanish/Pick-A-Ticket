from tkinter import *
import random

root = Tk()
root.title("Random Code Generator")
root.geometry("400x200")
root.configure(bg = "orange2")

label = Label(root, bg = "orange")

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
print(alphabet)

def generateCode():
    r1 = random.randint(0,25)
    r2 = random.randint(0,25)
    r3 = random.randint(0,25)
    r4 = random.randint(0,25)
    r5 = random.randint(0,25)
    a1 = alphabet[r1]
    a2 = alphabet[r2]
    a3 = alphabet[r3]
    a4 = alphabet[r4]
    a5 = alphabet[r5]
    print(type(a1))
    code = a1 + a2 + a3 + a4 + a5
    label['text'] = code


btn = Button(root, text = "Pick A Ticket", command = generateCode)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)


label.place(relx = 0.5, rely = 0.65, anchor = CENTER)





root.mainloop()