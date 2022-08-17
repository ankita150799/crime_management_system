from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import criminal as cr
import register as re

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1530x790+0+0")

        #self.bg=ImageTk.PhotoImage(file=r"C:\Users\DELL\Downloads\64.jpg")
        #lbl_bg=Label(self.root,image=self.bg)
        #lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

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

        #login frame

        frame= Frame(self.root,bg="Black")
        frame.place(x=595,y=270,width=340,height=450)

        img1=Image.open("images/logo4.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        lbl_img1=Label(image=self.photoimage1,bg='Black',borderwidth=0)
        lbl_img1.place(x=720,y=280,width=100,height=100)

        get_str=Label(frame,text="Login Page",font=('times new roman',20,'bold'),fg='white',bg='black')
        get_str.place(x=105,y=110)

        #lebels
        username_lbl=Label(frame,text='User ID',font=('times new roman',15,'bold'),fg='white',bg='black')
        username_lbl.place(x=50,y=155)

        self.textuser=ttk.Entry(frame,font=("times new roman",10))
        self.textuser.place(x=40,y=180,width=270)

        password_lbl=Label(frame,text='Password',font=('times new roman',15,'bold'),fg='white',bg='black')
        password_lbl.place(x=50,y=225)

        self.textpassword=ttk.Entry(frame,font=("times new roman",10))
        self.textpassword.place(x=40,y=250,width=270)

        #login button

        img2=Image.open("images/login.png")
        img2=img2.resize((105,50),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        lbl_img2=Button(image=self.photoimage2,command=self.login, bg='Black',borderwidth=0,cursor="hand2", activeforeground='white',activebackground='black')
        lbl_img2.place(x=710,y=550,width=120,height=80)

        #login_btn=Button(frame,text="Login",command=self.login,font=('times new roman',15,'bold'),fg='white',bg='red', activeforeground='white',activebackground='red')
        #login_btn.place(x=120,y=300,width=100,height=35)

        #register button

        register_btn=Button(frame,text="New User Register",command=self.register_window, font=('times new roman',10,'bold'),borderwidth =0,fg='white',bg='black', activeforeground='white',activebackground='black')
        register_btn.place(x=15,y=372,width=160)

        #forget password

        forgetpassword_btn=Button(frame,text="Forget Password ?",command=self.forget_password_window, font=('times new roman',10,'bold'),borderwidth =0,fg='white',bg='black', activeforeground='white',activebackground='black')
        forgetpassword_btn.place(x=15,y=390,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app= re.Register(self.new_window)
    
    def login(self):
        if self.textuser.get()=="" or self.textpassword.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.textuser.get()=="Ankita" and self.textpassword.get()=="Paul":
            messagebox.showinfo("Login Successful","You have sucessfully logged in")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='Boomboomwoosh',database='criminal_database')
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where ID=%s and password=%s",(
                self.textuser.get(),
                self.textpassword.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username or password")
            else:
                open_main=messagebox.askyesno("","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app= cr.Criminal(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    
    




    #reset_password

    def forget_password_window(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password.")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='Boomboomwoosh',database='criminal_database')
            my_cursor=conn.cursor()
            query=("select * from register where ID=%s")
            value=(self.textuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

        if row==None:
            messagebox.showerror("Error","Please enter a valid user ID")
        else:
            conn.close()
            self.root2=Toplevel()
            self.root2.title("Forget Password")
            self.root2.geometry("340x450+610+200")

            l=Label(self.root2,text="Reset Password",font=('times new roman',20,'bold'),fg="Red",bg="white")
            l.place(x=0,y=20,relwidth=1)

            scode=Label(self.root2,text="Station Code:",font=("times new roman",12,"bold"),fg="darkslategrey")
            scode.place(x=50,y=100)

            self.scode_entry=ttk.Entry(self.root2,font=("Arial",10))
            self.scode_entry.place(x=50,y=130,width=250)

            email=Label(self.root2,text="Official Email Id.:",font=("times new roman",12,"bold"),fg="darkslategrey")
            email.place(x=50,y=170)

            self.email_entry=ttk.Entry(self.root2,font=("Arial",10))
            self.email_entry.place(x=50,y=200,width=250)

            new_password=Label(self.root2,text="New Password:",font=("times new roman",12,"bold"),fg="darkslategrey")
            new_password.place(x=50,y=230)

            self.new_password_entry=ttk.Entry(self.root2,font=("Arial",10))
            self.new_password_entry.place(x=50,y=270,width=250)

            confirm_password=Label(self.root2,text="Confirm New Password:",font=("times new roman",12,"bold"),fg="darkslategrey")
            confirm_password.place(x=50,y=310)

            self.confirm_password_entry=ttk.Entry(self.root2,font=("Arial",10))
            self.confirm_password_entry.place(x=50,y=340,width=250)

            btn=Button(self.root2,command=self.reset_password, text="Reset",font=('times new roman',15,'bold'),fg='white',bg='red', activeforeground='white',activebackground='red')
            btn.place(x=140,y=390)

    def reset_password(self):
        if self.scode_entry.get()=="":
            messagebox.showerror("Error","Enter a valid Station Code.",parent=self.root2)
        elif self.email_entry.get()=="":
            messagebox.showerror("Error","Enter a valid email id.",parent=self.root2)
        elif self.new_password_entry.get()=="":
            messagebox.showerror("Error","Enter a new password",parent=self.root2)
        elif self.confirm_password_entry.get()=="" or self.new_password_entry.get()!= self.confirm_password_entry.get():
            messagebox.showerror("Error","Confirm password must be same as new password.")
        
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='Boomboomwoosh',database='criminal_database')
            my_cursor=conn.cursor()
            query=("select * from register where ID=%s and scode=%s and email=%s")
            value=(self.textuser.get(),self.scode_entry.get(),self.email_entry.get())
            my_cursor.execute(query,value)

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter a valid inpout.",parent=self.root2)
            else:
                query=("update register set password=%s , confirm_password=%s where ID=%s")
                value=(self.new_password_entry.get(),self.confirm_password_entry.get(),self.textuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("","Password reset successful.",parent=self.root2)
                self.root2.destroy()


if __name__=="__main__":
    main()