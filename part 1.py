import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_table():
    conn = sqlite3.connect("change_requests.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS change_requests (Change Request TEXT, Customer TEXT, Color TEXT, Part Description TEXT, Berry Part Number TEXT, Drawing Number Ver TEXT, Mold TEXT, Material TEXT, Press Location TEXT, Process Press Data Sheet TEXT, Control Plan TEXT, Cavities TEXT)''')
    conn.commit()
    conn.close()

def insert_contact(cr, customer, color, pd, bpn, dnv, mold, material, pl, ppds, cp, cavities):
    conn = sqlite3.connect("change_requests.db")
    c = conn.cursor()
    c.execute("INSERT INTO change_requests VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (cr, customer, color, pd, bpn, dnv, mold, material, pl, ppds, cp, cavities))
    conn.commit()
    conn.close()

def save_change_request():
    cr = Change_Request.get()
    customer = Customer.get()
    color = Color.get()
    pd = Part_Description.get()
    bpn = Berry_Part_Number.get()
    dnv = Drawing_Number_and_Ver.get()
    mold = Mold.get()
    material = Material.get()
    pl = Press_Location.get()
    ppds = Press_Process_Data_Sheet.get()
    cp = Control_Plan.get()
    cavities = Cavities.get()

    if cr == "" or customer == "" or color == "" or pd =="" or bpn =="" or dnv =="" or mold =="" or material =="" or pl =="" or ppds =="" or cp =="" or cavities =="":
        messagebox.showerror("Error", "Please fill in all fields or type TBD")
        return

    insert_contact(cr, customer, color, pd, bpn, dnv, mold, material, pl, ppds, cp, cavities)
    messagebox.showinfo("Success", "Change Request saved successfully.")

    # Clear the entry fields after saving
    Change_Request.delete(0, tk.END)
    Customer.delete(0, tk.END)
    Color.delete(0, tk.END)
    Part_Description.delete(0, tk.END)
    Berry_Part_Number.delete(0, tk.END)
    Drawing_Number_and_Ver.delete(0, tk.END)
    Mold.delete(0, tk.END)
    Material.delete(0, tk.END)
    Press_Location.delete(0, tk.END)
    Press_Process_Data_Sheet.delete(0, tk.END)
    Control_Plan.delete(0, tk.END)
    Cavities.delete(0, tk.END)

root = tk.Tk()
root.title("CR Entry")

# Create table if not exists
create_table()

# Create labels and entry fields
tk.Label(root, text="Change Request:").grid(row=0, column=0, sticky="e")
Change_Request = tk.Entry(root)
Change_Request.grid(row=0, column=1)

tk.Label(root, text="Customer:").grid(row=1, column=0, sticky="e")
Customer = tk.Entry(root)
Customer.grid(row=1, column=1)

tk.Label(root, text="Color:").grid(row=2, column=0, sticky="e")
Color = tk.Entry(root)
Color.grid(row=2, column=1)

tk.Label(root, text="Part Description:").grid(row=3, column=0, sticky="e")
Part_Description = tk.Entry(root)
Part_Description.grid(row=3, column=1)

tk.Label(root, text="Berry (JDE) Part Number:").grid(row=4, column=0, sticky="e")
Berry_Part_Number = tk.Entry(root)
Berry_Part_Number.grid(row=4, column=1)

tk.Label(root, text="Drawing Number Ver. TEXT:").grid(row=5, column=0, sticky="e")
Drawing_Number_and_Ver = tk.Entry(root)
Drawing_Number_and_Ver.grid(row=5, column=1)

tk.Label(root, text="Mold:").grid(row=6, column=0, sticky="e")
Mold = tk.Entry(root)
Mold.grid(row=6, column=1)

tk.Label(root, text="Material:").grid(row=7, column=0, sticky="e")
Material = tk.Entry(root)
Material.grid(row=7, column=1)

tk.Label(root, text="Press Location:").grid(row=8, column=0, sticky="e")
Press_Location = tk.Entry(root)
Press_Location.grid(row=8, column=1)

tk.Label(root, text="Process Press Data Sheet:").grid(row=9, column=0, sticky="e")
Press_Process_Data_Sheet = tk.Entry(root)
Press_Process_Data_Sheet.grid(row=9, column=1)

tk.Label(root, text="Control Plan:").grid(row=10, column=0, sticky="e")
Control_Plan = tk.Entry(root)
Control_Plan.grid(row=10, column=1)

tk.Label(root, text="Cavities:").grid(row=11, column=0, sticky="e")
Cavities = tk.Entry(root)
Cavities.grid(row=11, column=1)

# Save button
save_button = tk.Button(root, text="Save", command=save_change_request)
save_button.grid(row=12, column=0, columnspan=2)

root.mainloop()