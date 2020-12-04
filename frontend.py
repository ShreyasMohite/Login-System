from tkinter import *
from tkinter.ttk import Notebook,Progressbar,Combobox
from tkinter import ttk
from backend import *
import tkinter.messagebox



class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("500x300")
        self.root.iconbitmap("logo590.ico")
        self.root.resizable(0,0)
        
        sid=StringVar()
        email=StringVar()
        password=StringVar()





        def on_enter1(e):
            but_Login['background']="black"
            but_Login['foreground']="cyan"  
        def on_leave1(e):
            but_Login['background']="SystemButtonFace"
            but_Login['foreground']="SystemButtonText"

            

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"


        def on_enter3(e):
            but_view['background']="black"
            but_view['foreground']="cyan"  
        def on_leave3(e):
            but_view['background']="SystemButtonFace"
            but_view['foreground']="SystemButtonText"

            

        def on_enter4(e):
            but_delete['background']="black"
            but_delete['foreground']="cyan"  
        def on_leave4(e):
            but_delete['background']="SystemButtonFace"
            but_delete['foreground']="SystemButtonText"

        def on_enter5(e):
            but_clear_tree['background']="black"
            but_clear_tree['foreground']="cyan"  
        def on_leave5(e):
            but_clear_tree['background']="SystemButtonFace"
            but_clear_tree['foreground']="SystemButtonText"

        
        def clear():
            sid.set("")
            email.set("")
            password.set("")


        def add_logins():
            if len(email.get())!=0:
                if len(password.get())!=0:
                    add_login(email.get(),password.get())
                    clear()
                else:
                    tkinter.messagebox.showerror("Eroor","Please Enter Password")
            else:
                tkinter.messagebox.showerror("Error","Please Enter Email")

        def view_logins():
            login_trees.delete(*login_trees.get_children())
            for row in view_login():
                login_trees.insert('',END,values=row)

        
        def clear_tree():
            login_trees.delete(*login_trees.get_children())


        def delete_logins(): 
            if(len(sid.get())!=0):      
                delete_login(sid.get())
                view_logins()
                clear()
            else:
                tkinter.messagebox.showerror("Error","Please Enter number to delete contact")





#===================frame====================#
        
        mainframe=Frame(self.root,width=500,height=300,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

#============================================#
         
        #notebook


        tabControl = Notebook(mainframe,width=491,height=270) 
  
        login_frame = Frame(tabControl,background="grey57") 
        view_login_frame = Frame(tabControl,background="grey87")        
        tabControl.add(login_frame, text ='Login') 
        tabControl.add(view_login_frame, text ='View Delete Login')
        tabControl.place(x=0,y=0)

#============================================#

        def  game(event):
            crow=login_trees.focus()
            contents=login_trees.item(crow)
            row=contents['values']
            sid.set(row[0])
            email.set(row[1])
            password.set(row[2])

        scol=Scrollbar(view_login_frame,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')

        login_trees=ttk.Treeview(view_login_frame,columns=("ID","Email","Password"),height=10,yscrollcommand=scol.set)
        login_trees.heading("ID",text="ID")
        login_trees.heading("Email",text="Email")
        login_trees.heading("Password",text="Password")
        login_trees['show']="headings"
        login_trees.column("ID",width=50,minwidth=10)
        login_trees.column("Email",width=225,minwidth=40)
        login_trees.column("Password",width=196,minwidth=40)
        login_trees.place(x=0,y=0)

        login_trees.bind('<ButtonRelease-1>',game)



        but_view=Button(view_login_frame,text="View",font=('times new roman',13),width=14,cursor="hand2",command=view_logins)
        but_view.place(x=10,y=233)
        but_view.bind("<Enter>",on_enter3)
        but_view.bind("<Leave>",on_leave3)

        but_delete=Button(view_login_frame,text="Delete",font=('times new roman',13),width=14,cursor="hand2",command=delete_logins)
        but_delete.place(x=167,y=233)
        but_delete.bind("<Enter>",on_enter4)
        but_delete.bind("<Leave>",on_leave4)

        but_clear_tree=Button(view_login_frame,text="Clear",font=('times new roman',13),width=14,cursor="hand2",command=clear_tree)
        but_clear_tree.place(x=327,y=233)
        but_clear_tree.bind("<Enter>",on_enter5)
        but_clear_tree.bind("<Leave>",on_leave5)







#==============================================#
        
        
        ent_id=Entry(login_frame,width=3,font=('times new roman',15),relief="ridge",bd=3,textvariable=sid)
        ent_id.place(x=5,y=5)

        
        lab_email=Label(login_frame,text="Email",font=('times new roman',15),bg="grey57",fg="white")
        lab_email.place(x=200,y=20)

        ent_email=Entry(login_frame,width=40,font=('times new roman',15),relief="ridge",bd=3,textvariable=email)
        ent_email.place(x=40,y=60)


        lab_password=Label(login_frame,text="Password",font=('times new roman',15),bg="grey57",fg="white")
        lab_password.place(x=180,y=100)

        ent_password=Entry(login_frame,width=40,font=('times new roman',15),show="*",relief="ridge",bd=3,textvariable=password)
        ent_password.place(x=40,y=140)


        but_Login=Button(login_frame,text="Login",font=('times new roman',16),width=15,cursor="hand2",command=add_logins)
        but_Login.place(x=40,y=200)
        but_Login.bind("<Enter>",on_enter1)
        but_Login.bind("<Leave>",on_leave1)

        but_clear=Button(login_frame,text="Clear",font=('times new roman',16),width=15,cursor="hand2",command=clear)
        but_clear.place(x=255,y=200)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)









if __name__ == "__main__":
    root=Tk()
    Login(root)
    root.mainloop()