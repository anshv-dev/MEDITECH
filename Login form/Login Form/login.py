from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import PIL
from tkinter import messagebox
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
        Register_btn=Button(frame,text="New User Register",font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="Black",activeforeground="white",activebackground="black")
        Register_btn.place(x=15,y=330,width=160)

         #Forget Pass word button
         
        Forget_btn=Button(frame,text="Forget Password",font=("times new roman",12,"bold"),borderwidth=0,fg="White",bg="Black",activeforeground="white",activebackground="Black")
        Forget_btn.place(x=5,y=360,width=160)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="Rohit" and self.txtpass.get()=="Pass":
            messagebox.showinfo("Succeess","Welcome")
        else:
            messagebox.showerror("Invalid","Invalid Username & Password")
if __name__=="__main__":
    root=Tk()
    app=login_window(root)
    root.mainloop()