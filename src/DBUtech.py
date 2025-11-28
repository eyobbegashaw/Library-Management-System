import tkinter as tk 
from tkinter import ttk,messagebox,StringVar
from tkinter import * 
from database1 import *
import re  
db=LibraryDB("library.db")
root=tk.Tk()
root.geometry('1400x1900')
root.title("dbu tech labrary")
 
tabControl =ttk.Notebook(root,padding=20)  
member_tab = Frame(tabControl)
book_tab = Frame(tabControl)  
staff_tab =Frame(tabControl)  
notification_tab =Frame(tabControl) 
borrowing_tab = Frame(tabControl) 
publisher_tab = Frame(tabControl)
catalog_tab = Frame(tabControl)
        
tabControl.add(member_tab, text='member')
tabControl.add(book_tab, text='book')
tabControl.add(staff_tab, text='staff')
tabControl.add(notification_tab, text='notification')
tabControl.add(borrowing_tab, text='borrow')
tabControl.add(publisher_tab, text='publisher')
tabControl.add(catalog_tab, text='catalog')

tabControl.pack(expand=1, fill="both")  
#  member_tab
 
ssn = StringVar()
firstname = tk.StringVar()
lastname = tk.StringVar()
campus = tk.StringVar()
home = tk.StringVar()
phone = tk.StringVar()
mem = tk.StringVar()
card = tk.StringVar()
Cex = tk.StringVar()
status = tk.StringVar()
email = tk.StringVar()
photo = tk.StringVar()
borrow = tk.StringVar()
penality = tk.StringVar()

# Create labels and entry fields for member details
 

Label(member_tab, text="SS Number:").grid(row=1, column=0, sticky="w")
ssn_entry = Entry(member_tab, textvariable=ssn)
ssn_entry.grid(row=1, column=1, sticky="ew")

Label(member_tab, text="First Name:").grid(row=2, column=0, sticky="w")
first_name_entry = Entry(member_tab, textvariable=firstname)
first_name_entry.grid(row=2, column=1, sticky="ew")

Label(member_tab, text="Last Name:").grid(row=3, column=0, sticky="w")
last_name_entry = Entry(member_tab, textvariable=lastname)
last_name_entry.grid(row=3, column=1, sticky="ew")

Label(member_tab, text="Campus Address:").grid(row=4, column=0, sticky="w")
campus_entry = Entry(member_tab, textvariable=campus)
campus_entry.grid(row=4, column=1, sticky="ew")

Label(member_tab, text="Home Address:").grid(row=5, column=0, sticky="w")
home_entry = Entry(member_tab, textvariable=home)
home_entry.grid(row=5, column=1, sticky="ew")

Label(member_tab, text="Phone Number(+251):").grid(row=6, column=0, sticky="w")
phone_entry = Entry(member_tab, textvariable=phone)
phone_entry.grid(row=6, column=1, sticky="ew")

Label(member_tab, text="Membership Type:").grid(row=7, column=0, sticky="w")
mem_entry = ttk.Combobox(member_tab, width=50, values=('Regular', 'Lecturer'), textvariable=mem)
mem_entry.grid(row=7, column=1, sticky="ew")

Label(member_tab, text="Card Issued Date:").grid(row=8, column=0, sticky="w")
card_entry = tk.Entry(member_tab, textvariable=card)
card_entry.grid(row=8, column=1, sticky="ew")

Label(member_tab, text="Card Expiry Date:").grid(row=9, column=0, sticky="w")
Cex_entry = tk.Entry(member_tab, textvariable=Cex)
Cex_entry.grid(row=9, column=1, sticky="ew")

Label(member_tab, text="Status:").grid(row=10, column=0, sticky="w")
status_entry = ttk.Combobox(member_tab, width=50, values=('Active', 'Inactive'), textvariable=status)
status_entry.grid(row=10, column=1, sticky="ew")

Label(member_tab, text="Email:").grid(row=11, column=0, sticky="w")
email_entry = tk.Entry(member_tab, textvariable=email)
email_entry.grid(row=11, column=1, sticky="ew")

Label(member_tab, text="Photo:").grid(row=12, column=0, sticky="w")
photo_entry = tk.Entry(member_tab, textvariable=photo)
photo_entry.grid(row=12, column=1, sticky="ew")

Label(member_tab, text="BorrowingHistory(in num):").grid(row=13, column=0, sticky="w")
borrow_entry = tk.Entry(member_tab, textvariable=borrow)
borrow_entry.grid(row=13, column=1, sticky="ew")

Label(member_tab, text="Penalty Balance(inNum):").grid(row=14, column=0, sticky="w")
penality_entry = tk.Entry(member_tab, textvariable=penality)
penality_entry.grid(row=14, column=1, sticky="ew")


def fetchData():
     
    member_tree.delete(*member_tree.get_children())
    members = db.fetch_all_members()
    for row in members:
        member_tree.insert("",END, values=row)

def getrecord(event):
   
    selected_row = member_tree.focus()
    data = member_tree.item(selected_row)
    global row
    row = data['values']

     
    ssn.set(row[1])
    firstname.set(row[2])
    lastname.set(row[3])
    campus.set(row[4])
    home.set(row[5])
    phone.set(row[6])
    mem.set(row[7])
    card.set(row[8])
    Cex.set(row[9])
    status.set(row[10])
    email.set(row[11])
    photo.set(row[12])
    borrow.set(row[13])
    penality.set(row[14])
