from tkinter import *
import tkinter as tk
from functools import partial



def call_result(l1,l2,l3,l4,l5,lh,lg,n1,n2,n3,n4 , n5):
    num1 = (n1.get())
    num2 = (n2.get())
    num3 = int((n3.get()))
    num4 = int((n4.get()))
    num5 = int((n5.get()))

    hasil = num3 + num4 + num5
    hasil1 = hasil / 3

    if hasil1 >= 80 and hasil1 <= 100 :
        grade = "A"
    elif hasil1 >= 70 and hasil1 <= 79 :
        grade = "B"
    elif hasil1 >= 60 and hasil1 <= 69 :
        grade = "C"
    elif hasil1 >= 50 and hasil1 <= 59 :
        grade = "D"
    else :
        grade = "E"

    l1.config(text="Nama            : %s"%num1)
    l2.config(text="NIM               : %s"%num2)
    l3.config(text="Nilai Tugas   : %s"%num3)
    l4.config(text="Nilai MID      : %s"%num4)
    l5.config(text="Nilai Final     : %s"%num5)
    lh.config(text="Nilai Akhir    : %d"%hasil1)
    lg.config(text="Grade            : %s"%grade)

    return

root = tk.Tk()
root.geometry("500x600")
root.title('Data Nilai')
root.config(bg="blue")

number1 = StringVar()
number2 = StringVar()
number3 = StringVar()
number4 = StringVar()
number5 = StringVar()

labelNum1 = tk.Label(root, text="Nama " , bg="blue").grid(row=2, column=0,sticky=W)
labelNum2 = tk.Label(root, text="NIM " , bg="blue").grid(row=3, column=0,sticky=W)
labelNum3 = tk.Label(root,text="Nilai Tugas " , bg="blue").grid(row=4,column=0,sticky=W)
labelNum4 = tk.Label(root,text="Nilai MID " , bg="blue").grid(row=5,column=0,sticky=W)
labelNum5 = tk.Label(root,text="Nilai Final " , bg="blue").grid(row=6,column=0,sticky=W)

labelResult1= tk.Label(root , bg="blue")
labelResult2= tk.Label(root , bg="blue")
labelResult3= tk.Label(root , bg="blue")
labelResult4= tk.Label(root , bg="blue")
labelResult5= tk.Label(root , bg="blue")
labelHasil = tk.Label(root , bg="blue")
labelGrade = tk.Label(root , bg="blue")

labelResult1.grid(row=19, column=0,sticky=W)
labelResult2.grid(row=20, column=0,sticky=W)
labelResult3.grid(row=21, column=0,sticky=W)
labelResult4.grid(row= 22, column=0,sticky=W)
labelResult5.grid(row=23, column=0,sticky=W)
labelHasil.grid(row=24, column=0 , sticky=W)
labelGrade.grid(row=25 , column=0 , sticky=W)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=2, column=5)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=3, column=5)
entryNum3 = tk.Entry(root, textvariable=number3).grid(row=4, column=5)
entryNum4 = tk.Entry(root, textvariable=number4).grid(row=5, column=5)
entryNum5 = tk.Entry(root, textvariable=number5).grid(row=6, column=5)

'''
labelnama= tk.Label(root, text="Nama : ").grid(row=7, column=0,sticky=W)
labelnim = tk.Label(root, text="Nim : ").grid(row=8, column=0,sticky=W)
labelnt = tk.Label(root, text="Nilai Tugas : ").grid(row=9, column=0,sticky=W)
labelnm = tk.Label(root, text="Nilai MID : ").grid(row=10, column=0,sticky=W)
labelnf = tk.Label(root, text="Nilai FInal : ").grid(row=11, column=0,sticky=W)
'''



call_result = partial(call_result, labelResult1,labelResult2,labelResult3,labelResult4,labelResult5, labelHasil , labelGrade ,number1, number2,number3 , number4,number5)

buttonCal = tk.Button(root, text="Show", command=call_result , bg= "orange" , width=20).grid(row=15, column=4)

root.mainloop()