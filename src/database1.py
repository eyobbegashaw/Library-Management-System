import sqlite3

class LibraryDB:
    def __init__(self, db_name='library.db'):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
         
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Member (
                                MemberID INTEGER PRIMARY KEY AUTOINCREMENT,
                                SSN TEXT,
                                FirstName TEXT,
                                LastName TEXT,
                                CampusAddress TEXT,
                                HomeAddress TEXT,
                                PhoneNumber TEXT,
                                MembershipType TEXT,
                                CardIssuedDate TEXT,
                                CardExpiryDate TEXT,
                                Status TEXT,
                                Email TEXT,
                                Photo BLOB,
                                BorrowingHistory TEXT,
                                PenaltyBalance REAL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Book (
                                BookID INTEGER PRIMARY KEY  AUTOINCREMENT,
                                ISBN TEXT,
                                Title TEXT,  
                                Author TEXT,
                                SubjectArea TEXT,
                                BindingType TEXT,
                                IsLendable TEXT,
                                CopiesAvailable INTEGER,
                                CopiesOnLoan INTEGER)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Catalog (
                                CatalogID INTEGER PRIMARY KEY  AUTOINCREMENT ,
                                ISBN TEXT,
                                Description TEXT,
                                FOREIGN KEY (ISBN) REFERENCES Book(ISBN))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS BorrowingActivity (
                                TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
                                MemberID INTEGER,
                                BookID INTEGER,
                                BorrowDate TEXT,
                                DueDate TEXT,
                                ReturnDate TEXT,
                                Status TEXT,
                                FOREIGN KEY (MemberID) REFERENCES Member(MemberID),
                                FOREIGN KEY (BookID) REFERENCES Book(BookID))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Staff (
                                StaffID INTEGER PRIMARY KEY AUTOINCREMENT,
                                FirstName TEXT,
                                LastName TEXT,
                                Role TEXT,
                                Email TEXT,
                                PhoneNumber TEXT,
                                Shift TEXT,
                                DateHired TEXT)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Publisher (
                                PublisherID INTEGER PRIMARY KEY  AUTOINCREMENT ,
                                Name TEXT,
                                Address TEXT,
                                PhoneNumber TEXT,
                                Email TEXT)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Notifications (
                                NotificationID INTEGER PRIMARY KEY AUTOINCREMENT,
                                MemberID INTEGER,
                                NotificationDate TEXT,
                                NotificationType TEXT,
                                Status TEXT,
                                FOREIGN KEY (MemberID) REFERENCES Member(MemberID))''')

        self.connection.commit()

    def close(self):
        self.connection.close()
    # Add Methods for Each Table
    def add_member(self, ssn, first_name, last_name, campus_address, home_address, phone_number, membership_type, card_issued_date, card_expiry_date, status, email, photo, borrowing_history, penalty_balance):
        self.cursor.execute('''INSERT INTO Member (SSN, FirstName, LastName, CampusAddress, HomeAddress, PhoneNumber, MembershipType, CardIssuedDate, CardExpiryDate, Status, Email, Photo, BorrowingHistory, PenaltyBalance)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                            (ssn, first_name, last_name, campus_address, home_address, phone_number, membership_type, card_issued_date, card_expiry_date, status, email, photo, borrowing_history, penalty_balance))
        self.connection.commit()

    def add_book(self, isbn, title, author, subject_area, binding_type, is_lendable, copies_available, copies_on_loan):
        self.cursor.execute('''INSERT INTO Book (ISBN, Title, Author, SubjectArea, BindingType, IsLendable, CopiesAvailable, CopiesOnLoan)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                            (isbn, title, author, subject_area, binding_type, is_lendable, copies_available, copies_on_loan))
        self.connection.commit()

    def add_catalog(self, isbn, description):
        self.cursor.execute('''INSERT INTO Catalog (ISBN, Description)
                                VALUES (?, ?)''',
                            (isbn, description))
        self.connection.commit()

    def add_borrowing_activity(self, member_id, book_id, borrow_date, due_date, return_date, status):
        self.cursor.execute('''INSERT INTO BorrowingActivity (MemberID, BookID, BorrowDate, DueDate, ReturnDate, Status)
                                VALUES (?, ?, ?, ?, ?, ?)''',
                            (member_id, book_id, borrow_date, due_date, return_date, status))
        self.connection.commit()

    def add_staff(self, first_name, last_name, role, email, phone_number, shift, date_hired):
        self.cursor.execute('''INSERT INTO Staff (FirstName, LastName, Role, Email, PhoneNumber, Shift, DateHired)
                                VALUES (?, ?, ?, ?, ?, ?, ?)''',
                            (first_name, last_name, role, email, phone_number, shift, date_hired))
        self.connection.commit()

    def add_publisher(self, name, address, phone_number, email):
        self.cursor.execute('''INSERT INTO Publisher (Name, Address, PhoneNumber, Email)
                                VALUES (?, ?, ?, ?)''',
                            (name, address, phone_number, email))
        self.connection.commit()

    def add_notification(self, member_id, notification_date, notification_type, status):
        self.cursor.execute('''INSERT INTO Notifications (MemberID, NotificationDate, NotificationType, Status)
                                VALUES (?, ?, ?, ?)''',
                            (member_id, notification_date, notification_type, status))
        self.connection.commit()
    # Fetch Methods
    def fetch_all_members(self):
        self.cursor.execute('SELECT * FROM Member')
        return self.cursor.fetchall()

    def fetch_all_books(self):
        self.cursor.execute('SELECT * FROM Book')
        return self.cursor.fetchall()

    def fetch_all_catalog(self):
        self.cursor.execute('SELECT * FROM Catalog')
        return self.cursor.fetchall()

    def fetch_all_borrowing_activity(self):
        self.cursor.execute('SELECT * FROM BorrowingActivity')
        return self.cursor.fetchall()

    def fetch_all_staff(self):
        self.cursor.execute('SELECT * FROM Staff')
        return self.cursor.fetchall()

    def fetch_all_publishers(self):
        self.cursor.execute('SELECT * FROM Publisher')
        return self.cursor.fetchall()

    def fetch_all_notifications(self):
        self.cursor.execute('SELECT * FROM Notifications')
        return self.cursor.fetchall()
    # Update Methods
    def update_member(self, member_id, ssn, first_name, last_name, campus_address, home_address, phone_number, membership_type, card_issued_date, card_expiry_date, status, email, photo, borrowing_history, penalty_balance):
        self.cursor.execute('''UPDATE Member SET SSN = ?, FirstName = ?, LastName = ?, CampusAddress = ?, HomeAddress = ?, PhoneNumber = ?, MembershipType = ?, CardIssuedDate = ?, CardExpiryDate = ?, Status = ?, Email = ?, Photo = ?, BorrowingHistory = ?, PenaltyBalance = ? WHERE MemberID = ?''',
                            (ssn, first_name, last_name, campus_address, home_address, phone_number, membership_type, card_issued_date, card_expiry_date, status, email, photo, borrowing_history, penalty_balance, member_id))
        self.connection.commit()

    def update_book(self, book_id, isbn, title, author, subject_area, binding_type, is_lendable, copies_available, copies_on_loan):
        self.cursor.execute('''UPDATE Book SET ISBN = ?, Title = ?, Author = ?, SubjectArea = ?, BindingType = ?, IsLendable = ?, CopiesAvailable = ?, CopiesOnLoan = ? WHERE BookID = ?''',
                            (isbn, title, author, subject_area, binding_type, is_lendable, copies_available, copies_on_loan, book_id))
        self.connection.commit()

    def update_catalog(self, catalog_id, isbn, description):
        self.cursor.execute('''UPDATE Catalog SET ISBN = ?, Description = ? WHERE CatalogID = ?''',
                            (isbn, description, catalog_id))
        self.connection.commit()

    def update_borrowing_activity(self, transaction_id, member_id, book_id, borrow_date, due_date, return_date, status):
        self.cursor.execute('''UPDATE BorrowingActivity SET MemberID = ?, BookID = ?, BorrowDate = ?, DueDate = ?, ReturnDate = ?, Status = ? WHERE TransactionID = ?''',
                            (member_id, book_id, borrow_date, due_date, return_date, status, transaction_id))
        self.connection.commit()

    def update_staff(self, staff_id, first_name, last_name, role, email, phone_number, shift, date_hired):
        self.cursor.execute('''UPDATE Staff SET FirstName = ?, LastName = ?, Role = ?, Email = ?, PhoneNumber = ?, Shift = ?, DateHired = ? WHERE StaffID = ?''',
                            (first_name, last_name, role, email, phone_number, shift, date_hired, staff_id))
        self.connection.commit()

    def update_publisher(self, publisher_id, name, address, phone_number, email):
        self.cursor.execute('''UPDATE Publisher SET Name = ?, Address = ?, PhoneNumber = ?, Email = ? WHERE PublisherID = ?''',
                            (name, address, phone_number, email, publisher_id))
        self.connection.commit()

    def update_notification(self, notification_id, member_id, notification_date, notification_type, status):
        self.cursor.execute('''UPDATE Notifications SET MemberID = ?, NotificationDate = ?, NotificationType = ?, Status = ? WHERE NotificationID = ?''',
                            (member_id, notification_date, notification_type, status, notification_id))
        self.connection.commit()
    # Remove Methods
    def remove_member(self, member_id):
        self.cursor.execute('DELETE FROM Member WHERE MemberID = ?', (member_id,))
        self.connection.commit()

    def remove_book(self, book_id):
        self.cursor.execute('DELETE FROM Book WHERE BookID = ?', (book_id,))
        self.connection.commit()

    def remove_catalog(self, catalog_id):
        self.cursor.execute('DELETE FROM Catalog WHERE CatalogID = ?', (catalog_id,))
        self.connection.commit()

    def remove_borrowing_activity(self, transaction_id):
        self.cursor.execute('DELETE FROM BorrowingActivity WHERE TransactionID = ?', (transaction_id,))
        self.connection.commit()

    def remove_staff(self, staff_id):
        self.cursor.execute('DELETE FROM Staff WHERE StaffID = ?', (staff_id,))
        self.connection.commit()

    def remove_publisher(self, publisher_id):
        self.cursor.execute('DELETE FROM Publisher WHERE PublisherID = ?', (publisher_id,))
        self.connection.commit()

    def remove_notification(self, notification_id):
        self.cursor.execute('DELETE FROM Notifications WHERE NotificationID = ?', (notification_id,))
        self.connection.commit()