def validt():
    date= r"^\d{4}-\d{2}-\d{2}$"
    if not ssn_entry.get().strip() or len(ssn_entry.get().strip())!=9:
        messagebox.showinfo("error","Enter valid ssn")
        return False
    if not first_name_entry.get().strip():
        messagebox.showinfo("error","Enter correct name pls")
        return False
    if not last_name_entry.get().strip():
        messagebox.showinfo("error","Enter correct name pls")
        return False
    if not campus_entry.get().strip():
        messagebox.showinfo("error","Enter correct word pls")
        return False
    if not home_entry.get().strip():
        messagebox.showinfo("error","Enter correct home address  pls")
        return False
    if not phone_entry.get().strip().isdigit()or len(phone_entry.get().strip())!=10:
        messagebox.showinfo("error","enter correct valid phone number pls")
        return False
    if not mem_entry.get().strip() in ['Regular', 'Lecturer']:
        messagebox.showinfo("error","you must select from Regular or Lecturer")
        return False
    if not re.match(date,card_entry.get()):
        messagebox.showinfo("error","Enter  valid card issued date(yyyy/mm/dd)")
        return False
    if  not re.match(date,Cex_entry.get()):
        messagebox.showinfo("error","Enter  valid card expariry date(yyyy/mm/dd)")
        return False
    if not status_entry .get().strip() in ['Active', 'Inactive']:
        messagebox.showinfo("error","you must select from 'Active' or 'Inactive'")
        return False
    if not email_entry .get().strip() or "@" not in email_entry.get().strip():
        messagebox.showinfo("error","Enter correct email address pls")
        return False
    if not photo_entry .get().strip() or ".png"not in photo_entry.get().strip():
        messagebox.showinfo("error","your photo entry is must be .png ")
        return False
    if not borrow_entry .get().strip().isdigit():
        messagebox.showinfo("error","Enter correct borrow history pls")
        return False
    if not penality_entry .get().strip().isdecimal():
        messagebox.showinfo("error","Enter correct penality balance pls")
        return False
    return True
def addMember():
    if not validt():
        return
    db.add_member(
            ssn_entry.get(), first_name_entry.get(), last_name_entry.get(),
            campus_entry.get(), home_entry.get(), phone_entry.get(), mem_entry.get(), card_entry.get(),
            Cex_entry.get(), status_entry.get(), email_entry.get(), photo_entry.get(),
            borrow_entry.get(), penality_entry.get()
        )
    fetchData()
    clearData()
    messagebox.showinfo("Message", "Record inserted successfully!")

def updateData():
    if not validt():
         return 
    db.update_member(
           row[0], ssn_entry.get(), first_name_entry.get(), last_name_entry.get(),
            campus_entry.get(), home_entry.get(), phone_entry.get(), mem_entry.get(), card_entry.get(),
            Cex_entry.get(), status_entry.get(), email_entry.get(), photo_entry.get(),
            borrow_entry.get(), penality_entry.get()
        )
    fetchData()
    clearData()
    messagebox.showinfo("Message", "Record updated successfully!")

def clearData():
     
    ssn.set("")
    firstname.set("")
    lastname.set("")
    campus.set("")
    home.set("")
    phone.set("")
    mem.set("")
    card.set("")
    Cex.set("")
    status.set("")
    email.set("")
    photo.set("")
    borrow.set("")
    penality.set("")

def deleteData():
    if not row:
        messagebox.showinfo("Message", "Please select a record to delete!")
        return
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this record?")
    if confirm:
        db.remove_member(row[0])
        fetchData()
        clearData()
        messagebox.showinfo("Message", "Record deleted successfully!")

 
add_member_button =Button(member_tab, text="Add", bg="green", width=4, padx=20, pady=5, command=addMember)
add_member_button.grid(row=15, column=15)

delete_member_button = Button(member_tab, text="Delete", bg="red", width=4, padx=20, pady=5, command=deleteData)
delete_member_button.grid(row=15, column=12)

update_member_button = tk.Button(member_tab, text="Update", bg='#01a3a4', width=4, padx=20, pady=5, command=updateData)
update_member_button.grid(row=15, column=10)


member_tree = ttk.Treeview(member_tab, column=("MemberId","SSNumber", "FirstName", "LastName", "CampusAddress", "HomeAddress", "PhoneNumber",
    "Member Type", "IssuedDate", "ExpiryDate", "Status", "Email", "Photo", "Borrow Activity", "Pena Balance"
), show="headings")
for i in member_tree["column"]:
  member_tree.heading(i, text=i)
  member_tree.column(i, width=88)
member_tree.grid(row=25, column=0, columnspan=30, sticky="nsew")

 
member_tree.bind("<ButtonRelease-1>", getrecord)
 
isbn = StringVar()
title = StringVar()
author = StringVar()
subject_area = StringVar()
binding_type = StringVar()
is_lendable = StringVar()
copies_available = StringVar()
copies_on_loan = StringVar()

Label(book_tab, text="ISBN(15digit):").grid(row=1, column=0, sticky="w")
isbn_entry = Entry(book_tab, textvariable=isbn)
isbn_entry.grid(row=1, column=1, sticky="ew")

