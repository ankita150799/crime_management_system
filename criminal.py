from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        #variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_crime_type=StringVar()
        self.var_criminal_name=StringVar()
        self.var_criminal_nickname=StringVar()
        self.var_father_name=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_gender=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_birthmark=StringVar()
        self.var_occupation=StringVar()
        self.var_wanted=StringVar()

        #logo
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
        
        #main_Frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=7,y=260,width=1510,height=520)

        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Criminal Information',font=('times new roman',15,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1484,height=250)

        #label_entry
        #case_id
        caseid=Label(upper_frame,text='Case ID:',font=('Arial',10,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('Arial',10,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        #Criminal_no
        lbl_criminal_no=Label(upper_frame,font=('Arial',10,'bold'),text='Criminal Number: ',bg='white')
        lbl_criminal_no.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=('Arial',10,'bold'))
        txt_criminal_no.grid(row=0,column=3,padx=2,pady=7)

        #Criminal_name
        lbl_criminal_name=Label(upper_frame,font=('Arial',10,'bold'),text='Criminal Name: ',bg='white')
        lbl_criminal_name.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_criminal_name=ttk.Entry(upper_frame,textvariable=self.var_criminal_name,width=22,font=('Arial',10,'bold'))
        txt_criminal_name.grid(row=1,column=1,padx=2,pady=7)

        #nick_name
        lbl_nick_name=Label(upper_frame,font=('Arial',10,'bold'),text='Criminal Nickname: ',bg='white')
        lbl_nick_name.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_nick_name=ttk.Entry(upper_frame,textvariable=self.var_criminal_nickname,width=22,font=('Arial',10,'bold'))
        txt_nick_name.grid(row=1,column=3,padx=2,pady=7)

        #father_name
        lbl_father_name=Label(upper_frame,font=('Arial',10,'bold'),text="Father's Name: ",bg='white')
        lbl_father_name.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_father_name=ttk.Entry(upper_frame,textvariable=self.var_father_name,width=22,font=('Arial',10,'bold'))
        txt_father_name.grid(row=1,column=5,padx=2,pady=7)

        #crime_type
        lbl_crime_type=Label(upper_frame,font=('Arial',10,'bold'),text='Crime Type: ',bg='white')
        lbl_crime_type.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_crime_type=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=('Arial',10,'bold'))
        txt_crime_type.grid(row=0,column=5,padx=2,pady=7)

        #Arrest_Date
        lbl_arrest_date=Label(upper_frame,font=('Arial',10,'bold'),text='Arrest Date: ',bg='white')
        lbl_arrest_date.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_arrest_date=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=('Arial',10,'bold'))
        txt_arrest_date.grid(row=2,column=1,padx=2,pady=7)

        #date_of_crime
        lbl_date_of_crime=Label(upper_frame,font=('Arial',10,'bold'),text='Date Of Crime: ',bg='white')
        lbl_date_of_crime.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_date_of_crime=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=('Arial',10,'bold'))
        txt_date_of_crime.grid(row=2,column=3,padx=2,pady=7)

        #address
        lbl_address=Label(upper_frame,font=('Arial',10,'bold'),text='Address: ',bg='white')
        lbl_address.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('Arial',10,'bold'))
        txt_address.grid(row=3,column=1,padx=2,pady=7)

        #age
        lbl_age=Label(upper_frame,font=('Arial',10,'bold'),text='Age: ',bg='white')
        lbl_age.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('Arial',10,'bold'))
        txt_age.grid(row=3,column=3,padx=2,pady=7)

        #occupation
        lbl_occupation=Label(upper_frame,font=('Arial',10,'bold'),text='Occupation: ',bg='white')
        lbl_occupation.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_occupation=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=('Arial',10,'bold'))
        txt_occupation.grid(row=4,column=1,padx=2,pady=7)

        #birthmark
        lbl_birthmark=Label(upper_frame,font=('Arial',10,'bold'),text='Birthmark: ',bg='white')
        lbl_birthmark.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_birthmark=ttk.Entry(upper_frame,textvariable=self.var_birthmark,width=22,font=('Arial',10,'bold'))
        txt_birthmark.grid(row=4,column=3,padx=2,pady=7)

        #gender
        lbl_gender=Label(upper_frame,font=('Arial',10,'bold'),text='Gender: ',bg='white')
        lbl_gender.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        #radio button gender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=670,y=77,width=170,height=30)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('arial',9,'bold'),bg='white')
        male.grid(row=0,column=0,padx=5,pady=2,sticky='W')

        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=('arial',9,'bold'),bg='white')
        female.grid(row=0,column=1,padx=5,pady=2,sticky='W')

        #wanted
        lbl_wanted=Label(upper_frame,font=('Arial',10,'bold'),text='Wanted: ',bg='white')
        lbl_wanted.grid(row=3,column=4,sticky=W,padx=2,pady=7)

        #radio button wanted
        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=670,y=110,width=170,height=30)

        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='YES',value='yes',font=('arial',9,'bold'),bg='white')
        yes.grid(row=0,column=0,padx=5,pady=2,sticky='W')

        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='NO',value='no',font=('arial',9,'bold'),bg='white')
        no.grid(row=0,column=1,padx=5,pady=2,sticky='W')

        #Button
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=180,width=630,height=40)

        #add button
        button_add=Button(button_frame,command=self.add_data,text='Save',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        button_add.grid(row=0,column=0,padx=3,pady=5)

        #update button
        button_update=Button(button_frame,command=self.update_data,text='Update',font=('arial',13,'bold'),width=14,bg='white',fg='black')
        button_update.grid(row=0,column=2,padx=3,pady=5)

        #clear button
        button_clear=Button(button_frame,command=self.clear_data,text='Clear',font=('arial',13,'bold'),width=14,bg='white',fg='black')
        button_clear.grid(row=0,column=4,padx=3,pady=5)

        #delete button
        button_delete=Button(button_frame,command=self.delete_data,text='Delete',font=('arial',13,'bold'),width=14,bg='red',fg='white')
        button_delete.grid(row=0,column=6,padx=3,pady=5)

        #background right side image
        img5=Image.open('images/SC.png')
        img5=img5.resize((158,156),Image.ANTIALIAS)
        self.photo5=ImageTk.PhotoImage(img5)

        self.img_5=Label(upper_frame,image=self.photo5)
        self.img_5.place(x=1100,y=5,width=158,height=156)

        #down_frame
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Criminal Information Table',font=('times new roman',15,'bold'),fg='red')
        down_frame.place(x=10,y=260,width=1484,height=250)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Criminal Record',font=('times new roman',10,'bold'),fg='red')
        search_frame.place(x=2,y=0,width=1474,height=60)

        lbl_search_by=Label(search_frame,font=('Arial',10,'bold'),text='Search By: ',bg='red',fg='white')
        lbl_search_by.grid(row=0,column=0,sticky=W,padx=2,pady=7)
        
        self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('Arial',10,'bold'),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_id','Criminal_number')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky='W',padx=5)
        
        self.var_search=StringVar()
        serach_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=('Arial',10,'bold'))
        serach_entry.grid(row=0,column=2,sticky='W',padx=5)

        #search_button
        button_search=Button(search_frame,command=self.search_data,text='Search',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        button_search.grid(row=0,column=3,sticky='W',padx=5)

        #show all button
        button_all=Button(search_frame,command=self.fetch_data,text='Show All',font=('arial',13,'bold'),width=14,bg='white',fg='black')
        button_all.grid(row=0,column=4,sticky='W',padx=5)

        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=2,y=60,width=1473,height=162)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal=ttk.Treeview(table_frame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal.xview)
        scroll_y.config(command=self.criminal.yview)

        self.criminal.heading('1',text='Case ID')
        self.criminal.heading('2',text='Criminal Nmber')
        self.criminal.heading('3',text='Crime Type')
        self.criminal.heading('4',text='Criminal Name')
        self.criminal.heading('5',text='Criminal Nickname')
        self.criminal.heading('6',text="Father's Name")
        self.criminal.heading('7',text='Arrest Date')
        self.criminal.heading('8',text='Date Of Crime')
        self.criminal.heading('9',text='Gender')
        self.criminal.heading('10',text='Address')
        self.criminal.heading('11',text='Age')
        self.criminal.heading('12',text='Birthmark')
        self.criminal.heading('13',text='Occupation')
        self.criminal.heading('14',text='Wanted')

        self.criminal['show']='headings'

        self.criminal.column('1',width=105)
        self.criminal.column('2',width=105)
        self.criminal.column('3',width=105)
        self.criminal.column('4',width=105)
        self.criminal.column('5',width=105)
        self.criminal.column('6',width=105)
        self.criminal.column('7',width=105)
        self.criminal.column('8',width=105)
        self.criminal.column('9',width=105)
        self.criminal.column('10',width=105)
        self.criminal.column('11',width=105)
        self.criminal.column('11',width=105)
        self.criminal.column('12',width=105)
        self.criminal.column('13',width=104)
        self.criminal.column('14',width=106)

        self.criminal.pack(fill=BOTH,expand=1)

        self.criminal.bind('<ButtonRelease>',self.get_cursor)

        self.fetch_data()

    #add function

    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Frields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Boomboomwoosh',database='criminal_database')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_case_id.get(),
                    self.var_criminal_no.get(),
                    self.var_crime_type.get(),
                    self.var_criminal_name.get(),
                    self.var_criminal_nickname.get(),
                    self.var_father_name.get(),
                    self.var_arrest_date.get(),
                    self.var_date_of_crime.get(),
                    self.var_gender.get(),
                    self.var_address.get(),
                    self.var_age.get(),
                    self.var_birthmark.get(),
                    self.var_occupation.get(),
                    self.var_wanted.get()
                ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record has been added successfully')
            except Exception as es:
                messagebox.showerror('Error',f'Due to{str(es)}')

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Boomboomwoosh',database='criminal_database')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal.delete(*self.criminal.get_children())
            for i in data:
                self.criminal.insert('',END,values=i)
            conn.commit()
        conn.close()
    
    #get cursor

    def get_cursor(self,event=""):
        cursor_row=self.criminal.focus()
        content=self.criminal.item(cursor_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1]),
        self.var_crime_type.set(data[2]),
        self.var_criminal_name.set(data[3]),
        self.var_criminal_nickname.set(data[4]),
        self.var_father_name.set(data[5]),
        self.var_arrest_date.set(data[6]),
        self.var_date_of_crime.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_address.set(data[9]),
        self.var_age.set(data[10]),
        self.var_birthmark.set(data[13]),
        self.var_occupation.set(data[12]),
        self.var_wanted.set(data[11])

    #update

    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Frields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure to update the criminal record')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Boomboomwoosh',database='criminal_database')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update criminal set Criminal_number=%s,Crime_Type=%s,criminalName=%s,NickName=%s,father_name=%s,ArrestDate=%s,DateOfCrime=%s,Gender=%s,Address=%s,age=%s,BirthMark=%s,occupation=%s,Wanted=%s where Case_id=%s',(
                    self.var_criminal_no.get(),
                    self.var_crime_type.get(),
                    self.var_criminal_name.get(),
                    self.var_criminal_nickname.get(),
                    self.var_father_name.get(),
                    self.var_arrest_date.get(),
                    self.var_date_of_crime.get(),
                    self.var_gender.get(),
                    self.var_address.get(),
                    self.var_age.get(),
                    self.var_birthmark.get(),
                    self.var_occupation.get(),
                    self.var_wanted.get(),
                    self.var_case_id.get()
                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record has been successfully updated')
            except Exception as es:
                messagebox.showerror('Error',f'Due to{str(es)}')

            
    #delete
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure?')
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Boomboomwoosh',database='criminal_database')
                    my_cursor=conn.cursor()
                    sql='delete from criminal where Case_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record has been successfully deleted')
            except Exception as es:
                messagebox.showerror('Error',f'Due to{str(es)}')
                

    #clear
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set(""),
        self.var_crime_type.set(""),
        self.var_criminal_name.set(""),
        self.var_criminal_nickname.set(""),
        self.var_father_name.set(""),
        self.var_arrest_date.set(""),
        self.var_date_of_crime.set(""),
        self.var_gender.set(""),
        self.var_address.set(""),
        self.var_age.set(""),
        self.var_birthmark.set(""),
        self.var_occupation.set(""),
        self.var_wanted.set("")
    
    #search
    def search_data(self):
        if self.var_com_search.get()=='':
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Boomboomwoosh',database='criminal_database')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from criminal where ' +str(self.var_com_search.get())+ " LIKE'%" +str(self.var_search.get()+ "%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal.delete(*self.criminal.get_children())
                    for i in rows:
                        self.criminal.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due to{str(es)}')
                conn.close()

if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()