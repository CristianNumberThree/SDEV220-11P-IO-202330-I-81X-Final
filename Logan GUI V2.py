import tkinter as tk
from tkinter import messagebox
from tkinter import *
import sqlite3

root = tk.Tk()
root.title("Main Menu")
root.geometry("250x150")

def MainProgram():
    # Function to create the database table if it does not exist
    def create_table():
        conn = sqlite3.connect("change_requests.db")
        c = conn.cursor()
        c.execute( '''CREATE TABLE IF NOT EXISTS change_requests (
            Change_Request TEXT, 
            Customer TEXT, 
            Color TEXT, 
            Part_Description TEXT, 
            Berry_Part_Number TEXT, 
            Drawing_Number_Ver TEXT, 
            Mold TEXT, 
            Material TEXT, 
            Press_Location TEXT, 
            Process_Press_Data_Sheet TEXT, 
            Control_Plan TEXT, 
            Cavities TEXT)''')
        conn.commit()
        conn.close()

    # Function to insert a change request into the database
    def insert_contact(cr, customer, color, pd, bpn, dnv, mold, material, pl, ppds, cp, cavities):
        conn = sqlite3.connect("change_requests.db")
        c = conn.cursor()
        c.execute("INSERT INTO change_requests VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
            (cr, customer, color, pd, bpn, dnv, mold, material, pl, ppds, cp, cavities))
        conn.commit()
        conn.close()

    # Function to save the change request data
    def save_change_request():
        cr = Change_Request.get()
        customer = Customer.get()
        color = Color.get()
        pd = Part_Description.get()
        bpn = Berry_Part_Number.get()
        dnv = Drawing_Number_and_Ver.get()
        mold = Mold_Options.get()
        material = Material.get()
        pl = Press_Location.get()
        ppds = Press_Process_Data_Sheet.get()
        cp = Control_Plan.get()
        cavities = Cavities.get()

        if cr == "" or customer == "" or color == "" or pd == "" or bpn == "" or dnv == "" or mold == "" or material == "" or pl == "" or ppds == "" or cp == "" or cavities == "":
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
        Mold_Type.set(list(mold_options.keys())[0])
        Mold_Options.set("")  # Clear mold options
        Material.delete(0, tk.END)
        Press_Location.delete(0, tk.END)
        Press_Process_Data_Sheet.delete(0, tk.END)
        Control_Plan.delete(0, tk.END)
        Cavities.delete(0, tk.END)

    # Function to generate a report from the database
    def generate_report():
        conn = sqlite3.connect("change_requests.db")
        c = conn.cursor()
        c.execute("SELECT * FROM change_requests ORDER BY rowid DESC LIMIT 1")  # Fetch the last entry
        data = c.fetchone()
        conn.close()

        if data is None:
            messagebox.showinfo("No Data", "No change request data found.")
            return

        report_text = "Change Request Report:\n\n"
        report_text += f"Change Request: {data[0]}\n"
        report_text += f"Customer: {data[1]}\n"
        report_text += f"Color: {data[2]}\n"
        report_text += f"Part Description: {data[3]}\n"
        report_text += f"Berry (JDE) Part Number: {data[4]}\n"
        report_text += f"Drawing Number and Ver.: {data[5]}\n"
        report_text += f"Mold: {data[6]}\n"
        report_text += f"Material: {data[7]}\n"
        report_text += f"Press Location: {data[8]}\n"
        report_text += f"Process Press Data Sheet: {data[9]}\n"
        report_text += f"Control Plan: {data[10]}\n"
        report_text += f"Cavities: {data[11]}\n"

        # Additional text to print in the report
        additional_text = "Qualification Plan for {}\nSampling Plan and Acceptance Criteria: ".format(data[0])

        # Concatenate the additional text to the report
        report_text += "\n\n" + additional_text

        # Display the report in a messagebox
        messagebox.showinfo("Change Request Report", report_text)

    def update_mold_options(*args):
        selected_type = Mold_Type.get()
        options = mold_options[selected_type]
        Mold_Options_Menu['menu'].delete(0, 'end')
        for option in options:
            Mold_Options_Menu['menu'].add_command(label=option, command=tk._setit(Mold_Options, option))

    program = tk.Tk()
    program.title("CR Entry")

    # Create table if not exists
    create_table()

    # Create dictionaries to hold mold options for each mold type
    mold_options = {
        "MLX Molds": [
            "75624B" , "75624C" , "75624D" , "75624E", "75624F" , "75624G" , "75624H" , "75624J" ,
            "75624K" , "75624L" , "75624M" , "75624N" , "76032A" , "76032B" , "76032C" , "76032D" ,
            "76032E" , "76032F" , " 76032G"
        ],
        "Injection Molds": [
            "1941" , "1942" , "5838" , "30980" , "31098" , "31157" , "31167" , "31311" , "A-1638-A1" ,
            "ACM-055" , "ACM-057" , "ACM-058" , "ACM-059" , "APT-01934" , "CM-0064" , "CM-8417" , "CM-8418" ,
            "CM-8418A" , "CM-8445" , "CM-8552" , "CM-8566" , "CM-8566-A" , "CM-8567-A" , "CM-8629" , "CM-8728" ,
            "CM-8729" , "CM-8736" , "CM-8736-A" , "CM-8737-1" , "CM-8737-A" , "CM-8740" , "CM-8758" , "CM-8760" ,
            "CM-8776-A" , "CM-8776-B" , "CM-8776-C" , "CM-8815" , "CM-8816" , "CM-8817" , "CM-8886" , "CM-8886A" ,
            "CM-8902" , "CM-8903" , "CM-8904" , "CM-8905" , "CM-8907" , "CM-8926" , "CM-8990" , "CM-8992" , "CM-8993",
            "CVR-01935" , "JM-5287-1" , "JM-5288-1" , "JM-5289-1" , "JM-5449-1" , "JM-5666-2" , "MJ-0924-A" , "MJ-0941" ,
            "MJ-0941-A" , "MJ-0941-B" , "MJ-0941-C" , "MJ-0942-A" , "MJ-0943-A" , "MJ-1327" , "MJ-1331" , "MJ-1333"
        ],
        "IBM Molds": [
            "4287" , "4736" , "4780" , "5012" , "5035" , "5052" , "5085" , "5087" , "5088" , "5122" , "5125" , "5153" ,
            "5198" , "5219" , "5237" , "5240" , "5264" , "5265" , "5297" , "5308" , "5309" , "5324" , "5325" , "5359" ,
            "5360" , "5361" , "5362" , "5365" , "5379" , "5412" , "5429" , "5430" , "5436" , "5437" , "5439" , "5462" ,
            "5464" , "5491" , "5492" , "5493" , "5497" , "5532" , "5549" , "5566" , "5593" , "5597" , "5603" , "5605" ,
            "5611" , "5617" , "5625" , "5648" , "5660" , "5711" , "5720" , "5721" , "5750" , "5848" , "5883" , "5943" ,
            "5945" , "5998" , "6006" , "6007" , "6010" , "6022" , "6033" , "6036" , "6039" , "6040" , "6043" , "6044" ,
            "6045" , "6046" , "6047" , "7031" , "0361" , "4377" , "4379/4738" , "4380" , "4643/4739" , "4711" , "4730" ,
            "5019" , "5266A HDPE" , "5266A LUGS" , "5266A PP" , "5422B" , "5422 C/D/E" , "5436 Private Mold" , "5548" ,
            "5566 With Lugs" , "5655 HD" , "5655 PP" , "J120-1" , "J148"
            ]
    }

    # Create labels and entry fields
    tk.Label(program, text="Change Request:").grid(row=0, column=0, sticky="e")
    Change_Request = tk.Entry(program)
    Change_Request.grid(row=0, column=1)

    # Customer
    tk.Label(program, text="Customer:").grid(row=1, column=0, sticky="e")
    Customer = tk.Entry(program)
    Customer.grid(row=1, column=1)

    # Color
    tk.Label(program, text="Color:").grid(row=2, column=0, sticky="e")
    Color = tk.Entry(program)
    Color.grid(row=2, column=1)

    # Part Description
    tk.Label(program, text="Part Description:").grid(row=3, column=0, sticky="e")
    Part_Description = tk.Entry(program)
    Part_Description.grid(row=3, column=1)

    # Berry (JDE) Part Number
    tk.Label(program, text="Berry (JDE) Part Number:").grid(row=4, column=0, sticky="e")
    Berry_Part_Number = tk.Entry(program)
    Berry_Part_Number.grid(row=4, column=1)

    # Drawing Number and Ver.
    tk.Label(program, text="Drawing Number and Ver.:").grid(row=5, column=0, sticky="e")
    Drawing_Number_and_Ver = tk.Entry(program)
    Drawing_Number_and_Ver.grid(row=5, column=1)

    # Create labels for Mold Type and Mold
    tk.Label(program, text="Mold Type:").grid(row=6, column=0, sticky="e")
    Mold_Type = tk.StringVar(program)
    Mold_Type.set(list(mold_options.keys())[0])  # Set default selected option
    Mold_Type_Options = tk.OptionMenu(program, Mold_Type, *mold_options.keys())
    Mold_Type_Options.grid(row=6, column=1)

    tk.Label(program, text="Mold:").grid(row=7, column=0, sticky="e")
    Mold_Options = tk.StringVar(program)
    Mold_Options_Menu = tk.OptionMenu(program, Mold_Options, "")
    Mold_Options_Menu.grid(row=7, column=1)

    # Bind the update_mold_options function to the Mold_Type variable
    Mold_Type.trace('w', update_mold_options)

    # Material
    tk.Label(program, text="Material:").grid(row=8, column=0, sticky="e")
    Material = tk.Entry(program)
    Material.grid(row=8, column=1)

    # Press Location
    tk.Label(program, text="Press Location:").grid(row=9, column=0, sticky="e")
    Press_Location = tk.Entry(program)
    Press_Location.grid(row=9, column=1)

    # Process Press Data Sheet
    tk.Label(program, text="Process Press Data Sheet:").grid(row=10, column=0, sticky="e")
    Press_Process_Data_Sheet = tk.Entry(program)
    Press_Process_Data_Sheet.grid(row=10, column=1)

    # Control Plan
    tk.Label(program, text="Control Plan:").grid(row=11, column=0, sticky="e")
    Control_Plan = tk.Entry(program)
    Control_Plan.grid(row=11, column=1)
    
    # Cavities
    tk.Label(program, text="Cavities:").grid(row=12, column=0, sticky="e")
    Cavities = tk.Entry(program)
    Cavities.grid(row=12, column=1)

    # Save button
    save_button = tk.Button(program, text="Save", command=save_change_request)
    save_button.grid(row=13, column=0, columnspan=2)

    # Generate report button
    report_button = tk.Button(program, text="Generate Report", command=generate_report)
    report_button.grid(row=14, column=0, columnspan=2)

    #Exit
    btnExit = tk.Button(program, text ='Exit', fg ='red', command=program.destroy)
    btnExit.grid(row=15, column=0, columnspan=2)

btnOpenProgram=Button(root, text="Open Program", command=MainProgram).pack(pady=10)
btnQuit = Button(root, text ='Quit', fg ='red', command=root.destroy)
btnQuit.pack()

root.mainloop()