Label(book_tab, text="Title:").grid(row=2, column=0, sticky="w")
title_entry = Entry(book_tab, textvariable=title)
title_entry.grid(row=2, column=1, sticky="ew")

Label(book_tab, text="Author:").grid(row=3, column=0, sticky="w")
author_entry = Entry(book_tab, textvariable=author)
author_entry.grid(row=3, column=1, sticky="ew")

Label(book_tab, text="Subject Area:").grid(row=4, column=0, sticky="w")
subject_area_entry = Entry(book_tab, textvariable=subject_area)
subject_area_entry.grid(row=4, column=1, sticky="ew")

Label(book_tab, text="Binding Type:").grid(row=5, column=0, sticky="w")
binding_type_entry = Entry(book_tab, textvariable=binding_type)
binding_type_entry.grid(row=5, column=1, sticky="ew")

Label(book_tab, text="is_lendable:").grid(row=6, column=0, sticky="w")
is_lendable_entry = ttk.Combobox(book_tab, width=50, values=('Yes', 'No'), textvariable=is_lendable)
is_lendable_entry.grid(row=6, column=1, sticky="ew")

Label(book_tab, text="Copies Available:").grid(row=7, column=0, sticky="w")
copies_available_entry = Entry(book_tab, textvariable=copies_available)
copies_available_entry.grid(row=7, column=1, sticky="ew")

Label(book_tab, text="Copies On Loan:").grid(row=8, column=0, sticky="w")
copies_on_loan_entry = Entry(book_tab, textvariable=copies_on_loan)
copies_on_loan_entry.grid(row=8, column=1, sticky="ew")

book_tree = ttk.Treeview(book_tab, columns=(
    "BookID", "ISBN", "Title", "Author", "SubjectArea", "BindingType", "IsLendable", "CopiesAvailable", "CopiesOnLoan"
), show="headings")
for col in book_tree["columns"]:
    book_tree.heading(col, text=col)
    book_tree.column(col, width=100)
book_tree.grid(row=10, column=0, columnspan=30, sticky="nsew")

 
def fetchBookData():
    book_tree.delete(*book_tree.get_children())
    books = db.fetch_all_books()
    for row in books:
        book_tree.insert("", END, values=row)
def validput():
    if not isbn_entry.get().strip() or len(isbn_entry.get().strip())!=15:
        messagebox.showinfo("error","Enter valid    ISBN")
        return False
    if not title_entry.get().strip():
        messagebox.showinfo("error","Enter correct title pls")
        return False
    if not author_entry.get().strip():
        messagebox.showinfo("error","Enter correct author name")
        return False
    if not subject_area_entry.get().strip():
        messagebox.showinfo("error","Enter correct subject area of the book")
        return False
    if not binding_type_entry.get().strip():
        messagebox.showinfo("error","Enter correct home bindig type pls")
        return False
    if not is_lendable_entry.get().strip() in ['Yes','No']:
        messagebox.showinfo("error","you must select from yes or no")
        return False
    if not copies_available_entry.get().strip():
        messagebox.showinfo("error","you must enter valid number")
        return False
    return True 
def getBookRecord(event):
    selected_row = book_tree.focus()
    data = book_tree.item(selected_row)
    global book_row
    book_row = data['values']

    
    isbn.set(book_row[1])
    title.set(book_row[2])
    author.set(book_row[3])
    subject_area.set(book_row[4])
    binding_type.set(book_row[5])
    is_lendable.set(book_row[6])
    copies_available.set(book_row[7])
    copies_on_loan.set(book_row[8])

def addBook():
    if not validput():
         return
    db.add_book(
            isbn_entry.get(), title_entry.get(), author_entry.get(), subject_area_entry.get(),
            binding_type_entry.get(), is_lendable_entry.get(), copies_available_entry.get(), copies_on_loan_entry.get()
        )
    fetchBookData()
    clearBookData()
    messagebox.showinfo("Message", "Book added successfully!")

def updateBookData():
    if not validput():
        return
    db.update_book(
            book_row[0], isbn_entry.get(), title_entry.get(), author_entry.get(), subject_area_entry.get(),
            binding_type_entry.get(), is_lendable_entry.get(), copies_available_entry.get(), copies_on_loan_entry.get()
        )
    fetchBookData()
    clearBookData()
    messagebox.showinfo("Message", "Book updated successfully!")

def clearBookData():
    isbn.set("")
    title.set("")
    author.set("")
    subject_area.set("")
    binding_type.set("")
    is_lendable.set("")
    copies_available.set("")
    copies_on_loan.set("")

def deleteBookData():
    if not book_row:
        messagebox.showinfo("Message", "Please select a record to delete!")
        return
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this book?")
    if confirm:
        db.remove_book(book_row[0])
        fetchBookData()
        clearBookData()
        messagebox.showinfo("Message", "Book deleted successfully!")
 
add_book_button = Button(book_tab, text="Add", bg="green", width=10, padx=20, pady=5, command=addBook)
add_book_button.grid(row=9, column=10, columnspan=2)

delete_book_button = Button(book_tab, text="Delete", bg="red", width=10, padx=20, pady=5, command=deleteBookData)
delete_book_button.grid(row=9, column=6, columnspan=2)

