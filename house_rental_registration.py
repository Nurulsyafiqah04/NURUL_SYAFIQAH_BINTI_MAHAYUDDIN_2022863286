import tkinter as tk
from tkinter import ttk
import mysql.connector

# CONNECT TO MYSQL DATABASE
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="house_rental"
)

# CREATE A CURSOR OBJECT TO EXECUTE SQL QUERIES
mycursor = mydb.cursor()

def collect_data():
    Ic_Number = Ic_number_entry.get()
    Customer_Name = Customer_name_entry.get()
    Contact_Number = Contact_number_entry.get()
    Type_Of_House = Type_of_house_combobox.get()
    Year_Rent = int(Year_rent_entry.get())
    Cleaning_Service = (Cleaning_service_combobox.get())

    # DEFINE VALUES FROM SELECTIONS
    Price_Per_House ={
        "HOUSE A" : 600,
        "HOUSE B" : 400,
    }

    # CALCULATE TOTAL RENT
    Cleaning_Service_Charge = {
        "YES": 100,
        "NO": 0,
    }

    if Cleaning_Service == "YES":
        Total_Rent = Cleaning_Service_Charge[Cleaning_Service] + Price_Per_House[Type_Of_House] * int(Year_Rent)
        print(Total_Rent)

    else :
        Total_Rent = Price_Per_House[Type_Of_House] * int(Year_Rent)
        print(Total_Rent)

    # TO INSERT DATA TO DATABASE
    sql = "INSERT INTO house_rental_registration (Ic_Number, Customer_Name, Contact_Number, Type_Of_House, Year_Rent,Cleaning_Service, Total_Rent) VALUES (%s, %s, %s,%s,%s,%s,%s)"
    val = (Ic_Number, Customer_Name, Contact_Number, Type_Of_House, Year_Rent, Cleaning_Service, Total_Rent)
    mycursor.execute(sql, val)
    mydb.commit()

    # FUNCTION COLLECT DATA
    output_label.configure(text=f"Ic Number: {Ic_Number},Contact Number: {Contact_Number},Type Of House: {Type_Of_House},Year Rent:{Year_Rent},Cleaning Service Payment: {Cleaning_Service},Total Rent:RM{Total_Rent}")

# INTERFACE
root = tk.Tk()
root.title("house_rental") 
root.geometry('800x800')
root.configure(bg="GoldenRod4")

frame = tk.Frame(root)
frame.pack()

# PAGE TITLE
label = tk.Label(root, text="HOUSE RENTAL REGISTRATION", font=("Franklin Gothic Medium", 16, "bold"),bg="LightGoldenrod3",fg="floralwhite",bd=5,relief="ridge")
label.pack(ipadx=12, ipady=10)

#  HOUSE SPECIFICATION LIST BY USING TEXTBOX
house_specification = tk.Text(root, height=10, width=60, bg="Khaki2", bd=7)
house_specification.pack(pady=15)

# DEFINE LIST BY USING HOUSE SPECIFICATION BOX
house_specification.insert(tk.END, "House Specification and Price\n\n")
house_specification.insert(tk.END, "House A: Corner lot house, three bedroom \nAdd cleaning service: Rm100 \nPrice: RM 600\n\n")
house_specification.insert(tk.END, "House B: Middle house, two bedroom \nAdd Cleaning service: RM100 \nPrice: RM 400\n\n")
house_specification.configure(state='disable')

frame = tk.Frame(root)
frame.pack()

# SAVING CUSTOMER REGISTRATION USING
Customer_Registration_frame=tk.LabelFrame(frame, text="Customer Registration",font=("aldhabi",10,"bold"),bg="Goldenrod",fg="FloralWhite")
Customer_Registration_frame.grid(row=7, column=0)

Ic_number_label=tk.Label(Customer_Registration_frame, text="Ic Number",bg="Khaki1",bd=3,relief="sunken")
Ic_number_label.grid(row=7,column=0)

Ic_number_entry=tk.Entry(Customer_Registration_frame,bd=3,relief="ridge")
Ic_number_entry.grid(row=8, column=0)

Customer_name_label=tk.Label(Customer_Registration_frame, text="Customer Name",bg="Khaki1",bd=3,relief="sunken")
Customer_name_label.grid(row=7, column=3)

Customer_name_entry=tk.Entry(Customer_Registration_frame,bd=3,relief="ridge")
Customer_name_entry.grid(row=8, column=3)

Contact_number_label=tk.Label(Customer_Registration_frame, text="Contact Number",bg="Khaki1",bd=3,relief="sunken")
Contact_number_label.grid(row=7, column=6)

Contact_number_entry=tk.Entry(Customer_Registration_frame,bd=3,relief="ridge")
Contact_number_entry.grid(row=8, column=6)

Type_of_house_label=tk.Label(Customer_Registration_frame, text="Type Of House",bg="Khaki1",bd=3,relief="sunken")
Type_of_house_combobox=ttk.Combobox(Customer_Registration_frame, values=["HOUSE A", "HOUSE B"])
Type_of_house_label.grid(row=12, column=0)
Type_of_house_combobox.grid(row=13, column=0)

Year_rent_label=tk.Label(Customer_Registration_frame, text="Year Rent",bg="Khaki1",bd=3,relief="sunken")
Year_rent_label.grid(row=12, column=3)

Year_rent_entry=tk.Entry(Customer_Registration_frame,bd=3,relief="ridge")
Year_rent_entry.grid(row=13, column=3)

Cleaning_service_label=tk.Label(Customer_Registration_frame, text="Cleaning Service",bg="Khaki1",bd=3,relief="sunken")
Cleaning_service_combobox=ttk.Combobox(Customer_Registration_frame, values=["YES","NO"])
Cleaning_service_label.grid(row=12, column=6)
Cleaning_service_combobox.grid(row=13, column=6)


for widget in Customer_Registration_frame.winfo_children():
    widget.grid_configure(padx=15, pady=10)

# CALCULATE AND SAVE BUTTON
calculate_button = tk.Button(root, text="CALCULATE", command=collect_data,bg="DarkGoldenrod",bd=5,relief="raised")
calculate_button.pack(pady=15)

label = tk.Label(root, text='TOTAL RENT :', font=("Segoe Print",15,"underline","bold"))
label.pack(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()