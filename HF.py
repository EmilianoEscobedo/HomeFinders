from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title('Home finders v0.1')
root.geometry('300x330')
f1=Frame(root, bg='#64778D')
f1.pack()
f2=Frame(root, bg='#64778D')
f2.pack()
#root=cascade // f1=entrys & labels // f2=buttons

#------------------------------Functions-------------------------------------
def cdb():
    hs=sqlite3.connect('Home Search')
    dbcursor=hs.cursor()
    try:
        dbcursor.execute('''CREATE TABLE Home_Search (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME VARCHAR(30),
        RELATION VARCHAR(40),
        TEL VARCHAR(40),
        COMMENT TEXT   
        )''')
        messagebox.showinfo('Data Base', 'Data Base create successfully')
    except:
        messagebox.showwarning('Data Base', 'Data Base is alredy created')
def exit():
    value=messagebox.askquestion('Data Base', 'Dou you really want to exit?')
    if value=='yes':
        root.destroy()
def Clear():
    EidVar.set('')
    EnameVar.set('')
    ErelationVar.set('')
    EtelVar.set('')
    Ecomment.delete('1.0', END)
def helpmenu(o):
    if o=='l':
        messagebox.showinfo('Licence', 
        '''
        Home Finders its a free software program
        under GNU GPL v3 2007. 
        You can use, share, study and modify 
        this software for free.
        ''')
    if o=='f':
        messagebox.showinfo('FAQ', '''
        1. Q. WTF is this program? 
        1. A. This program its an usefull tool to make your own 
        DB of home finders, a really tipically thing at Argentina 
        and the rest of poor and shitty nations. 
        2. Q. Nice! and how i use this crap? 
        2. A. If is your fist time at HF you will have to create DB
        at Connect button in the menu DB, after that 
        Do NOT introduce any charater at ID camp, its an 
        autoincrement camp and he does all the work :). 
        Finally fill other camps and press Create button 
        for save the data at your DB. 
        3. Q. Ok, cool. And other buttons? 
        3. A. Use your brain my good friend, 
        now you are able to write an ID number
        for read, update or delete information of your DB.
        Have a nice experience at HF v0.1 
        Good luck with your next home! 
        A big hug from Laingardo.''')
    if o=='a':
        messagebox.showinfo('About',
        '''
        Laingardo its a nice good guy who want 
        to be a programmer.
        In your free time work on develop 
        this tinys shit programs only for practice.
        ''')
def save():
    hs=sqlite3.connect('Home Search')
    dbcursor=hs.cursor()
    saves= [Ename.get(), Erelation.get(), Etel.get(), Ecomment.get('1.0',END)]
    dbcursor.execute('INSERT INTO Home_Search VALUES (NULL, ?, ?, ?, ?)', saves,)
    hs.commit()
    messagebox.showinfo('Data Base', 'Register successfully created!')

def read():
    Rid=Eid.get()
    hs=sqlite3.connect('Home Search')
    dbcursor=hs.cursor()
    dbcursor.execute('SELECT * FROM Home_Search WHERE ID=' + Rid)
    san=dbcursor.fetchone()
    EnameVar.set(san[1])
    ErelationVar.set(san[2])
    EtelVar.set(san[3])
    Ecomment.delete(1.0, END)
    Ecomment.insert(1.0, san[4])    
    hs.commit()

def update():
    hs=sqlite3.connect('Home Search')
    dbcursor=hs.cursor()
    ask=messagebox.askquestion('Data Base', 'Do you wanna update these camps?')
    if ask=='yes':
        saves=[Ename.get(), Erelation.get(), Etel.get(), Ecomment.get('1.0',END)]
        dbcursor.execute("UPDATE Home_Search SET NAME=?, RELATION=?, TEL=?, COMMENT=? WHERE ID="+Eid.get(), saves)
        hs.commit()
    
def delete():
    hs=sqlite3.connect('Home Search')
    dbcursor=hs.cursor()
    ask=messagebox.askquestion('Data Base', 'Do you want to delete this register?')
    if ask=='yes':
        dbcursor.execute('DELETE FROM Home_Search WHERE ID='+Eid.get())
        hs.commit()