update_book_button = Button(book_tab, text="Update", bg='#01a3a4', width=10, padx=20, pady=5, command=updateBookData)
update_book_button.grid(row=9, column=8, columnspan=2)

 
 
book_tree.bind("<ButtonRelease-1>", getBookRecord)

 
 
catalog_isbn = StringVar()
catalog_description = StringVar()
 
Label(catalog_tab, text="ISBN:").grid(row=1, column=0, sticky="w")
catalog_isbn_entry = Entry(catalog_tab, textvariable=catalog_isbn)
catalog_isbn_entry.grid(row=1, column=1, sticky="ew")

Label(catalog_tab, text="Description:").grid(row=2, column=0, sticky="w")
catalog_description_entry = Entry(catalog_tab, textvariable=catalog_description)
catalog_description_entry.grid(row=2, column=1, sticky="ew")

 
catalog_tree = ttk.Treeview(catalog_tab, columns=(
    "CatalogID", "ISBN", "Description"
), show="headings")
for col in catalog_tree["columns"]:
    catalog_tree.heading(col, text=col)
    catalog_tree.column(col, width=180)
catalog_tree.grid(row=6, column=0, columnspan=30, sticky="nsew")

 
def fetchCatalogData():
    catalog_tree.delete(*catalog_tree.get_children())
    catalogs = db.fetch_all_catalog()
    for row in catalogs:
        catalog_tree.insert("", END, values=row)
def input():
    if  not catalog_isbn_entry.get().strip() or len(catalog_isbn_entry.get())!=15:
        messagebox.showinfo("error","enter valid ISBN")
        return False
    if not catalog_description_entry.get().strip():
        messagebox.showinfo("error","you must correct description of catalog entry")
        return False
    return True
def getCatalogRecord(event):
    selected_row = catalog_tree.focus()
    data = catalog_tree.item(selected_row)
    global catalog_row
    catalog_row = data['values']

    
    catalog_isbn.set(catalog_row[1])
    catalog_description.set(catalog_row[2])
def addCatalog():
    if not input():
        return
    db.add_catalog(
        catalog_isbn_entry.get(), catalog_description_entry.get()
        )
    fetchCatalogData()
    clearCatalogData()
    messagebox.showinfo("Message", "Catalog added successfully!")

def updateCatalogData():
    if not input():
        return
    db.update_catalog(
        catalog_row[0], catalog_isbn_entry.get(), catalog_description_entry.get()
        )
    fetchCatalogData()
    clearCatalogData()
    messagebox.showinfo("Message", "Catalog updated successfully!")

def clearCatalogData():
     
    catalog_isbn.set("")
    catalog_description.set("")
def deleteCatalogData():
    if not catalog_row:
        messagebox.showinfo("Message", "Please select a record to delete!")
        return
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this catalog?")
    if confirm:
        db.remove_catalog(catalog_row[0])
        fetchCatalogData()
        clearCatalogData()
        messagebox.showinfo("Message", "Catalog deleted successfully!")

add_catalog_button = Button(catalog_tab, text="Add", bg="green", width=10, padx=20, pady=5, command=addCatalog)
add_catalog_button.grid(row=3, column=3, columnspan=2)

delete_catalog_button = Button(catalog_tab, text="Delete", bg="red", width=10, padx=20, pady=5, command=deleteCatalogData)
delete_catalog_button.grid(row=3, column=5 ,columnspan=2)

update_catalog_button = Button(catalog_tab, text="Update", bg='#01a3a4', width=10, padx=20, pady=5, command=updateCatalogData)
update_catalog_button.grid(row=3, column=7, columnspan=2)

 
catalog_tree.bind("<ButtonRelease-1>", getCatalogRecord)

 
 
borrow_member_id = StringVar()
borrow_book_id = StringVar()
borrow_date = StringVar()
due_date = StringVar()
return_date = StringVar()
borrow_status = StringVar()
 
 
Label(borrowing_tab, text="Member ID:").grid(row=1, column=0, sticky="w")
borrow_member_id_entry = Entry(borrowing_tab, textvariable=borrow_member_id)
borrow_member_id_entry.grid(row=1, column=1, sticky="ew")

Label(borrowing_tab, text="Book ID:").grid(row=2, column=0, sticky="w")
borrow_book_id_entry = Entry(borrowing_tab, textvariable=borrow_book_id)
borrow_book_id_entry.grid(row=2, column=1, sticky="ew")

Label(borrowing_tab, text="Borrow Date(yyyy-mm-dd):").grid(row=3, column=0, sticky="w")
borrow_date_entry = Entry(borrowing_tab, textvariable=borrow_date)
borrow_date_entry.grid(row=3, column=1, sticky="ew")

Label(borrowing_tab, text="Due Date(yyyy-mm-dd):").grid(row=4, column=0, sticky="w")
due_date_entry = Entry(borrowing_tab, textvariable=due_date)
due_date_entry.grid(row=4, column=1, sticky="ew")

Label(borrowing_tab, text="Return Date(yyyy-mm-dd):").grid(row=5, column=0, sticky="w")
return_date_entry = Entry(borrowing_tab, textvariable=return_date)
return_date_entry.grid(row=5, column=1, sticky="ew")

