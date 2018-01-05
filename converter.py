# -*- coding: utf-8 -*-

from xml.etree.ElementTree import parse
from tkinter import filedialog
from tkinter import *
import pandas as pd

# root
root = Tk()
root.title("XML to CSV converter")

# lbl
lbl = Label(root, text="File")
lbl.grid(row=0, column=0)

# txt
txt = Entry(root, width=35)
txt.grid(row=0, column=1)

# btn1
def click1():
    txt.insert(0, '')
    myfile = filedialog.askopenfilename( filetypes = ( ("XML", ".xml"), ("All files", "*.*") ) )
    txt.insert(0, myfile)

btn1 = Button(root, text="select", command=click1, borderwidth=2, width=5)  # grid.arrange
btn1.grid(row=0, column=2)

# btn1.bind("<key>", click1)

# btn2
btn2 = Button(root, text="convert", borderwidth=2, width=5)
btn2.grid(row=0, column=3)

def click2(event):
    # tree = parse("C:\\Users\\seokhoonj\\Desktop\\sms-20171221155428.xml")
    mypath = txt.get()
    tree = parse(mypath)
    notes = tree.findall('sms')

    mycol = []
    for k, v in notes[0].items():
        mycol.append(k)

    mydb = []
    mylist = []
    for row in range(len(notes)):
        mylist = []
        for k, v in notes[row].items():
            mylist.append(v)
        mydb.append(mylist)

    db = pd.DataFrame(mydb)
    db.columns = mycol
    db = db[76:]
    db[db['address'].astype(str).str[0]=='0']
    db['address'] = db['address'].astype(str).str[0:3]+'-'+db['address'].astype(str).str[3:7]+'-'+db['address'].astype(str).str[7:]
    db = db[['address','body','readable_date']]
    db.to_csv(mypath[0:mypath.find('.')] + '.csv')
    # popup
    popup = Toplevel(root)
    popuplbl = Label(popup, text="Go home!!")
    popuplbl.grid(row=1, column=0)

btn2.bind("<Button-1>", click2)

# mainloop
root.mainloop()
