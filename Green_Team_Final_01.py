import tkinter as tk
from tkinter import messagebox
import sqlite3
import pyodbc

class DatabaseManager:
    def __init__(self, db_name="change_requests.db"):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS change_requests(
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

    def insert_change_request(self, cr, customer, color, pd, bpn, dnv, mold, material, pl, ppds, cp, cavities):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("INSERT INTO change_requests VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (cr, customer, color, pd, bpn, dnv, mold, material, pl, ppds, cp, cavities))        
        conn.commit()
        conn.close()

    def fetch_last_change_request(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM change_requests ORDER BY rowid DESC LIMIT 1")
        data = c.fetchone()
        conn.close()
        return data

    def fetch_infinity_query_results(self):
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=FRINDBS001;DATABASE=Infinity Proficient;UID=jdillehay_2;PWD=dxk#An8^Y@^G(m3s3wJE8')
        cursor = conn.cursor()
        sql_query = '''
        Select P.F_NAME, T.F_NAME, S.F_USL, S.F_TAR, S.F_LSL
        FROM [Infinity Proficient].[dbo].[PART_DAT] as P
        INNER join [Infinity Proficient].[dbo].[SPEC_LIM] as S
        on P.F_NAME = '5660a 60cc square'
        and P.F_PART = S.F_PART
        Inner Join [Infinity Proficient].[dbo].[TEST_DAT] as T
        on S.F_TEST = T.F_TEST
        '''
        cursor.execute(sql_query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results

class ChangeRequestEntryForm:
    def __init__(self, parent, db_manager, mold_options):
        self.parent = parent
        self.db_manager = db_manager
        self.mold_options = mold_options
        self.program = tk.Toplevel(self.parent)
        self.program.title("CR Entry")

        #Create UI
        self.create_ui()

    def create_ui(self):
        #Create labels and entry fields
        tk.Label(self.program, text="Change Request:").grid(row=0, column=0, sticky="e")
        self.Change_Request = tk.Entry(self.program)
        self.Change_Request.grid(row=0, column=1)

        # Customer
        tk.Label(self.program, text="Customer:").grid(row=1, column=0, sticky="e")
        self.Customer = tk.Entry(self.program)
        self.Customer.grid(row=1, column=1)

        # Color
        tk.Label(self.program, text="Color:").grid(row=2, column=0, sticky="e")
        self.Color = tk.Entry(self.program)
        self.Color.grid(row=2, column=1)

        # Part Description
        tk.Label(self.program, text="Part Description:").grid(row=3, column=0, sticky="e")
        self.Part_Description = tk.Entry(self.program)
        self.Part_Description.grid(row=3, column=1)

        # Berry (JDE) Part Number
        tk.Label(self.program, text="Berry (JDE) Part Number:").grid(row=4, column=0, sticky="e")
        self.Berry_Part_Number = tk.Entry(self.program)
        self.Berry_Part_Number.grid(row=4, column=1)

        # Drawing Number and Ver.
        tk.Label(self.program, text="Drawing Number and Ver.:").grid(row=5, column=0, sticky="e")
        self.Drawing_Number_and_Ver = tk.Entry(self.program)
        self.Drawing_Number_and_Ver.grid(row=5, column=1)

        # Create labels for Mold Type and Mold
        tk.Label(self.program, text="Mold Type:").grid(row=6, column=0, sticky="e")
        self.Mold_Type = tk.StringVar(self.program)
        self.Mold_Type.set(list(self.mold_options.keys())[0])  # Set default selected option
        self.Mold_Type_Options = tk.OptionMenu(self.program, self.Mold_Type, *self.mold_options.keys())
        self.Mold_Type_Options.grid(row=6, column=1)

        tk.Label(self.program, text="Mold:").grid(row=7, column=0, sticky="e")
        self.Mold_Options = tk.StringVar(self.program)
        self.Mold_Options_Menu = tk.OptionMenu(self.program, self.Mold_Options, "")
        self.Mold_Options_Menu.grid(row=7, column=1)

        # Bind the update_mold_options function to the Mold_Type variable
        self.Mold_Type.trace('w', self.update_mold_options)

        # Material
        tk.Label(self.program, text="Material:").grid(row=8, column=0, sticky="e")
        self.Material = tk.Entry(self.program)
        self.Material.grid(row=8, column=1)

        # Press Location
        tk.Label(self.program, text="Press Location:").grid(row=9, column=0, sticky="e")
        self.Press_Location = tk.Entry(self.program)
        self.Press_Location.grid(row=9, column=1)

        # Process Press Data Sheet
        tk.Label(self.program, text="Process Press Data Sheet:").grid(row=10, column=0, sticky="e")
        self.Press_Process_Data_Sheet = tk.Entry(self.program)
        self.Press_Process_Data_Sheet.grid(row=10, column=1)

        # Control Plan
        tk.Label(self.program, text="Control Plan:").grid(row=11, column=0, sticky="e")
        self.Control_Plan = tk.Entry(self.program)
        self.Control_Plan.grid(row=11, column=1)
        
        # Cavities
        tk.Label(self.program, text="Cavities:").grid(row=12, column=0, sticky="e")
        self.Cavities = tk.Entry(self.program)
        self.Cavities.grid(row=12, column=1)

        # Save button
        save_button = tk.Button(self.program, text="Save", command=self.save_change_request)
        save_button.grid(row=13, column=0, columnspan=2)

        # Generate report button
        report_button = tk.Button(self.program, text="Generate Report", command=self.generate_report)
        report_button.grid(row=14, column=0, columnspan=2)

        # Exit button
        btnExit = tk.Button(self.program, text='Exit', fg='red', command=self.program.destroy)
        btnExit.grid(row=15, column=0, columnspan=2)

    def update_mold_options(self, *args):
        selected_mold_type = self.Mold_Type.get()
        self.Mold_Options.set("") #Reset selected mold option
        menu = self.Mold_Options_Menu["menu"]
        menu.delete(0, "end")
        for mold in self.mold_options[selected_mold_type]:
            menu.add_command(label=mold, command=lambda value=mold: self.Mold_Options.set(value))

    def save_change_request(self):
        #Get data from entry fields
        cr = self.Change_Request.get()
        customer = self.Customer.get()
        color = self.Color.get()
        part_description = self.Part_Description.get()
        berry_part_number = self.Berry_Part_Number.get()
        drawing_number_and_ver = self.Drawing_Number_and_Ver.get()
        mold = self.Mold_Options.get()
        material = self.Material.get()
        press_location = self.Press_Location.get()
        process_press_data_sheet = self.Press_Process_Data_Sheet.get()
        control_plan = self.Control_Plan.get()
        cavities = self.Cavities.get()

        self.db_manager.insert_change_request(cr, customer, color, part_description, berry_part_number,
                                               drawing_number_and_ver, mold, material, press_location,
                                               process_press_data_sheet, control_plan, cavities)

        #Clear entry fields
        self.Change_Request.delete(0, tk.END)
        self.Customer.delete(0, tk.END)
        self.Color.delete(0, tk.END)
        self.Part_Description.delete(0, tk.END)
        self.Berry_Part_Number.delete(0, tk.END)
        self.Drawing_Number_and_Ver.delete(0, tk.END)
        self.Material.delete(0, tk.END)
        self.Press_Location.delete(0, tk.END)
        self.Press_Process_Data_Sheet.delete(0, tk.END)
        self.Control_Plan.delete(0, tk.END)
        self.Cavities.delete(0, tk.END)

    def generate_report(self):
        # Report all data
        data = self.db_manager.fetch_last_change_request()
        report_text = ""
        if data:
            report_text += f"Change Request: {data[0]}\n"
            report_text += f"Customer: {data[1]}\n"
            report_text += f"Color: {data[2]}\n"
            report_text += f"Part Description: {data[3]}\n"
            report_text += f"Berry Part Number: {data[4]}\n"
            report_text += f"Drawing Number and Ver.: {data[5]}\n"
            report_text += f"Mold: {data[6]}\n"
            report_text += f"Material: {data[7]}\n"
            report_text += f"Press Location: {data[8]}\n"
            report_text += f"Process Press Data Sheet: {data[9]}\n"
            report_text += f"Control Plan: {data[10]}\n"
            report_text += f"Cavities: {data[11]}\n\n"

            # Include hard-coded paragraphs
            additional_text = """1. Qualification Procedure 
            1.1. Conduct a minimum 4 - hour capability study running within the process parameters identified on the press process data sheet per the following steps:
            1.2. Allow a warm up period of no less than ½ hour and review bottle attributes before beginning sampling.  Raise any concerns to Management.
            1.3. Obtain samples from all cavities, all stations (Full shot = 8 cavities per station x 3 stations = 24 pieces total per full shot):
            1.3.1. One full shot after warm up - all stations (A, B and C)  
            1.3.2. Four additional full shots, spaced 1 hour apart.  Each group of shots to include all stations. 
            1.3.3. Total of 120 parts.  
            1.4. Put one station per zipped bag and mark each bag with the CR#, shot number (#1-5) and station (A, B, or C). 
            1.5. Provide a copy of the completed Press Data Sheet to Joseph Neeson.or Jennifer Dillehay.
            1.6. Perform all attribute inspections in accordance with Control Plan TBD.   Document the attribute inspections in Infinity.  Attributes MUST pass review.  Any concerns need to be brought to Quality Manager for review.
            1.7. If attribute review passes, turn in the parts to Metrology using the Metrology Ticket.  Metrology will perform all variable inspections on the samples collected and record the data in Infinity.  
            2. If the Qualification is to be part of a production work order (build at risk):
            2.1 The production work order must be available before the start of the run.  
            2.2 Work with Quality to initiate an Event Based Investigation (EBI) form prior to starting the run.  Identify the discrepancy as “Qualify new manifold.”
            2.3 Keep the EBI form in the work order packet.  
            2.4 Notify a Quality Tech when the qualification portion of the run is complete.
            2.5 Both during the qualification portion of the run, and after commencing normal build, all inspections required by the Control Plan or additional instructions in the work order packet must be completed and recorded in Infinity, the same as for a normal production run.  If the attribute inspections required by the Qualification Plan also meet the requirements of the work order, they do not need to be repeated.   

            3. If all parts run are solely for qualification:
            3.1. Stop producing parts after the required qualification period is complete and the required number of samples has been collected.  
            3.2. Scrap all ware produced.  

            ****DO NOT SAVE PARTS WHEN QUALIFICATION RUNS ARE COMPLETED****""".format(data[0])
            report_text += additional_text

        # Query Infinity database
        infinity_results = self.db_manager.fetch_infinity_query_results()

        # Format and append Infinity results to report_text
        if infinity_results:
            report_text += "\nInfinity Database Results:\n"
            for row in infinity_results:
                report_text += f"{row}\n"

        if report_text:
            messagebox.showinfo("Change Request Report", report_text)
        else:
            messagebox.showinfo("Change Request Report", "No change request data found.")


class ChangeRequestApp:
    def __init__(self, master):
        self.master = master
        master.title("Main Menu")
        master.geometry("350x250")
        self.db_manager = DatabaseManager()

        #Create dictionaries for mold options
        self.mold_options = {
            "MLX Molds":  [
            "75624B 78cc Vial" , "75624C 78cc Vial" , "75624D 78cc Vial" , "75624E 78cc Vial", "75624F 78cc Vial" , "75624G 78cc Vial" ,
            "75624H 78cc Vial" , "75624J 78cc Vial" , "75624K 78cc Vial" , "75624L 78cc Vial" , "75624M 78cc Vial" , "75624N 78cc Vial" ,
            "76032A 80ml Vial" , "76032B 80ml Vial" , "76032C 80ml Vial" , "76032D 80ml Vial" , "76032E 80ml Vial" , "76032F 80ml Vial" ,
            " 76032G 80ml Vial"
        ],
        "Injection Molds": [
            "1941 Navigator Cap" , "1942 39ml Vial" , "5838" , "30980" , "31098" , "31157" , "31167" , "31311" , "A-1638-A1 Applicator Stick" ,
            "ACM-055 89mm Fitment" , "ACM-057 11mm Spoon Engraved" , "ACM-058 7mm Spoon Long Handle" , "ACM-059 7mm Spoon Short Handle" ,
            "APT-01934" , "CM-0064 ETO Ring" , "CM-8417 Tip Plug Round .062" , "CM-8418 Tip Plug Flat" ,
            "CM-8418A" , "CM-8445 Tip Plug Round .026" , "CM-8552 Plunger Rod" , "CM-8553 Barrel Long" , "CM-8566A Barrel Short" ,
            "CM-8567A Plunger" , "CM-8629 Deco Cap" , "CM-8728 Tip Cap" ,"CM-8729 Cannula" , "CM-8736A Barrel Redesign" , "CM-8737A Tip Cap Redesign" ,
            "CM-8740 4 Way Nasal Plug" , "CM-8758" , "CM-8760 2tbs Kaopectate Cup" , "CM-8776B Basket Hanger Tab" , "CM-8776C Basket Hanger Tab" ,
            "CM-8815 Hub" , "CM-8816 Actuator Cup" , "CM-8817 Base" , "CM-8886 Applicator Tube" , "CM-8886-A Applicator Tube" ,
            "CM-8902 Tip Plug .010" , "CM-8903" , "CM-8904 Smooth Base" , "CM-8905" , "CM-8907" , "CM-8926 30ml Dosage Cup" , "CM-8990 CRC 13mm Outer" ,
            "CM-8992 CRC 15mm Outer" , "CM-8993", "CVR-01935" , "JM-5287-1 Tip Plug Round .010" , "JM-5288-1 Tip Plug Round .026" ,
            "JM-5289-1 Tip Plug Round .062" , "JM-5449-1 Tip Plug .021" , "JM-5666-2 Plunger Rod" , "MJ-0924 15mm Cap" , "MJ-0941A Lens Case Base" ,
            "MJ-0941B Lens Case Base" , "MJ-0941C Lens Case Base" , "MJ-0942A Lens Case Rt Closure" , "MJ-0943A Lens Case Left Closure" ,
            "MJ-1327 CRC 13mm Inner" , "MJ-1331 CRC 15mm Inner" , "MJ-1333 CRC 18mm Inner"
        ],
        "IBM Molds": [ 
            "361 100cc Round" , "4287 125cc Round" , "4377B 250cc Round" , "4379 45cc Round" , "4380 150cc Packer" , "4455H 45cc Square" ,
            "4628 30cc Round" , "4629 120cc Round" , "4630 250cc" , "4643B 115cc Round" , "4711 18cc Round" , "4730 4oz Cylinder" , "4736 45cc Square" ,
            "4736A 45cc Square" , "4738 45cc Round" , "4739C 115cc Rnd" , "4780 120cc Square" , "5012 45cc Square" , "5019 90cc Square" ,
            "5035 150cc Square" , "5052A 1oz Cylinder" , "5085A 30ml Round" , "5087A 20ml Round" , "5088B 10ml Round" , "5088C 10ml Round" ,
            "5122 60cc Round" , "5125 250cc Round" , "5153B 3cc Round" , "5153C 3cc Round" , "5153CC 3cc Round" , "5198A 14mm Vial" ,
            "5219B 150cc Round" , "5237 60ml Oblong" , "5240 30ml Oblong" , "5264 60cc Round" , "5265A 120ml Round" , "5265C 120ml Round" ,
            "5266A HDPE 180ml Round" , "5266A Lugs 180ml Round" , "5266A PP 180ml Round" , "5297 45cc Wht Rnd" ,
            "5297A 45cc Wht Rnd" , "5308 1.6oz Trapezoidal" , "5308B 1.6oz Trapezoidal" , "5309 2.7oz Trapezoidal" , "5309B 2.7oz Trapezoidal" ,
            "5324 40cc Round" , "5325 75cc Round" , "5359B 15cc Round" ,
            "5360 30cc Round" , "5360A 30cc Round" , "5361A 60cc Round" , "5362B 120cc Round" , "5362C  120cc Round" , "5365 2oz Round" ,
            "5379 2oz Round" , "5412 60ml Round" , "5422B 75ml Round" , "5422C 75ml Round" , "5422D 75ml Round" , "5422E 75ml Round" ,
            "5429A 1.25oz Round" , "5430 525ml Oblong" , "5436B 325ml Square" , "5436B BMS 325ml Square" , "5437B 60ml Square" , "5437C 60ml Square" ,
            "5439 60ml round" , "5462A 4oz Round" , "5462B 4oz Round" , 
            "5464 2oz Round" , "5491B 120cc Round" , "5492A 150cc Round" , "5493 200cc Round" , "5497 300cc Round" , "5532 2oz Cylinder" ,
            "5548 6ml Vial" , "5549 30ml Vial" , "5566A 250cc Round" , "5593 95ml white square" , "5597 10ml Round" , "5603 315cc Round" ,
            "5605 10ml nat" ,
            "5611 60cc Round" , "5617B  105cc" , "5625A 20ml Round" , "5625B 20ml Round" , "5648B 45cc Square" , "5648E 45cc Square" , "5655A HDPE 100cc Round" ,
            "5655A PP 100cc Round" , "5655B HDPE 100cc Round" , "5655B PP 100cc Round" , "5660A 60cc Square" , "5660B 60cc Square" , "5660C 60cc Square" ,
            "5660D 60cc Square" , "5660E 60cc Square" , "5711 100cc Round" , "5720A 120cc Square" , "5720B 120cc Square" , "5720C 120cc Square" ,
            "5721B 180cc Square" , "5721C 180cc Square" , "5750A 120cc Round" , "5848B 40cc Round" , "5883B 60cc Square" , "5943 10ml Round" ,
            "5945 100ml Round" , "5998A 3ml Vial" , "5998B 3ml Vial" , "5998C 3ml Vial" , "5998D 3ml Vial" , "5998E 3ml Vial" , "6006 215cc Wide Mouth Oblong" ,
            "6007A 90cc Square" , "6007B 90cc Square" , "6010 150cc Square" , "6022 30ml Round" , "6033 2oz Round" , "6036 105cc HDPE Square" ,
            "6039 2oz Round" , "6040 2oz Round" , "6043 5ml Round" , "6044 10ml Round" ,
            "6045 20ml Round" , "6046 30ml Round" , "6047 50ml Round" , "7031B 1oz Visine" , "7146 4oz Round" , "J120-1 165cc Round" , "J148 110cc Round" ,
            "J148-2 110cc Round" , "J148-4 110cc Round"
           
        ]
        }

        self.btnOpenProgram = tk.Button(master, text = "Open Program", command=self.open_program)
        self.btnOpenProgram.pack(pady=10)

        self.btnQuit = tk.Button(master, text = "Quit", fg = "red", command = master.destroy)
        self.btnQuit.pack()

    def open_program(self):
        ChangeRequestEntryForm(self.master, self.db_manager, self.mold_options)

def main():
    root = tk.Tk()
    app = ChangeRequestApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