Label(borrowing_tab, text="Status:").grid(row=6, column=0, sticky="w")
borrow_status_entry = ttk.Combobox(borrowing_tab, width=50, values=('Borrowed', 'Returned'), textvariable=borrow_status)
borrow_status_entry.grid(row=6, column=1, sticky="ew")
 
 
borrow_tree = ttk.Treeview(borrowing_tab, columns=(
    "TransactionID", "MemberID", "BookID", "BorrowDate", "DueDate", "ReturnDate", "Status"
), show="headings")
for col in borrow_tree["columns"]:
    borrow_tree.heading(col, text=col)
    borrow_tree.column(col, width=100)
     
borrow_tree.grid(row=8, column=0, columnspan=30, sticky="nsew")



def Addborrow(member_id, book_id, borrow_date, due_date):
    db.cursor.execute("SELECT CopiesAvailable FROM Book WHERE BookID = ?", (book_id,))
    result = db.cursor.fetchone()
    if not result or result[0] <= 0:
        messagebox.showinfo("Message", "This book is not available for borrowing.")
        return False
    db.cursor.execute('''
        UPDATE Book
        SET CopiesAvailable = CopiesAvailable - 1,
            CopiesOnLoan = CopiesOnLoan + 1
        WHERE BookID = ?
    ''', (book_id,))
    db.cursor.execute('''
        INSERT INTO BorrowingActivity (MemberID, BookID, BorrowDate, DueDate, Status)
        VALUES (?, ?, ?, ?, 'Borrowed')
    ''', (member_id, book_id, borrow_date, due_date))

    db.connection.commit()
    return True
 
def fetchBorrowData():
    borrow_tree.delete(*borrow_tree.get_children())
    borrowings = db.fetch_all_borrowing_activity()
    for row in borrowings:
        borrow_tree.insert("", END, values=row)

def getBorrowRecord(event):
    selected_row = borrow_tree.focus()
    data = borrow_tree.item(selected_row)
    global borrow_row
    borrow_row = data['values']

    borrow_member_id.set(borrow_row[1])
    borrow_book_id.set(borrow_row[2])
    borrow_date.set(borrow_row[3])
    due_date.set(borrow_row[4])
    return_date.set(borrow_row[5])
    borrow_status.set(borrow_row[6])

def valid_input():
    date= r"^\d{4}-\d{2}-\d{2}$"
    if not borrow_member_id_entry.get().isdigit():
         messagebox.showinfo("error","you must enter valid member id")
         return False
    if not borrow_book_id_entry.get().isdigit():
         messagebox.showinfo("error","you must enter valid book id")
         return False
    if not re.match(date,borrow_date_entry.get()):
        messagebox.showinfo("error","you keep the this(yyyy/mm/dd)")
        return False
    if not re.match(date,return_date_entry.get()):
        messagebox.showinfo("error","you keep the this(yyyy/mm/dd)")
        return False
    if  not re.match(date,due_date_entry.get()):
        messagebox.showinfo("error","you keep the this(yyyy/mm/dd)")
        return False
    return True
def updateBorrowData():
    if not valid_input():
        return
    db.update_borrowing_activity(
            borrow_row[0], borrow_member_id_entry.get(), borrow_book_id_entry.get(), borrow_date_entry.get(),
            due_date_entry.get(), return_date_entry.get(), borrow_status_entry.get()
        )
    fetchBorrowData()
    clearBorrowData()
    messagebox.showinfo("Message", "Borrowing record updated successfully!")

def clearBorrowData():
     
    borrow_member_id.set("")
    borrow_book_id.set("")
    borrow_date.set("")
    due_date.set("")
    return_date.set("")
    borrow_status.set("")

def deleteBorrowData():
    if not borrow_row:
        messagebox.showinfo("Message", "Please select a record to delete!")
        return
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this borrowing record?")
    if confirm:
        db.remove_borrowing_activity(borrow_row[0])
        fetchBorrowData()
        clearBorrowData()
        messagebox.showinfo("Message", "Borrowing record deleted successfully!")
def borrow_book_gui():
    member_id = borrow_member_id_entry.get().strip()
    book_id = borrow_book_id_entry.get().strip()
    borrow_date = borrow_date_entry.get().strip()
    due_date = due_date_entry.get().strip()

    if not member_id or not book_id or not borrow_date or not due_date:
        messagebox.showinfo("Message", "Please fill all the fields!")
        return

    if Addborrow(member_id, book_id, borrow_date, due_date):
        messagebox.showinfo("Message", "Book borrowed successfully!")
        fetchBookData()   
        fetchBorrowData()   
    else:
        messagebox.showinfo("Message", "Failed to borrow the book.")

 

delete_borrow_button = Button(borrowing_tab, text="Delete", bg="red", width=10, padx=20, pady=5, command=deleteBorrowData)
delete_borrow_button.grid(row=7, column=3, columnspan=2)

update_borrow_button = Button(borrowing_tab, text="Update", bg='#01a3a4', width=10, padx=20, pady=5, command=updateBorrowData)
update_borrow_button.grid(row=7, column=5, columnspan=2)

borrow_button = Button(borrowing_tab, text="Borrow Book", bg="green", width=15, padx=20, pady=5, command=borrow_book_gui)
borrow_button.grid(row=7 ,column=7, columnspan=2)

