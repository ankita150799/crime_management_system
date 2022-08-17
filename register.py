from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")

        #Variables

        self.var_ID=StringVar()
        self.var_scode=StringVar()
        self.var_first_name=StringVar()
        self.var_last_name=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_ros=StringVar()
        self.var_sname=StringVar()
        self.var_password=StringVar()
        self.var_conform_password=StringVar()


        img_logo=Image.open('images/download.png')
        img_logo=img_logo.resize((100,100),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=720,y=5,width=90,height=90)

        #Img_Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=100,width=1530,height=130)

        lbl_title2=Label(self.root,text= 'Kokata Police', font=('times new roman',40,'bold'),fg='black')
        lbl_title2.place(x=0,y=100,width=1530,height=70)

        lbl_title3=Label(self.root,text= 'Lalbazar,Kolkata:700001', font=('times new roman',20,'bold'),fg='black')
        lbl_title3.place(x=0,y=175,width=1530,height=70)

        #frame

        frame=Frame(self.root,bg='LightGrey')
        frame.place(x=355,y=300,width=840,height=450)

        #label
        register_lbl=Label(self.root,text="REGISTER HERE",font=("Courier new",20,"bold"),fg="black",bg='lightgrey')
        register_lbl.place(x=355,y=250,width=840,height=50)

        #entry lebels

        #row1
        ID=Label(frame,text="Officer's ID (User ID):",font=("times new roman",15,"bold"),fg="darkslategrey",bg="lightgrey")
        ID.place(x=50,y=20)

        ID_entry=Entry(frame,textvariable=self.var_ID, font=("Arial",12))
        ID_entry.place(x=50,y=45,width=250)

        scode=Label(frame,text="Station Code:",font=("times new roman",15,"bold"),fg="darkslategrey",bg="lightgrey")
        scode.place(x=480,y=20)

        scode_entry=Entry(frame,textvariable=self.var_scode, font=("Arial",12))
        scode_entry.place(x=480,y=45,width=250)

        #row2
        first_name=Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="darkslategrey",bg="lightgrey")
        first_name.place(x=50,y=75)

        first_name_entry=Entry(frame,textvariable=self.var_first_name, font=("Arial",12))
        first_name_entry.place(x=50,y=100,width=250)

        last_name=Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="darkslategrey",bg="lightgrey")
        last_name.place(x=480,y=75)

        last_name_entry=Entry(frame,textvariable=self.var_last_name, font=("Arial",12))
        last_name_entry.place(x=480,y=100,width=250)

        #row3
        contact=Label(frame,text="Contact Number:",font=("times new roman",15,"bold"),fg="darkslategrey",bg="lightgrey")
        contact.place(x=50,y=130)

        contact_entry=Entry(frame,textvariable=self.var_contact, font=("Arial",12))
        contact_entry.place(x=50,y=155,width=250)

        email=Label(frame,text="Official Email Id.:",font=("times new roman",15,"bold"),fg="darkslategrey",bg="lightgrey")
        email.place(x=480,y=130)

        email_entry=Entry(frame,textvariable=self.var_email, font=("Arial",12))
        email_entry.place(x=480,y=155,width=250)

        #row4
        ros=Label(frame,text="Region Of the Station:",font=("times new roman",15,"bold"),fg="darkslategrey",bg="lightgrey")
        ros.place(x=50,y=185)

        
        combo_ros_box=ttk.Combobox(frame,textvariable=self.var_ros, font=('times new roman',12,'bold'),foreground="darkslategrey",background="lightgrey",width=18,state='readonly')
        combo_ros_box['value']=('Select Option','North','South','East','West')
        combo_ros_box.current(0)
        combo_ros_box.place(x=50,y=212,width=250)

        sname=Label(frame,text="Station Name:",font=("times new roman",15,"bold"),fg="darkslategrey",bg="lightgrey")
        sname.place(x=480,y=185)

        sname_entry=Entry(frame,textvariable=self.var_sname, font=("Arial",12))
        sname_entry.place(x=480,y=212,width=250)

        #row5
        password=Label(frame, text="Password:",font=("times new roman",15,"bold"),fg="darkslategrey",bg="lightgrey")
        password.place(x=50,y=245)

        password_entry=Entry(frame,textvariable=self.var_password,font=("Arial",12))
        password_entry.place(x=50,y=270,width=250)

        confirm_password=Label(frame, text="Confirm Password:",font=("times new roman",15,"bold"),fg="darkslategrey",bg="lightgrey")
        confirm_password.place(x=480,y=245)

        confirm_password_entry=Entry(frame,textvariable=self.var_conform_password,font=("Arial",12))
        confirm_password_entry.place(x=480,y=270,width=250)

        #check_button
        self.var_check=IntVar()
        check_button=Checkbutton(frame,variable=self.var_check, text="I acknowedge that the informations that I've given are correct.",font=('times new roman',9,'bold'),fg="darkslategrey",bg='lightgrey',onvalue=1,offvalue=0)
        check_button.place(x=50,y=305)

        #register_button

        register_btn=Button(frame,command=self.register_data,text="Register",font=('times new roman',15,'bold'),fg='black',bg='darkgrey', activeforeground='black',activebackground='darkgrey')
        register_btn.place(x=200,y=370,width=120,height=50)

        #login_button
        login_btn=Button(frame,text="Login",font=('times new roman',15,'bold'),command=self.return_login, fg='black',bg='darkgrey', activeforeground='black',activebackground='darkgrey')
        login_btn.place(x=500,y=370,width=120,height=50)

    #function_declaration
    def register_data(self):
        if self.var_ID.get()=="" or self.var_scode.get()=="" or self.var_password.get()=="" or self.var_conform_password.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_password.get()!=self.var_conform_password .get():
            messagebox.showerror("Error","Password and Confirm Password must contain same value.")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree with the acknowledgement.")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='Boomboomwoosh',database='criminal_database')
            my_cursor=conn.cursor()
            query=("select * from register where ID=%s")
            value=(self.var_ID.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_ID.get(),
                    self.var_scode.get(),
                    self.var_first_name.get(),
                    self.var_last_name.get(),
                    self.var_contact.get(), 
                    self.var_email.get(),
                    self.var_ros.get(),
                    self.var_sname.get(),
                    self.var_password.get(),
                    self.var_conform_password.get()      
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration Successful")

    def return_login(self):
        self.root.destroy()

if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()