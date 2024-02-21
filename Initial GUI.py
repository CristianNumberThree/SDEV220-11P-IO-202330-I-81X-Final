from tkinter import *

#inital window
root = Tk()
root.title("Main Menu")
root.geometry("250x150")

#main program window
def OpenProgram():
        
    Program=Toplevel()
    Program.title("Main Program")

    #Create frame
    frame = Frame(Program)
    exitframe = Frame(Program)

    #Entries

    #Change Requests
    Label(frame, text='Change Request (CR):').grid(row=0)
    ChangeRQEntry = Entry(frame)
    ChangeRQEntry.grid(row=0, column=1)

    #Customer
    Label(frame, text='Customer:').grid(row=1)
    CustomerEntry = Entry(frame)
    CustomerEntry.grid(row=1, column=1)

    #Color
    Label(frame, text='Color:').grid(row=2)
    ColorEntry = Entry(frame)
    ColorEntry.grid(row=2, column=1)

    #Part description
    Label(frame, text='Part description:').grid(row=3)
    PartDescEntry = Entry(frame)
    PartDescEntry.grid(row=3, column=1)

    #Berry part number
    Label(frame, text='Berry (JDE) part number:').grid(row=4)
    PartNumEntry = Entry(frame)
    PartNumEntry.grid(row=4, column=1)

    #Drawing number and ver
    Label(frame, text='Drawing number & ver.:').grid(row=5)
    DrawingNumEntry = Entry(frame)
    DrawingNumEntry.grid(row=5, column=1)

    #Mold
    Label(frame, text='Mold:').grid(row=6)
    MoldEntry = Entry(frame)
    MoldEntry.grid(row=6, column=1)

    #Material
    Label(frame, text='Material:').grid(row=7)
    MaterialEntry = Entry(frame)
    MaterialEntry.grid(row=7, column=1)

    #Press location
    Label(frame, text='Press location:').grid(row=8)
    PressLocEntry = Entry(frame)
    PressLocEntry.grid(row=8, column=1)

    #Press process data sheet
    Label(frame, text='Press process data sheet:').grid(row=9)
    PPDSEntry = Entry(frame)
    PPDSEntry.grid(row=9, column=1)

    #Control plan
    Label(frame, text='Control plan:').grid(row=10)
    CtrlPlanEntry = Entry(frame)
    CtrlPlanEntry.grid(row=10, column=1)

    #Cavities
    Label(frame, text='Cavities:').grid(row=11)
    CavitiesEntry = Entry(frame)
    CavitiesEntry.grid(row=11, column=1)

    #Exit
    btnExit = Button(exitframe, text ='Exit', fg ='red', command=Program.destroy)
    btnExit.pack()


    frame.pack()
    exitframe.pack()

#open program
btnOpenProgram=Button(root, text="Open Program", command=OpenProgram).pack(pady=10)
btnQuit = Button(root, text ='Quit', fg ='red', command=root.destroy)
btnQuit.pack()

root.mainloop()