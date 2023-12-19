import PIL
from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root 
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        #===========variable========================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_sequrityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        # ====================== bg image ======================
        self.bg=PIL.ImageTk.PhotoImage(file=r"C:\Users\rohit\Desktop\Login Form\photos\gok.jpg")
        bg_lb1=Label(self.root,image=self.bg)
        bg_lb1.place(x=0,y=0,relwidth=1,relheight=1)

        # ====================== left image ======================
        self.bg1=PIL.ImageTk.PhotoImage(file=r"C:\Users\rohit\Desktop\Login Form\photos\goku.jpg")
        left_lb1=Label(self.root,image=self.bg1)
        left_lb1.place(x=50,y=100,width=470,height=550)

        # ====================== Main Frame ======================
        frame=Frame(self.root,bg="black")
        frame.place(x=525,y=100,width=450,height=550)
        
        register_lb1=Label(frame,text="REGISTER HERE",font=("times new roman", 20, "bold"),fg="violet",bg="black")
        register_lb1.place(x=20,y=20)

        # label and enntry
        #=====================row1================================= 

        fname=Label(frame,text="First Name ", font=("times new roman", 10, "bold"),fg="white",bg="black")
        fname.place(x=25, y=80)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman", 10, "bold"))
        self.fname_entry.place(x=25, y=106)

        lname=Label(frame,text="Last Name  ", font=("times new roman", 10, "bold"),fg="white",bg="black")
        lname.place(x=225, y=80)

        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman", 10, "bold"))
        self.lname_entry.place(x=225, y=106)

         # row2 

        contact=Label(frame,text="Contact No", font=("times new roman", 10, "bold"),fg="white",bg="black")
        contact.place(x=25, y=140)

        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman", 10, "bold"))
        self.contact_entry.place(x=25, y=166)

        email=Label(frame,text="Email  ", font=("times new roman", 10, "bold"),fg="white",bg="black")
        email.place(x=225, y=140)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman", 10, "bold"))
        self.email_entry.place(x=225, y=166)

        # row3 

        selectsecq=Label(frame,text="Select Security Questions", font=("times new roman", 10, "bold"),fg="white",bg="black")
        selectsecq.place(x=25, y=200)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",8,"bold"),state="readonly")
        self.combo_security_Q["values"]=("select","Your Birth Place","Your Girlfriend name","Your Pet name")
        self.combo_security_Q.place(x=25,y=230,width=145)
        self.combo_security_Q.current(0)

        # selectsecq=ttk.Entry(frame,font=("times new roman", 10, "bold"))
        # selectsecq.place(x=25, y=226)

        secans=Label(frame,text="Security answers  ", font=("times new roman", 10, "bold"),fg="white",bg="black")
        secans.place(x=225, y=200)

        self.secans=ttk.Entry(frame,textvariable=self.var_sequrityA,font=("times new roman", 10, "bold"))
        self.secans.place(x=225, y=226)

        # row4

        passw=Label(frame,text="Password  ", font=("times new roman", 10, "bold"),fg="white",bg="black")
        passw.place(x=25, y=260)

        self.passw=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman", 10, "bold"))
        self.passw.place(x=25, y=286)

        cpassw=Label(frame,text="Confirm Password  ", font=("times new roman", 10, "bold"),fg="white",bg="black")
        cpassw.place(x=225, y=260)

        self.cpassw=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman", 10, "bold"))
        self.cpassw.place(x=225, y=286)

        #================CheckButtons===========#
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree All The Terms & Conditions",font=("times new roman",10,"bold"),onvalue=1,offvalue=0,bg="black",fg="blue")
        self.checkbtn.place(x=20,y=320)
        
        ###########------Buttons---------########
        
        b1=Button(frame,command=self.register_data,borderwidth=0,cursor="hand2",text="Register",font=("times new roman",11,"bold"),bd=3,relief=RIDGE,fg="White",bg="red",activeforeground="white",activebackground="red")
        b1.place(x=28,y=352,width=100)

        b2=Button(frame,text="Login Now",font=("times new roman",11,"bold"),bd=3,relief=RIDGE,fg="White",bg="blue",activeforeground="white",activebackground="Blue")
        b2.place(x=225,y=350,width=100)
        
        # img1=Image.open(r"C:\Users\rohit\Desktop\Login Form\photos\login.jpg")
        # img=img.resize((200,50),Image.ANTIALIAS)
        # self.photoimage=ImageTk.photoImage(img)
        # b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",10,"bold"))
        # b1.place(x=10,y=20,width=300)
       
       ########----Function Declaration---###########
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm poassword must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree all terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Ronny@3002",database="med_schema")
            my_cursor =conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User Already Exists by the Same Email,Try with Another Email.")
            else:
                my_cursor.execute("Insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_sequrityA.get(),
                                                                                        self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registeration Complete")

if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()