borrow_tree.bind("<ButtonRelease-1>", getBorrowRecord)
 

# Staff Tab
staff_first_name = StringVar()
staff_last_name = StringVar()
staff_role = StringVar()
staff_email = StringVar()
staff_phone_number = StringVar()
staff_shift = StringVar()
staff_date_hired = StringVar()


Label(staff_tab, text="First Name:").grid(row=1, column=0, sticky="w")
staff_first_name_entry = Entry(staff_tab, textvariable=staff_first_name)
staff_first_name_entry.grid(row=1, column=1, sticky="ew")

Label(staff_tab, text="Last Name:").grid(row=2, column=0, sticky="w")
staff_last_name_entry = Entry(staff_tab, textvariable=staff_last_name)
staff_last_name_entry.grid(row=2, column=1, sticky="ew")

Label(staff_tab, text="Role:").grid(row=3, column=0, sticky="w")
staff_role_entry = Entry(staff_tab, textvariable=staff_role)
staff_role_entry.grid(row=3, column=1, sticky="ew")

Label(staff_tab, text="Email:").grid(row=4, column=0, sticky="w")
staff_email_entry = Entry(staff_tab, textvariable=staff_email)
staff_email_entry.grid(row=4, column=1, sticky="ew")

Label(staff_tab, text="Phone Number:").grid(row=5, column=0, sticky="w")
staff_phone_number_entry = Entry(staff_tab, textvariable=staff_phone_number)
staff_phone_number_entry.grid(row=5, column=1, sticky="ew")

Label(staff_tab, text="Shift:").grid(row=6, column=0, sticky="w")
staff_shift_entry = ttk.Combobox(staff_tab, width=50,values=['morning','evening'] ,textvariable=staff_shift)
staff_shift_entry.grid(row=6, column=1, sticky="ew")

Label(staff_tab, text="Date Hired(yyyy/mm/dd):").grid(row=7, column=0, sticky="w")
staff_date_hired_entry = Entry(staff_tab, textvariable=staff_date_hired)
staff_date_hired_entry.grid(row=7, column=1, sticky="ew")

staff_tree = ttk.Treeview(staff_tab, columns=(
    "StaffID", "FirstName", "LastName", "Role", "Email", "PhoneNumber", "Shift", "DateHired"
), show="headings")
for col in staff_tree["columns"]:
    staff_tree.heading(col, text=col)
    staff_tree.column(col, width=80)
staff_tree.grid(row=9, column=0, columnspan=30, sticky="nsew")

 
def fetchStaffData():
    staff_tree.delete(*staff_tree.get_children())
    staffs = db.fetch_all_staff()
    for row in staffs:
        staff_tree.insert("", END, values=row)
def valid():
    date= r"^\d{4}-\d{2}-\d{2}$"
    if not staff_first_name_entry.get().strip():
        messagebox.showinfo("error","Enter valid frist name")
        return False
    if not staff_last_name_entry.get().strip():
        messagebox.showinfo("error","Enter correct way")
        return False
    if not staff_last_name_entry.get().strip():
        messagebox.showinfo("error","Enter correct last name pls")
        return False
    if not staff_role_entry.get().strip() :
        messagebox.showinfo("error","Enter correct word")
        return False
    if not staff_phone_number_entry.get().strip().isdigit()or len(staff_phone_number_entry.get().strip())!=10:
        messagebox.showinfo("error","enter correct valid phone number pls")
        return False
    if not staff_email_entry .get().strip() or "@" not in staff_email_entry.get().strip():
        messagebox.showinfo("error","Enter correct email address pls")
        return False
    if not staff_shift_entry .get().strip() in ["morning","evening"]:
        messagebox.showinfo("error","your select from Morning or evening")
        return False
    if  not re.match(date,staff_date_hired_entry.get()):
        messagebox.showinfo("error","you keep the this(yyyy-mm-dd")
        return False
    return True
def getStaffRecord(event):
    selected_row = staff_tree.focus()
    data = staff_tree.item(selected_row)
    global staff_row
    staff_row = data['values']

    staff_first_name.set(staff_row[1])
    staff_last_name.set(staff_row[2])
    staff_role.set(staff_row[3])
    staff_email.set(staff_row[4])
    staff_phone_number.set(staff_row[5])
    staff_shift.set(staff_row[6])
    staff_date_hired.set(staff_row[7])

def addStaff():
    if not valid():
        return
    db.add_staff(
            staff_first_name_entry.get(), staff_last_name_entry.get(), staff_role_entry.get(),
            staff_email_entry.get(), staff_phone_number_entry.get(), staff_shift_entry.get(), staff_date_hired_entry.get()
        )
    fetchStaffData()
    clearStaffData()
    messagebox.showinfo("Message", "Staff added successfully!")

def updateStaffData():
    if not valid():
        return
    db.update_staff(
            staff_row[0], staff_first_name_entry.get(), staff_last_name_entry.get(), staff_role_entry.get(),
            staff_email_entry.get(), staff_phone_number_entry.get(), staff_shift_entry.get(), staff_date_hired_entry.get()
        )
    fetchStaffData()
    clearStaffData()
    messagebox.showinfo("Message", "Staff updated successfully!")

