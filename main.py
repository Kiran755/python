from contextlib import redirect_stderr
from email import message
from tkinter import *
from tkinter import ttk
from types import NoneType
from cv2 import add
import mysql.connector
from tkinter import messagebox
from sqlalchemy import create_engine








global root
root = Tk()

med_ref=StringVar()
med_name = StringVar()
med_company =  StringVar()
med_mfg =  StringVar()
med_exp =  StringVar()
med_type1 =  StringVar()
med_eff =  StringVar()
med_side =  StringVar()
med_price1 = StringVar()
med_other =  StringVar()
update_ref_id = StringVar()

def connection_add():
    print("hello world")
    print(med_ref.get())
    print(med_mfg.get())
    print(med_exp.get())
    conn = mysql.connector.connect(host="localhost",username="root",password="Kiran$@9869768493",database="mini")
    my_cursor = conn.cursor()
    my_cursor.execute("insert into pharmacy(Ref_no,Name,Medicine_type,Effectivity,Company_Name,Mfg_date,exp_date,Side_Effects,Price,Other_Details) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            med_ref.get(),
            med_name.get(),
            med_type1.get(),
            med_eff.get(),
            med_company.get(),
            med_mfg.get(),
            med_exp.get(),
            med_side.get(),
            med_price1.get(),
            med_other.get()



    ))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success","Connection was succesful")
    med_ref.set("")
    med_name.set("")
    med_type1.set("")
    med_eff.set("")
    med_company.set("")
    med_mfg.set("")
    med_exp.set("")
    med_side.set("")
    med_price1.set("")
    med_other.set("")

def clear_data():
    med_ref.set("")
    med_name.set("")
    med_type1.set("")
    med_eff.set("")
    med_company.set("")
    med_mfg.set("")
    med_exp.set("")
    med_side.set("")
    med_price1.set("")
    med_other.set("")


def update_connection():
    conn = mysql.connector.connect(host="localhost",username="root",password="Kiran$@9869768493",database="mini")
    update_cursor = conn.cursor()
    print("awd")
    ref_id = int(update_ref_id.get())
    print(ref_id)

    c = update_cursor
    query = 'SELECT * from pharmacy WHERE Ref_no = %s'
    c.execute(query,[ref_id])    # selected rows stored in cursor memory
    rows = c.fetchone()
    if rows==None:
        messagebox.showinfo("Failure","No Ref_id found!")
    else:
        med_name.set(rows[1])
        if(rows[2]=="Topical"):
            med_type.current(0)
        elif rows[2]=="Antihistamine":
            med_type.current(1)
        else:
            med_type.current(2)
        med_eff.set(rows[3])
        med_company.set(rows[4])
        med_mfg.set(rows[5])
        med_exp.set(rows[6])
        med_side.set(rows[7])
        med_price1.set(rows[8])
        med_other.set(rows[9])

                           

def update_values():
    conn = mysql.connector.connect(host="localhost",username="root",password="Kiran$@9869768493",database="mini")
    update_cursor = conn.cursor()
    print("awd")
    ref_id = int(update_ref_id.get())
    print(ref_id)

    print(med_company.get())
    c = update_cursor
    query = 'SELECT * from pharmacy WHERE Ref_no = %s'
    c.execute(query,[ref_id])   
    rows = c.fetchone()
    c.execute("UPDATE pharmacy SET Name=%s,Medicine_type=%s,Effectivity=%s,Company_Name=%s,Mfg_date=%s,exp_date=%s,Side_Effects=%s,Price=%s,Other_Details=%s WHERE Ref_no = %s",(
            med_name.get(),
            med_type1.get(),
            med_eff.get(),
            med_company.get(),
            med_mfg.get(),
            med_exp.get(),
            med_side.get(),
            med_price1.get(),
            med_other.get(),
            ref_id,
    ))
    conn.commit()
    conn.close()         
    messagebox.showinfo("Success","Connection was succesful")


def delete_values():
    conn = mysql.connector.connect(host="localhost",username="root",password="Kiran$@9869768493",database="mini")
    update_cursor = conn.cursor()
    print("awd")
    ref_id = int(update_ref_id.get())
    print(ref_id)
    c = update_cursor
    c.execute("DELETE FROM pharmacy WHERE Ref_no = %s",[ref_id])
    conn.commit()
    conn.close()
    messagebox.showinfo("Success","Deletion was succesful")
    clear_data()

