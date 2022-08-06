from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox

class Cust_wind:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1295x550+0+0")
        self.root.title("Logout Window")
        self.var_logout = StringVar()
        self.var_login = StringVar()
        self.var_permission = StringVar()
        
    #Background
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\HP\Downloads\Background.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
    # title
        lbl_title = Label(self.root, text="LOGOUT WINDOW", font=(
            "times new roman", 22, "bold"), bg="Black", fg="White", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1290, height=50)
     
    # label frames
        lbl_frame = LabelFrame(self.root, bd=2, relief=RIDGE, font=(
            "times new roman", 12, "bold"), padx=2, pady=2)
        lbl_frame.place(x=0, y=50, width=1290, height=490)
        
    #left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\HP\Downloads\left.jpg")
        left_lbl=Label(lbl_frame,image=self.bg1)
        left_lbl.place(x=0,y=0,width=1400,height=480)

    # buttonsframe
        btn_frame = Frame(lbl_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=505, y=305, width=241, height=59)
        
    #Textframe
        txt_frame = LabelFrame(self.root, bd=2, relief=RIDGE, font=(
            "times new roman", 12, "bold"))
        txt_frame.place(x=50, y=100, width=280, height=59)

    # Texts
        lbl_cust = Label(txt_frame, text="HELLO user :)\n Click button below to EXIT", font=(
            "arial", 16, "bold"),bg="Maroon",fg="Black")
        lbl_cust.grid(row=0, column=0, sticky=W)

    # Buttons
        logout = Button(btn_frame, text="Logout", command=self.mlogout, font=(
            "arial", 19, "bold"), bg="Black", fg="White", width=15)
        logout.grid(row=0, column=1, padx=1)
        
    def mlogout(self):
        mlogout=messagebox.askyesno("Hotel Management System", "Do you want to logout", parent=self.root)
        if mlogout>0:
            exit(0)
        else:
            if not mlogout:
                return

if __name__ == "__main__":
    root = Tk()
    obj = Cust_wind(root)
    root.mainloop()
