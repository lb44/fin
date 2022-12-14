import tkinter as tk
from tkinter import *
from  tkinter import ttk
from PIL import ImageTk,Image
import tkinter.font as font



def add_custom():
    import addcustomer_form

editinvoice_form = tk.Tk()
editinvoice_form.title("finsYs")
editinvoice_form.geometry("5000x2000")
editinvoice_form['bg']='#2f516a'
wrappen=ttk.LabelFrame(editinvoice_form)
mycanvas=Canvas(wrappen)
mycanvas.pack(side=LEFT,fill="both",expand="yes")
yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

full_frame=Frame(mycanvas,width=2000,height=2500,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")


heading_frame=Frame(mycanvas)
mycanvas.create_window((10,20),window=heading_frame,anchor="nw")
invoice_heading= tk.Label(heading_frame, text="BALANCE SHEET",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=('Times', 25),width=68)
invoice_heading.pack()

#form fields

form_frame=Frame(mycanvas,width=1240,height=200,bg='#243e55')
mycanvas.create_window((10,130),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg='#243e55',width=50)
form_lable.place(x=0,y=0)
# form_heading=tk.Label(form_lable, text="FinsYs",fg='#fff',bg='#243e55',height=2,bd=1,relief="groove",font=('Times', 20),width=125)
# form_heading.pack()




select_customer_lab=tk.Label(form_frame,text="report period",bg='#243e55',fg='#fff')
select_customer_input=StringVar()
select_customer_lab.place(x=30,y=35,height=15)
drop2=ttk.Combobox(form_frame,textvariable = select_customer_input)
drop2['values']=("All dates", "Custom","Today","This month","This financial year")
drop2.place(x=30,y=50,height=40,width=200)
wrappen.pack(fill='both',expand='yes',)



b = Button(form_frame,text = "run report",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold'))  
b.place(x=900,y=120,width=130,height=40)
b = Button(form_frame,text = "back",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold'))  
b.place(x=1050,y=120,width=130,height=40)



form_frame=Frame(mycanvas,width=1240,height=1500,bg='#243e55')
mycanvas.create_window((10,355),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg='#243e55',width=50)
form_lable.place(x=0,y=0)

F = LabelFrame(form_frame, font=('times new roman', 15, 'bold'), fg="Black", bg="#FFFFFF")
F.place(x=145, y=50, width=950, height=1000 )
F1 = LabelFrame(F, font=('times new roman', 15, 'bold'), fg="Black", bg="#add8e6")
F1.place(x=-50, y=0, width=1000, height=200)



set = ttk.Treeview(form_frame,height=300)
set.place(x=145,y=250)

set['columns']= ('CUSTOMER NAME', 'TRANSACTION TYPE','CURRENT','0-30','30-60','60-90','90 AND OVER','TOTAL')
set.column("#0", width=0,  stretch=NO)
set.column("CUSTOMER NAME",width=120,anchor=CENTER )
set.column("TRANSACTION TYPE",width=130,anchor=CENTER, )
set.column("CURRENT",width=100,anchor=CENTER,)
set.column("0-30",width=100,anchor=CENTER,)
set.column("30-60",width=100,anchor=CENTER,)
set.column("60-90",width=100,anchor=CENTER)
set.column("90 AND OVER",width=100,anchor=CENTER)
set.column("TOTAL",width=198,anchor=CENTER)


#set.heading("#0",text="",anchor=CENTER)
set.heading("CUSTOMER NAME",text="",anchor=CENTER )
set.heading("TRANSACTION TYPE",text="",anchor=CENTER, )
set.heading("CURRENT",text="",anchor=CENTER,)
set.heading("0-30",text="",anchor=CENTER,)
set.heading("30-60",text="",anchor=CENTER,)
set.heading("60-90",text="",anchor=CENTER)
set.heading("90 AND OVER",text="",anchor=CENTER)
set.heading("TOTAL",text="TOTAL",anchor=CENTER)
my_label = Label(form_frame,text = "Assets",bg="#FFFFFF")
my_label.place(x=160,y=290)
my_label = Label(form_frame,text = " Current assets",bg="#FFFFFF")
my_label.place(x=180,y=320)

my_label = Label(form_frame,text = " Bank ",bg="#FFFFFF")
my_label.place(x=160,y=360)
my_label = Label(form_frame,text = " Account Receivable",bg="#FFFFFF")
my_label.place(x=180,y=390)
my_label = Label(form_frame,text = " 0.0",bg="#FFFFFF")
my_label.place(x=975,y=390)
my_label = Label(form_frame,text = " Total Account Receivable",bg="#FFFFFF")
my_label.place(x=180,y=420)
my_label = Label(form_frame,text = " 0.0",bg="#FFFFFF")
my_label.place(x=975,y=420)
my_label = Label(form_frame,text = " Total Current assets ",bg="#FFFFFF")
my_label.place(x=160,y=460)
my_label = Label(form_frame,text = " 0.0",bg="#FFFFFF")
my_label.place(x=975,y=460)
my_label = Label(form_frame,text = " Total Assets ",bg="#FFFFFF")
my_label.place(x=160,y=490)
my_label = Label(form_frame,text = " 0.0",bg="#FFFFFF")
my_label.place(x=975,y=490)




editinvoice_form.mainloop()