def open_add():
    
    global add
    add = Toplevel(root)
    add.geometry("1920x1080+0+0")
    add.title("New Window")
    Label(add, text="ADDING ITEM", font=('Helvetica 17 bold')).pack(pady=30)
    DataFrame =  Frame(add,bd=0,relief=RIDGE,padx=20)
    DataFrame.place(x=0,y=120,width=1530,height=600)





    DataFrameLeft = LabelFrame(DataFrame,bd=10,padx=20,relief=RIDGE,text="INFORMATION",font=("calibri 25"))
    DataFrameLeft.place(x=0,y=5,width=1400,height=550)


##---------------REFERENCE------------------
    RefrenceLabel = Label(DataFrameLeft,font=("calibri 25"),text="Refernce No.")
    RefrenceLabel.place(x=0,y=40)
    txtRef = Entry(DataFrameLeft,textvariable = med_ref, font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    txtRef.place(x=300,y=40)



##---------------MEDICINE NAME---------------
    MedicineName = Label(DataFrameLeft,font=("calibri 25"),text="Medicine Name :")
    MedicineName.place(x=0,y=80)
    TxtName = Entry(DataFrameLeft,textvariable = med_name,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    TxtName.place(x=300,y=80)



##--------------------MEDICINE TYPE--------------------
    MedicineType = Label(DataFrameLeft,font=("calibri 25"),text="Medicine Type :")
    MedicineType.place(x=0,y=120)

    global med_type
    med_type = ttk.Combobox(DataFrameLeft,font=("calibri 20"),state="readonly",textvariable=med_type1)
    med_type["values"] = ("Topical","Antihistamine","ABC")
    med_type.place(x=300,y=120)



##---------------------COMPANY NAME------------------------
    CompanyLabel = Label(DataFrameLeft,font=("calibri 25"),text="Company Name :")
    CompanyLabel.place(x=0,y=160)
    CNameTxt = Entry(DataFrameLeft,textvariable=med_company,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    CNameTxt.place(x=300,y=160)



##----------------------------MFG DATE--------------------------------------
    MDateLabel = Label(DataFrameLeft,font=("calibri 25"),text="Mfg Date :")
    MDateLabel.place(x=0,y=200)
    MDateTxt = Entry(DataFrameLeft,textvariable=med_mfg,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    MDateTxt.place(x=300,y=200)





##-----------------------------EXP DATE-------------------------------------
    EDateLabel = Label(DataFrameLeft,font=("calibri 25"),text="Exp Date :")
    EDateLabel.place(x=0,y=240)
    EDateTxt = Entry(DataFrameLeft,textvariable=med_exp,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    EDateTxt.place(x=300,y=240)





##--------------------------------EFFECTIVE AGAINST--------------------------
    EffLabel = Label(DataFrameLeft,font=("calibri 25"),text="Effective against :")
    EffLabel.place(x=0,y=280)
    EffTxt = Entry(DataFrameLeft,textvariable=med_eff,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    EffTxt.place(x=300,y=280)


##-----------------------SIDE EFFECTS------------------------------------
    SideLabel = Label(DataFrameLeft,font=("calibri 25"),text="Side effects :")
    SideLabel.place(x=0,y=320)
    Sidetxt = Entry(DataFrameLeft,textvariable=med_side,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    Sidetxt.place(x=300,y=320)




##-----------------PRICE LABEL
    PriceLabel = Label(DataFrameLeft,font=("calibri 25"),text="Price:")
    PriceLabel.place(x=0,y=360)
    PriceTxt2 = Entry(DataFrameLeft,textvariable=med_price1,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    PriceTxt2.place(x=300,y=360)



##-------------------OTHER DETAILS
    SideLabel = Label(DataFrameLeft,font=("calibri 25"),text="Other Details :")
    SideLabel.place(x=0,y=400)
    Sidetxt = Entry(DataFrameLeft,textvariable=med_other,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    Sidetxt.place(x=300,y=400)

    addData = Button(DataFrameLeft,text="Add",font=("arial",13),width=14,command=connection_add)
    addData.place(x=0,y=440)

    Clear_data = Button(DataFrameLeft,text="Clear Data",font=("arial",13),width= 14,command = clear_data)
    Clear_data.place(x=200,y=440)





def Update():
    global update 
    update = Toplevel(root)
    update.geometry("1920x1080+0+0")
    update.title("New Window")


    Label(update, text="UPDATING ITEM", font=('Helvetica 17 bold')).pack(pady=30)
    DataFrame =  Frame(update,bd=3,relief=RIDGE,padx=20)


    DataFrame.place(x=0,y=120,width=1530,height=600)
    SideLabel = Label(DataFrame,font=("calibri 25"),text="Enter Ref Id :")
    SideLabel.place(x=0,y=0)
    Sidetxt = Entry(DataFrame,textvariable=update_ref_id,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    Sidetxt.place(x=290,y=10)
    SearchData = Button(DataFrame,text="Search",font=("arial",13),width=14,command=update_connection)
    SearchData.place(x=550,y=10)

    DataFrameLeft = Frame(DataFrame,bd=3,padx=20,relief=RIDGE)
    DataFrameLeft.place(x=0,y=80,width=1400,height=500)


    MedicineName = Label(DataFrameLeft,font=("calibri 25"),text="Medicine Name :")
    MedicineName.place(x=0,y=80)
    TxtName = Entry(DataFrameLeft,textvariable = med_name,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    TxtName.place(x=300,y=80)

    MedicineType = Label(DataFrameLeft,font=("calibri 25"),text="Medicine Type :")
    MedicineType.place(x=0,y=120)

    global med_type 
    med_type = ttk.Combobox(DataFrameLeft,font=("calibri 20"),state="readonly", textvariable=med_type1)
    med_type["values"] = ("Topical","Antihistamine","ABC")
    med_type.place(x=300,y=120)

    CompanyLabel = Label(DataFrameLeft,font=("calibri 25"),text="Company Name :")
    CompanyLabel.place(x=0,y=160)
    CNameTxt = Entry(DataFrameLeft,textvariable=med_company,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    CNameTxt.place(x=300,y=160)


    MDateLabel = Label(DataFrameLeft,font=("calibri 25"),text="Mfg Date :")
    MDateLabel.place(x=0,y=200)
    MDateTxt = Entry(DataFrameLeft,textvariable=med_mfg,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    MDateTxt.place(x=300,y=200)


    EDateLabel = Label(DataFrameLeft,font=("calibri 25"),text="Exp Date :")
    EDateLabel.place(x=0,y=240)
    EDateTxt = Entry(DataFrameLeft,textvariable=med_exp,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    EDateTxt.place(x=300,y=240)

    EffLabel = Label(DataFrameLeft,font=("calibri 25"),text="Effective against :")
    EffLabel.place(x=0,y=280)
    EffTxt = Entry(DataFrameLeft,textvariable=med_eff,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    EffTxt.place(x=300,y=280)

    SideLabel = Label(DataFrameLeft,font=("calibri 25"),text="Side effects :")
    SideLabel.place(x=0,y=320)
    Sidetxt = Entry(DataFrameLeft,textvariable=med_side,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    Sidetxt.place(x=300,y=320)

    PriceLabel = Label(DataFrameLeft,font=("calibri 25"),text="Price:")
    PriceLabel.place(x=0,y=360)
    PriceTxt = Entry(DataFrameLeft,textvariable=med_price1,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    PriceTxt.place(x=300,y=360)

    SideLabel = Label(DataFrameLeft,font=("calibri 25"),text="Other Details :")
    SideLabel.place(x=0,y=400)
    Sidetxt = Entry(DataFrameLeft,textvariable=med_other,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    Sidetxt.place(x=300,y=400)

    updateBtn = Button(DataFrameLeft,text="Update Data",font=("arial",13),width= 14,command = update_values)
    updateBtn.place(x=0,y=440)


def delete():
    global delete_data
    delete_data = Toplevel(root)
    delete_data.geometry("1920x1080+0+0")
    delete_data.title("New Window")


    Label(delete_data, text="DELETING ITEM", font=('Helvetica 17 bold')).pack(pady=30)
    DataFrame =  Frame(delete_data,bd=3,relief=RIDGE,padx=20)


    DataFrame.place(x=0,y=120,width=1530,height=600)
    SideLabel = Label(DataFrame,font=("calibri 25"),text="Enter Ref Id :")
    SideLabel.place(x=0,y=0)
    Sidetxt = Entry(DataFrame,textvariable=update_ref_id,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    Sidetxt.place(x=290,y=10)
    SearchData = Button(DataFrame,text="Search",font=("arial",13),width=14,command=update_connection)
    SearchData.place(x=550,y=10)

    DataFrameLeft = Frame(DataFrame,bd=3,padx=20,relief=RIDGE)
    DataFrameLeft.place(x=0,y=80,width=1400,height=500)


    MedicineName = Label(DataFrameLeft,font=("calibri 25"),text="Medicine Name :")
    MedicineName.place(x=0,y=80)
    TxtName = Entry(DataFrameLeft,textvariable = med_name,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    TxtName.place(x=300,y=80)

    MedicineType = Label(DataFrameLeft,font=("calibri 25"),text="Medicine Type :")
    MedicineType.place(x=0,y=120)

    global med_type 
    med_type = ttk.Combobox(DataFrameLeft,font=("calibri 20"),state="readonly", textvariable=med_type1)
    med_type["values"] = ("Topical","Antihistamine","ABC")
    med_type.place(x=300,y=120)

    CompanyLabel = Label(DataFrameLeft,font=("calibri 25"),text="Company Name :")
    CompanyLabel.place(x=0,y=160)
    CNameTxt = Entry(DataFrameLeft,textvariable=med_company,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    CNameTxt.place(x=300,y=160)


    MDateLabel = Label(DataFrameLeft,font=("calibri 25"),text="Mfg Date :")
    MDateLabel.place(x=0,y=200)
    MDateTxt = Entry(DataFrameLeft,textvariable=med_mfg,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    MDateTxt.place(x=300,y=200)


    EDateLabel = Label(DataFrameLeft,font=("calibri 25"),text="Exp Date :")
    EDateLabel.place(x=0,y=240)
    EDateTxt = Entry(DataFrameLeft,textvariable=med_exp,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    EDateTxt.place(x=300,y=240)

    EffLabel = Label(DataFrameLeft,font=("calibri 25"),text="Effective against :")
    EffLabel.place(x=0,y=280)
    EffTxt = Entry(DataFrameLeft,textvariable=med_eff,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    EffTxt.place(x=300,y=280)

    SideLabel = Label(DataFrameLeft,font=("calibri 25"),text="Side effects :")
    SideLabel.place(x=0,y=320)
    Sidetxt = Entry(DataFrameLeft,textvariable=med_side,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    Sidetxt.place(x=300,y=320)

    PriceLabel = Label(DataFrameLeft,font=("calibri 25"),text="Price:")
    PriceLabel.place(x=0,y=360)
    PriceTxt = Entry(DataFrameLeft,textvariable=med_price1,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    PriceTxt.place(x=300,y=360)

    SideLabel = Label(DataFrameLeft,font=("calibri 25"),text="Other Details :")
    SideLabel.place(x=0,y=400)
    Sidetxt = Entry(DataFrameLeft,textvariable=med_other,font=("calibri",20),bg="white",bd=2,relief=RIDGE,width=14)
    Sidetxt.place(x=300,y=400)

    updateBtn = Button(DataFrameLeft,text="Delete Data",font=("arial",13),width= 14,command = delete_values)
    updateBtn.place(x=0,y=440)





def open_win():
    global dash
    dash = Tk()
    root.withdraw()
    dash.geometry("1920x1080+0+0")
    dash.title("New Window")


    DataFrame =  Frame(dash,bd=0,relief=RIDGE,padx=20)
    DataFrame.place(x=0,y=120,width=1530,height=600)


    DataFrameLeft = LabelFrame(DataFrame,bd=10,padx=20,relief=RIDGE,text="MAIN DASHBOARD",font=("calibri 25"))
    DataFrameLeft.place(x=0,y=5,width=1400,height=550)


    Button(DataFrameLeft, text='ADD MEDICINE',font=("calibri",25),width=20,command=open_add).place(x=10,y=10)
    Button(DataFrameLeft, text='UPDATE',font=("calibri",25),width=20,command=Update).place(x=1000,y=10)
    Button(DataFrameLeft, text='DELETE',font=("calibri",25),width=20,command=delete).place(x=10,y=100)
    Button(DataFrameLeft, text='VIEW',font=("calibri",25),width=20,command=open_add).place(x=1000,y=100)













class MainPage:
    def __init__(self,root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.configure(bg='#421CB5')

        title = Label(self.root,text="WELCOME TO PHARMACY MANAGEMENT SYSTEM",bd="4",relief=FLAT,font=("calibri",25,"bold"),bg="#421CB5",fg="white")
        title.pack()
        
        login = Label(self.root,text="Username : ",bd="3",
        relief=FLAT,font=("calibri",20),bg="#421CB5",fg="white")
        T = Text(root, height = 1, width = 32,font=("calibri",20))


        Pass = Label(self.root,text="Password : ",bd="3",
        relief=FLAT,font=("calibri",20),bg="#421CB5",fg="white",)
        passEntry = Entry(self.root,textvariable="password", show='*',font=("calibri",20),width = 32)
        Pass.place(relx=0.3,rely=0.4)
        T.place(relx=0.4,rely=0.3)
        passEntry.place(relx=0.4, rely=0.4)
        login.place(relx=0.3,rely=0.3)
        Auth = Button(self.root, text='Authenticate',font=("calibri",25),command=open_win)
        Auth.place(relx=0.45,rely=0.5)
    



obj = MainPage(root)

root.mainloop()
