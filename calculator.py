import tkinter as tk

win = tk.Tk()
win.title("Calculator")
win.geometry("300x350")

entry = tk.Entry(win, width=40)
entry.pack(pady=10)


buttoframe = tk.Frame(win)
buttoframe.columnconfigure(0,weight=1)
buttoframe.columnconfigure(1,weight=1)
buttoframe.columnconfigure(2,weight=1)
buttoframe.columnconfigure(3,weight=1)


def update_text(button):
    button_text = button.cget("text") 
    Ans = None
    if button_text == "=":
        Ans = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END,Ans)
    else:

        entry.insert(tk.END, button_text)


def delete():
    entry.delete(0, tk.END)
    

btn1 = tk.Button(buttoframe, text = "1", font =('Arial', 18),command=lambda: update_text(btn1))
btn1.grid(row = 0,column= 0, sticky=tk.W+tk.E)


btn2 = tk.Button(buttoframe, text = "2", font =('Arial', 18),command=lambda: update_text(btn2))
btn2.grid(row = 0,column= 1, sticky=tk.W+tk.E)


btn3 = tk.Button(buttoframe, text = "3", font =('Arial', 18),command=lambda: update_text(btn3))
btn3.grid(row = 0,column= 2, sticky=tk.W+tk.E)


btn4 = tk.Button(buttoframe, text = "4", font =('Arial', 18),command=lambda: update_text(btn4))
btn4.grid(row = 1,column= 0, sticky=tk.W+tk.E)


btn5 = tk.Button(buttoframe, text = "5", font =('Arial', 18),command=lambda: update_text(btn5))
btn5.grid(row = 1,column= 1, sticky=tk.W+tk.E)


btn6 = tk.Button(buttoframe, text = "6", font =('Arial', 18),command=lambda: update_text(btn6))
btn6.grid(row = 1,column= 2, sticky=tk.W+tk.E)


btn7 = tk.Button(buttoframe, text = "7", font =('Arial', 18),command=lambda: update_text(btn7))
btn7.grid(row = 2,column= 0, sticky=tk.W+tk.E)


btn8 = tk.Button(buttoframe, text = "8", font =('Arial', 18),command=lambda: update_text(btn8))
btn8.grid(row = 2,column= 1, sticky=tk.W+tk.E)


btn9 = tk.Button(buttoframe, text = "9", font =('Arial', 18),command=lambda: update_text(btn9))
btn9.grid(row = 2,column= 2, sticky=tk.W+tk.E)

btn0 = tk.Button(buttoframe, text = "0", font =('Arial', 18),command=lambda: update_text(btn0))
btn0.grid(row = 3,column= 1, sticky=tk.W+tk.E)

#operators
add = tk.Button(buttoframe, text = "+", font =('Arial', 18),command=lambda: update_text(add))
add.grid(row = 0,column= 3, sticky=tk.W+tk.E)

multipy = tk.Button(buttoframe, text = "*", font =('Arial', 18),command=lambda: update_text(multipy))
multipy.grid(row = 1,column= 3, sticky=tk.W+tk.E)

subtract = tk.Button(buttoframe, text = "-", font =('Arial', 18),command=lambda: update_text(subtract))
subtract.grid(row = 2,column= 3, sticky=tk.W+tk.E)

divide = tk.Button(buttoframe, text = "/", font =('Arial', 18),command=lambda: update_text(divide))
divide.grid(row = 3,column= 3, sticky=tk.W+tk.E)

equal = tk.Button(buttoframe, text = "=", font =('Arial', 18),command=lambda: update_text(equal))
equal.grid(row = 3,column= 2, sticky=tk.W+tk.E)




delete = tk.Button(buttoframe, text = "DEL", font =('Arial', 18),command=delete)
delete.grid(row = 3,column=0,sticky=tk.W+tk.E)


buttoframe.pack(fill='x')




win.mainloop()