def clearStaffData():
     
    staff_first_name.set("")
    staff_last_name.set("")
    staff_role.set("")
    staff_email.set("")
    staff_phone_number.set("")
    staff_shift.set("")
    staff_date_hired.set("")

def deleteStaffData():
    if not staff_row:
        messagebox.showinfo("Message", "Please select a record to delete!")
        return
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this staff?")
    if confirm:
        db.remove_staff(staff_row[0])
        fetchStaffData()
        clearStaffData()
        messagebox.showinfo("Message", "Staff deleted successfully!")

add_staff_button = Button(staff_tab, text="Add", bg="green", width=10, padx=20, pady=5, command=addStaff)
add_staff_button.grid(row=8, column=0, columnspan=2)

delete_staff_button = Button(staff_tab, text="Delete", bg="red", width=10, padx=20, pady=5, command=deleteStaffData)
delete_staff_button.grid(row=8, column=2, columnspan=2)

update_staff_button = Button(staff_tab, text="Update", bg='#01a3a4', width=10, padx=20, pady=5, command=updateStaffData)
update_staff_button.grid(row=8, column=4, columnspan=2)

staff_tree.bind("<ButtonRelease-1>", getStaffRecord)
# publisher tab
 
publisher_name = StringVar()
publisher_address = StringVar()
publisher_phone = StringVar()
publisher_email = StringVar()

Label(publisher_tab, text="Name:").grid(row=1, column=0, sticky="w")
publisher_name_entry = Entry(publisher_tab, textvariable=publisher_name)
publisher_name_entry.grid(row=1, column=1, sticky="ew")

Label(publisher_tab, text="Address:").grid(row=2, column=0, sticky="w")
publisher_address_entry = Entry(publisher_tab, textvariable=publisher_address)
publisher_address_entry.grid(row=2, column=1, sticky="ew")

Label(publisher_tab, text="Phone Number:").grid(row=3, column=0, sticky="w")
publisher_phone_entry = Entry(publisher_tab, textvariable=publisher_phone)
publisher_phone_entry.grid(row=3, column=1, sticky="ew")

Label(publisher_tab, text="Email:").grid(row=4, column=0, sticky="w")
publisher_email_entry = Entry(publisher_tab, textvariable=publisher_email)
publisher_email_entry.grid(row=4, column=1, sticky="ew")

publisher_tree = ttk.Treeview(publisher_tab, columns=(
    "PublisherID", "Name", "Address", "PhoneNumber", "Email"
), show="headings")
for col in publisher_tree["columns"]:
    publisher_tree.heading(col, text=col)
    publisher_tree.column(col, width=80)
publisher_tree.grid(row=6, column=0, columnspan=30, sticky="nsew")

 
def fetchPublisherData():
    publisher_tree.delete(*publisher_tree.get_children())
    publishers = db.fetch_all_publishers()
    for row in publishers:
        publisher_tree.insert("", END, values=row)
def validin():
    if not publisher_name_entry.get().strip():
        messagebox.showinfo("error","try agin your input invalid")
    if not publisher_address_entry.get().strip():
        messagebox.showinfo("error","enter valid input")
    if not publisher_phone_entry.get().strip().isdigit()or len(publisher_phone_entry.get().strip())!=10:
        messagebox.showinfo("error","enter correct valid phone number pls")
        return False
    if not publisher_email_entry .get().strip() or "@" not in publisher_email_entry.get().strip():
        messagebox.showinfo("error","Enter correct email address pls")
        return False
    return True
def getPublisherRecord(event):
    selected_row = publisher_tree.focus()
    data = publisher_tree.item(selected_row)
    global publisher_row
    publisher_row = data['values']

     
    publisher_name.set(publisher_row[1])
    publisher_address.set(publisher_row[2])
    publisher_phone.set(publisher_row[3])
    publisher_email.set(publisher_row[4])

def addPublisher():
    if not validin():
       return
    db.add_publisher(
            publisher_name_entry.get(), publisher_address_entry.get(), publisher_phone_entry.get(), publisher_email_entry.get()
        )
    fetchPublisherData()
    clearPublisherData()
    messagebox.showinfo("Message", "Publisher added successfully!")

def updatePublisherData():
    if not validin():
        return
    db.update_publisher(
            publisher_row[0], publisher_name_entry.get(), publisher_address_entry.get(), publisher_phone_entry.get(), publisher_email_entry.get()
        )
    fetchPublisherData()
    clearPublisherData()
    messagebox.showinfo("Message", "Publisher updated successfully!")

def clearPublisherData():
     
    publisher_name.set("")
    publisher_address.set("")
    publisher_phone.set("")
    publisher_email.set("")

def deletePublisherData():
    if not publisher_row:
        messagebox.showinfo("Message", "Please select a record to delete!")
        return
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this publisher?")
    if confirm:
        db.remove_publisher(publisher_row[0])
        fetchPublisherData()
        clearPublisherData()
        messagebox.showinfo("Message", "Publisher deleted successfully!")

add_publisher_button = Button(publisher_tab, text="Add", bg="green", width=10, padx=20, pady=5, command=addPublisher)
add_publisher_button.grid(row=5, column=1, columnspan=2)

