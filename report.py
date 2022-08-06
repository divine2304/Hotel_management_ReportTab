from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class Cust_wind:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1295x550+0+0")
        self.root.title("Report Window")

        # variables
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_criteria = StringVar()
        self.var_summary = StringVar()

        # title
        lbl_title = Label(self.root, text="ADD REPORT DETAILS", font=(
            "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # logo
        img0 = Image.open(r"C:\Users\HP\Downloads\logo.jpg")
        img0 = img0.resize((100, 40), Image.ANTIALIAS)
        self.photoimg0 = ImageTk.PhotoImage(img0)

        lblimg = Label(self.root, image=self.photoimg0, bd=4, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # label frames
        lbl_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Report Details", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_frame.place(x=5, y=50, width=425, height=490)

        #labels and entries

        # ref
        lbl_cust_ref = Label(lbl_frame, text="Customer Ref", font=(
            "arial", 13, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        enty_ref = ttk.Entry(lbl_frame, textvariable=self.var_ref, width=29, font=(
            "arial", 13, "bold"), state="readonly")
        enty_ref.grid(row=0, column=1)

        # customer name
        lblname = Label(lbl_frame, text="Customer Name",
                        font=("arial", 12, "bold"), padx=2, pady=6)
        lblname.grid(row=1, column=0, sticky=W)

        txtname = ttk.Entry(lbl_frame, textvariable=self.var_name,
                            width=29, font=("arial", 13, "bold"))
        txtname.grid(row=1, column=1)

        # email
        lblemail = Label(lbl_frame, text="Email",
                         font=("arial", 12, "bold"), padx=2, pady=6)
        lblemail.grid(row=2, column=0, sticky=W)
        txtemail = ttk.Entry(
            lbl_frame, textvariable=self.var_email, width=29, font=("arial", 13, "bold"))
        txtemail.grid(row=2, column=1)

        # criteria
        lblbranch = Label(lbl_frame, text="Field of report",
                          font=("arial", 12, "bold"), padx=2, pady=6)
        lblbranch.grid(row=3, column=0, sticky=W)
        combo_branch = ttk.Combobox(
            lbl_frame, textvariable=self.var_criteria, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_branch["value"] = ("Service related complaint", "Attitudinal complaint", "Mechanical Complaint",
                                 "Food related complaint", "Room related complaint", "Other(Please elaborate)")
        combo_branch.current(0)
        combo_branch.grid(row=3, column=1)

        # summary
        lblsummary = Label(lbl_frame, text="Summary",
                           font=("arial", 12, "bold"), padx=2, pady=6)
        lblsummary.grid(row=4, column=0, sticky=W)
        txtsummary = ttk.Entry(
            lbl_frame, textvariable=self.var_summary, width=29, font=("arial", 13, "bold"))
        txtsummary.grid(row=4, column=1)

        # buttonsframe
        btn_frame = Frame(lbl_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        # Buttons
        add = Button(btn_frame, text="ADD", command=self.add_data, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        add.grid(row=0, column=0, padx=1)

        update = Button(btn_frame, text="UPDATE", command=self.update_now, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        update.grid(row=0, column=1, padx=1)

        clear = Button(btn_frame, text="CLEAR", command=self.deletem, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        clear.grid(row=0, column=2, padx=1)

        reset = Button(btn_frame, text="RESET", command=self.reset, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        reset.grid(row=0, column=3, padx=1)

        # table
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Report Details", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        table_frame.place(x=435, y=50, width=860, height=490)

        # tableframe
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View details and summary", font=(
            "arial", 12, "bold"), padx=2)
        table_frame.place(x=435, y=50, width=860, height=490)

        lblsearch = Label(table_frame, font=(
            "arial", 12, "bold"), text="Search using:-", bg="red", fg="white")
        lblsearch.grid(row=0, column=0, sticky=W, padx=2)

        # table box
        #search and elaborate

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=(
            "arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Criteria", "Ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtsearch = ttk.Entry(table_frame, textvariable=self.txt_search, font=(
            "arial", 13, "bold"), width=24)
        txtsearch.grid(row=0, column=2, padx=2)

        Search = Button(table_frame, text="Search", command=self.search_m, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        Search.grid(row=0, column=3, padx=1)

        elaborate = Button(table_frame, text="Show all", command=self.fetch_data, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        elaborate.grid(row=0, column=4, padx=1)

        # data table elaboration
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_dit_table = ttk.Treeview(details_table, column=(
            "Ref", "Name", "Email", "Criteria", "Summary"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_dit_table.xview)
        scroll_y.config(command=self.cust_dit_table.yview)

        self.cust_dit_table.heading("Ref", text="Ref")
        self.cust_dit_table.heading("Name", text="Name")
        self.cust_dit_table.heading("Email", text="Email")
        self.cust_dit_table.heading("Criteria", text="Criteria")
        self.cust_dit_table.heading("Summary", text="Summary")

        self.cust_dit_table["show"] = "headings"
        self.cust_dit_table.pack(fill=BOTH, expand=1)
        self.cust_dit_table.bind("<ButtonRelease-1>", self.get_curser)
        self.fetch_data()

    def add_data(self):
        if self.var_email.get() == "" or self.var_criteria.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="divya", database="sqlbegineer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_criteria.get(),
                    self.var_summary.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Reported", "Report successfully added", parent=self.root)

            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="divya", database="sqlbegineer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.cust_dit_table.delete(*self.cust_dit_table.get_children())
            for i in rows:
                self.cust_dit_table.insert("", END, values=i)
            conn.commit()
            conn.close()

    def get_curser(self, event=""):
        cursor_row = self.cust_dit_table.focus()
        content = self.cust_dit_table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_criteria.set(row[3]),
        self.var_summary.set(row[4])

    def update_now(self):
        if self.var_criteria.get() == "":
            messagebox.showerror(
                "Error", "Please enter proper reason", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="divya", database="sqlbegineer")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name=%s,Email=%s,Criteria=%s,Summary=%s where Ref=%s", (


                self.var_name.get(),
                self.var_email.get(),
                self.var_criteria.get(),
                self.var_summary.get(),
                self.var_ref.get()
            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                "Updated", "Customer details are updated successfully", parent=self.root)

    def deletem(self):
        deletem = messagebox.askyesno(
            "Report Tab", "Do you want to delete this information", parent=self.root)
        if deletem > 0:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="divya", database="sqlbegineer")
            my_cursor = conn.cursor()
            query = "delete from customer where Ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not deletem:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x)),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_summary.set("")

    def search_m(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="divya", database="sqlbegineer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where " +
                          str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_dit_table.delete(*self.cust_dit_table.get_children())
            for i in rows:
                self.cust_dit_table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Cust_wind(root)
    root.mainloop()