#Cascade=
usermenu=Menu(root)
root.config(menu=usermenu, width=300, height=300, bg='black')
db=Menu(usermenu, tearoff=0)
db.add_command(label='Create/Connect', command=lambda:cdb())
db.add_command(label='Exit', command=lambda:exit())

clear=Menu(usermenu, tearoff=0)
clear.add_command(label='Clear data', command=lambda:Clear())

faq=Menu(usermenu, tearoff=0)
faq.add_command(label='Licence', command=lambda:helpmenu('l'))
faq.add_command(label='FAQ', command=lambda:helpmenu('f'))
faq.add_command(label='About', command=lambda:helpmenu('a'))

usermenu.add_cascade(label='Data Base', menu=db)
usermenu.add_cascade(label='Clear', menu=clear)
usermenu.add_cascade(label='Help', menu=faq)

#Labels=
Lid=Label(f1, text='ID', font=('Helvetica', 10, 'bold'), bg='black', fg='white')
Lid.grid(row=0, column=0, sticky='e', padx=10, pady=10)

Lname=Label(f1, text='Name', font=('Helvetica', 10, 'bold'), bg='black', fg='white')
Lname.grid(row=1, column=0, sticky='e', padx=10, pady=10)

Lrelation=Label(f1, text='Relation', font=('Helvetica', 10, 'bold'), bg='black', fg='white')
Lrelation.grid(row=2, column=0, sticky='e', padx=10, pady=10)

Ltel=Label(f1, text='Tel', font=('Helvetica', 10, 'bold'), bg='black', fg='white')
Ltel.grid(row=3, column=0, sticky='e', padx=10, pady=10)

Lcomment=Label(f1, text='Comment', font=('Helvetica', 10, 'bold'), bg='black', fg='white')
Lcomment.grid(row=4, column=0, sticky='e', padx=10, pady=10)

#Entrys=
EidVar=StringVar()
Eid=Entry(f1, font=('Helvetica', 10, 'bold'), justify='center', textvariable=EidVar)    
Eid.grid(row=0, column=1, padx=10, pady=10)

EnameVar=StringVar()
Ename=Entry(f1, font=('Helvetica', 10, 'bold'), justify='left', textvariable=EnameVar)
Ename.grid(row=1, column=1, padx=10, pady=10)

ErelationVar=StringVar()
Erelation=Entry(f1, font=('Helvetica', 10, 'bold'), justify='left', textvariable=ErelationVar)
Erelation.grid(row=2, column=1, padx=10, pady=10)

EtelVar=StringVar()
Etel=Entry(f1, font=('Helvetica', 10, 'bold'), justify='left', textvariable=EtelVar)
Etel.grid(row=3, column=1, padx=10, pady=10)

Ecomment=Text(f1, width=20, height=5)
Ecomment.grid(row=4, column=1, padx=10, pady=10)
ScrollVert=Scrollbar(f1, command=Ecomment.yview)
ScrollVert.grid(row=4, column=2, sticky='nsew')
Ecomment.config(font=('Helvetica', 10, 'bold'), yscrollcommand=ScrollVert.set)

#Buttons=
Bc=Button(f2, text='Create', font=('Helvetica', 10, 'bold'), pady=10, padx=10, command=lambda:save())
Bc.grid(row=0, column=0, sticky='e')

Br=Button(f2, text='Read', font=('Helvetica', 10, 'bold'), pady=10, padx=10, command=lambda:read())
Br.grid(row=0, column=1, sticky='e')

Bu=Button(f2, text='Update', font=('Helvetica', 10, 'bold'), pady=10, padx=10, command=lambda:update())
Bu.grid(row=0, column=2, sticky='e')

Bd=Button(f2, text='Delete', font=('Helvetica', 10, 'bold'), pady=10, padx=10, command=lambda:delete())
Bd.grid(row=0, column=3, sticky='e')


root.mainloop()
