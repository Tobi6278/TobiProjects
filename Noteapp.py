# Personal Diary:
# An app to write and save daily journal entries with search functionality.
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('My Diary')
root.geometry("350x500")

root.config(bg="lightblue")

index = 1



notes1  = []

with open('storage.txt','r') as file:
   content = file.readlines()
   if len(content) < 1:
      pass
   else:
    for line in content:
        nt_box = LabelFrame(root,bd=5)
        nt_box.grid(row=index,sticky=W)

        notes = Label(nt_box,text=line,wraplength=300,justify=LEFT)
        notes.grid(row = f"{index}\n",column=0,sticky=W)
        num = Label(nt_box,text=index,font=("MS Comic Sans",7))
        num.grid(row=0,column=0,sticky=NW)

        index += 1
      




#Creates note box
def new_note():
    global note,e,save
    note = LabelFrame(root,bd=5,padx=30,pady=30)
   
    note.grid()
    e = Text(note,bd=5,width=20,height=4)
    e.pack()
    saved = Button(note,text="Save",bg="pink",command=save)
    saved.pack()




#Saves the notes and prints them on the window
def save():
    global note,e,saved,index
    text = e.get("1.0", END)
    note.destroy()
    nt_box = LabelFrame(root,bd=5)
    nt_box.grid(row=index,sticky=W)


    notes = Label(nt_box,text=text,wraplength=300,justify=LEFT)
    notes.grid(row = f"{index}\n",column=0,sticky=W)
    num = Label(nt_box,text=index,font=("MS Comic Sans",7))
    num.grid(row=0,column=0,sticky=NW)

    index += 1
    notes1.append(text)
    print(index)
    with open('storage.txt', 'w') as file:
     for i in notes1:
        file.write(i)


Create_btn = Button(root,text="Create New",bg='pink',command=new_note)
Create_btn.grid(row=0,padx=140)




root.resizable(False,False)

root.mainloop()