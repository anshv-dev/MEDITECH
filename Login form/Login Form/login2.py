from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import PIL
from tkinter import messagebox
import mysql.connector

# =============Function Defination and object declaration=========================

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()

class login_window:
    def __init__(self,root):
        self.root=root 
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=PIL.ImageTk.PhotoImage(file=r"C:\Users\rohit\Desktop\Login Form\photos\ap.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=150,width=340,height=450)
        
        image1=Image.open(r"C:\Users\rohit\Desktop\Login Form\photos\admin.jpg")
        image1=image1.resize((70,70))#Image.ANTIALIAS
        self.photoimage1=ImageTk.PhotoImage(image1)
        lblimage1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimage1.place(x=580,y=160,width=200,height=100 )
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
        
        
        #labels
        username=lbl=Label(frame,text="Username",font=("times new roman",12,"bold"),fg="white",bg="Black")
        username.place(x=38,y=140)

        self.txtuser=ttk.Entry(frame,font=("times new roman",12,"bold"))
        self.txtuser.place(x=20,y=165,width=250)

        userpass=lbl=Label(frame,text="Password",font=("times new roman",12,"bold"),fg="white",bg="Black")
        userpass.place(x=38,y=200)

       
        self.txtpass=ttk.Entry(frame,font=("times new roman",12,"bold"))
        self.txtpass.place(x=20,y=225,width=250)

        ########ICON IMAGES#######
        
        image3=Image.open(r"C:\Users\rohit\Desktop\Login Form\photos\user.jpg")
        image3=image3.resize((20,20))#Image.ANTIALIAS
        self.photoimage3=ImageTk.PhotoImage(image3)
        lblimage3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimage3.place(x=518,y=292,width=20,height=20 )

        image2=Image.open(r"C:\Users\rohit\Desktop\Login Form\photos\pass.jpg")
        image2=image2.resize((20,20))#Image.ANTIALIAS
        self.photoimage2=ImageTk.PhotoImage(image2)
        lblimage2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimage2.place(x=518,y=352,width=20,height=20 )

        #Login Button
        login_btn=Button(frame,command=self.login,text="Login",font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="White",bg="red",activeforeground="white",activebackground="red")
        login_btn.place(x=95,y=290,width=120,height=35)

        #Register Button
        Register_btn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="Black",activeforeground="white",activebackground="black")
        Register_btn.place(x=15,y=330,width=160)

        #Forget Pass word button
         
        Forget_btn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",12,"bold"),borderwidth=0,fg="White",bg="Black",activeforeground="white",activebackground="Black")
        Forget_btn.place(x=5,y=360,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="Rohit" and self.txtpass.get()=="Pass":
            messagebox.showinfo("Succeess","Welcome")
        else:
            #connection with database using mysql
            conn=mysql.connector.connect(host="localhost",user="root",password="Ronny@3002",database="med_schema")
            my_cursor =conn.cursor()
            my_cursor.execute("select * from register where email=%s and password= %s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                        ))
            #fetching data from the database
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                messagebox.showinfo("Success","Successfully logged in")
                messagebox.showinfo("404","hum pai to hai naw")
                return
                # open_main=messagebox.askyesno("YesNo","Access only admin")
                # if open_main>0:
                #     self.new_window=Toplevel(self.new_window)
                #     self.app=Hospital(self.new_window)
                # else:
                #     if not open_main:
                #         return
            conn.commit()
            conn.close()

            # messagebox.showerror("Invalid","Invalid Username & Password")
    #====================== reset password ========================
    def reset_pass(self):
        if self.combo_security_Q.get() == "select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.secans.get()=="":
            messagebox.showerror("Error","Please Enter the valid answer",parent=self.root2)
        elif self.new_password.get()=="":
            messagebox.showerror("Error","Please Enter the new Password",parent=self.root2)
        else:
            
            #connection with database using mysql
            conn=mysql.connector.connect(host="localhost",user="root",password="Ronny@3002",database="med_schema")
            my_cursor =conn.cursor()
            
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.secans.get())
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Please Enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value) 
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset ,please login with new Password")
                self.root2.destroy()

    ######################====================== forget password wimdow ======================#########################
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Enter the valid Email address to reset the password")
        else:
            #connection with database using mysql
            conn=mysql.connector.connect(host="localhost",user="root",password="Ronny@3002",database="med_schema")
            my_cursor =conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Please enter valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("650x450+610+170")

                l=Label(self.root2,text="Forgot Passowrd",font=("times new roman",20,"bold"),fg="red", bg="white")
                l.place(x=0,y=10,relwidth=1)

                selectsecq=Label(self.root2,text="Select Security Questions", font=("times new roman", 10, "bold"),fg="black",bg="white")
                selectsecq.place(x=50, y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",8,"bold"),state="readonly")
                self.combo_security_Q["values"]=("select","Your Birth Place","Your Girlfriend name","Your Pet name")
                self.combo_security_Q.place(x=50,y=110,width=145)
                self.combo_security_Q.current(0)

                # selectsecq=ttk.Entry(frame,font=("times new roman", 10, "bold"))
                # selectsecq.place(x=25, y=226)

                secans=Label(self.root2,text="Security answers  ", font=("times new roman", 10, "bold"),fg="black",bg="white")
                secans.place(x=50, y=150)

                self.secans=ttk.Entry(self.root2,font=("times new roman", 10, "bold"))
                self.secans.place(x=50, y=180)

                new_password=Label(self.root2,text="New Password", font=("times new roman", 10, "bold"),fg="black",bg="white")
                new_password.place(x=50, y=220)

                self.new_password=ttk.Entry(self.root2,font=("times new roman", 10, "bold"))
                self.new_password.place(x=50, y=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)

#============Register=====================
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

        b2=Button(frame,text="Login Now",command=self.return_login,font=("times new roman",11,"bold"),bd=3,relief=RIDGE,fg="White",bg="blue",activeforeground="white",activebackground="Blue")
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
            #connection with database using mysql
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
    
    def return_login(self):
        self.root.destroy()

if __name__=="__main__":
    main()
    # root=Tk()
    # app=login_window(root)
    # root.mainloop()