delete_publisher_button = Button(publisher_tab, text="Delete", bg="red", width=10, padx=20, pady=5, command=deletePublisherData)
delete_publisher_button.grid(row=5, column=3, columnspan=2)

update_publisher_button = Button(publisher_tab, text="Update", bg='#01a3a4', width=10, padx=20, pady=5, command=updatePublisherData)
update_publisher_button.grid(row=5, column=5, columnspan=2)

publisher_tree.bind("<ButtonRelease-1>", getPublisherRecord)
# notification tab
 
notification_member_id = StringVar()
notification_date = StringVar()
notification_type = StringVar()
notification_status = StringVar()


Label(notification_tab, text="Member ID:").grid(row=1, column=0, sticky="w")
notification_member_id_entry = Entry(notification_tab, textvariable=notification_member_id)
notification_member_id_entry.grid(row=1, column=1, sticky="ew")

Label(notification_tab, text="Notification Date:").grid(row=2, column=0, sticky="w")
notification_date_entry = Entry(notification_tab, textvariable=notification_date)
notification_date_entry.grid(row=2, column=1, sticky="ew")

Label(notification_tab, text="Notification Type:").grid(row=3, column=0, sticky="w")
notification_type_entry = ttk.Combobox(notification_tab, width=50, values=('Overdue', 'Reminder', 'General'), textvariable=notification_type)
notification_type_entry.grid(row=3, column=1, sticky="ew")

Label(notification_tab, text="Status:").grid(row=4, column=0, sticky="w")
notification_status_entry = ttk.Combobox(notification_tab, width=50, values=('Sent', 'Pending'), textvariable=notification_status)
notification_status_entry.grid(row=4, column=1, sticky="ew")

notification_tree = ttk.Treeview(notification_tab, columns=(
    "NotificationID", "MemberID", "NotificationDate", "NotificationType", "Status"
), show="headings")
for col in notification_tree["columns"]:
    notification_tree.heading(col, text=col)
    notification_tree.column(col, width=80)
notification_tree.grid(row=6, column=0, columnspan=30, sticky="nsew")

def fetchNotificationData():
    notification_tree.delete(*notification_tree.get_children())
    notifications = db.fetch_all_notifications()
    for row in notifications:
        notification_tree.insert("", END, values=row)
def validi():
    date=r"^\d{4}-\d{2}-\d{2}$"
    if not notification_member_id_entry.get().isdigit():
        messagebox.showinfo("error","you must enter valid id")
        return False
    if not re.match(date,notification_date_entry.get().strip()):
        messagebox.showinfo("error","you the incorrect format(yyyy/mm/dd)")
        return False
    if not notification_type_entry.get().strip()  in ['Overdue', 'Reminder', 'General']:
        messagebox.showinfo("error","you must select one from 'Overdue', 'Reminder', 'General")
        return False
    if not notification_status_entry.get().strip() in ['Sent', 'Pending']:
        messagebox.showinfo("error","you must select one from 'Sent', 'Pending'")
        return False
    return True
def getNotificationRecord(event):
    selected_row = notification_tree.focus()
    data = notification_tree.item(selected_row)
    global notification_row
    notification_row = data['values']

     
    notification_member_id.set(notification_row[1])
    notification_date.set(notification_row[2])
    notification_type.set(notification_row[3])
    notification_status.set(notification_row[4])

def addNotification():
    if not validi():
        return
    db.add_notification(
            notification_member_id_entry.get(), notification_date_entry.get(), notification_type_entry.get(), notification_status_entry.get()
        )
    fetchNotificationData()
    clearNotificationData()
    messagebox.showinfo("Message", "Notification added successfully!")

def updateNotificationData():
    if not validi():
        return
    db.update_notification(
            notification_row[0], notification_member_id_entry.get(), notification_date_entry.get(), notification_type_entry.get(), notification_status_entry.get()
        )
    fetchNotificationData()
    clearNotificationData()
    messagebox.showinfo("Message", "Notification updated successfully!")

def clearNotificationData():
    
    notification_member_id.set("")
    notification_date.set("")
    notification_type.set("")
    notification_status.set("")

def deleteNotificationData():
    if not notification_row:
        messagebox.showinfo("Message", "Please select a record to delete!")
        return
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this notification?")
    if confirm:
        db.remove_notification(notification_row[0])
        fetchNotificationData()
        clearNotificationData()
        messagebox.showinfo("Message", "Notification deleted successfully!")


add_notification_button = Button(notification_tab, text="Add", bg="green", width=10, padx=20, pady=5, command=addNotification)
add_notification_button.grid(row=5, column=1, columnspan=2)

delete_notification_button = Button(notification_tab, text="Delete", bg="red", width=10, padx=20, pady=5, command=deleteNotificationData)
delete_notification_button.grid(row=5, column=2, columnspan=2)

update_notification_button = Button(notification_tab, text="Update", bg='#01a3a4', width=10, padx=20, pady=5, command=updateNotificationData)
update_notification_button.grid(row=5, column=4, columnspan=2)


notification_tree.bind("<ButtonRelease-1>", getNotificationRecord)
fetchData()
fetchBookData()
fetchCatalogData()
fetchStaffData()
fetchBorrowData()  
fetchPublisherData()
fetchNotificationData()

root.mainloop()