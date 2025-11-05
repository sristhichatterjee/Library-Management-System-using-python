import pickle

# Insert a book record
def insertRec():
    bookid = input('Enter Book ID: ')
    authorname = input('Enter Author Name: ')
    bookname = input('Enter Book Name: ')
    price = int(input('Enter Price: '))

    rec = {'BookID': bookid, 'AuthorName': authorname, 'Book Name': bookname, 'price': price}

    with open('Book.dat', 'ab') as f:
        pickle.dump(rec, f)
    print("✅ Book record inserted successfully!\n")

# Read all book records
def readRec():
    try:
        with open('Book.dat', 'rb') as f:
            while True:
                try:
                    rec = pickle.load(f)
                    print('Book ID:', rec['BookID'])
                    print('Author Name:', rec['AuthorName'])
                    print('Book Name:', rec['Book Name'])
                    print('Price:', rec['price'])
                    print('-' * 30)
                except EOFError:
                    break
    except FileNotFoundError:
        print("❌ No book records found.\n")

# Search book by Author name
def SearchAuthorName(r):
    found = False
    try:
        with open('Book.dat', 'rb') as f:
            while True:
                try:
                    rec = pickle.load(f)
                    if rec['AuthorName'] == r:
                        print('Book ID:', rec['BookID'])
                        print('Author Name:', rec['AuthorName'])
                        print('Book Name:', rec['Book Name'])
                        print('Price:', rec['price'])
                        found = True
                except EOFError:
                    break
    except FileNotFoundError:
        print("❌ No records found.\n")
        return

    if not found:
        print("❌ Author not found.\n")

# Search book by Book ID
def SearchBookID(bid):
    found = False
    try:
        with open('Book.dat', 'rb') as f:
            while True:
                try:
                    rec = pickle.load(f)
                    if rec['BookID'] == bid:
                        print('Book ID:', rec['BookID'])
                        print('Author Name:', rec['AuthorName'])
                        print('Book Name:', rec['Book Name'])
                        print('Price:', rec['price'])
                        found = True
                except EOFError:
                    break
    except FileNotFoundError:
        print("❌ No records found.\n")
        return

    if not found:
        print("❌ Book ID not found.\n")

# Update price of a book
def updatePrice(r, m):
    try:
        with open('Book.dat', 'rb') as f:
            reclst = []
            while True:
                try:
                    rec = pickle.load(f)
                    reclst.append(rec)
                except EOFError:
                    break
        updated = False
        for i in range(len(reclst)):
            if reclst[i]['AuthorName'] == r:
                reclst[i]['price'] = m
                updated = True
        with open('Book.dat', 'wb') as f:
            for rec in reclst:
                pickle.dump(rec, f)
        if updated:
            print("✅ Price updated successfully!\n")
        else:
            print("❌ Author not found.\n")
    except FileNotFoundError:
        print("❌ No records to update.\n")


#Delete Book by Book ID
import pickle

def deleteRec(bid):
    try:
        f = open('Book.dat', 'rb')
        reclst = []
        while True:
            try:
                rec = pickle.load(f)
                reclst.append(rec)
            except EOFError:
                break
        f.close()

        found = False
        f = open('Book.dat', 'wb')
        for x in reclst:
            if x.get('BookID') == bid:   # match BookID safely
                found = True
                print(f"🗑️ Deleted Book Record:\n  Book ID: {x.get('BookID')}\n  Author: {x.get('AuthorName')}\n  Book: {x.get('Book Name')}\n  Price: {x.get('price')}")
                continue   # skip saving this record
            pickle.dump(x, f)
        f.close()

        if found:
            print("\n✅ Record deleted successfully!")
        else:
            print("\n❌ No book found with that Book ID.")

    except FileNotFoundError:
        print("\n❌ No book records found.")


#safety
def readRec():
    try:
        with open('Book.dat', 'rb') as f:
            while True:
                try:
                    rec = pickle.load(f)
                    print('Book ID:', rec.get('BookID', 'N/A'))   # Safe access
                    print('Author Name:', rec['AuthorName'])
                    print('Book Name:', rec['Book Name'])
                    print('Price:', rec['price'])
                    print('-' * 30)
                except EOFError:
                    break
    except FileNotFoundError:
        print("❌ No book records found.\n")


# ================= USER RECORDS ==================

def insertUser():
    username = input('Enter the Username: ')
    userid = input('Enter the User ID: ')
    age = int(input('Enter the Age: '))
    rec = {'Username': username, 'UserID': userid, 'Age': age}

    with open('User.dat', 'ab') as f:
        pickle.dump(rec, f)
    print("✅ User record inserted successfully!\n")

def readUser():
    try:
        with open('User.dat', 'rb') as f:
            while True:
                try:
                    rec = pickle.load(f)
                    print('Username:', rec['Username'])
                    print('User ID:', rec['UserID'])
                    print('Age:', rec['Age'])
                    print('-' * 30)
                except EOFError:
                    break
    except FileNotFoundError:
        print("❌ No user records found.\n")

def SearchUser(name):
    found = False
    try:
        with open('User.dat', 'rb') as f:
            while True:
                try:
                    rec = pickle.load(f)
                    if rec['Username'] == name:
                        print('Username:', rec['Username'])
                        print('User ID:', rec['UserID'])
                        print('Age:', rec['Age'])
                        found = True
                except EOFError:
                    break
    except FileNotFoundError:
        print("❌ No records found.\n")
        return
    if not found:
        print("❌ User not found.\n")

def UpdateAge(name, new_age):
    try:
        with open('User.dat', 'rb') as f:
            records = []
            while True:
                try:
                    rec = pickle.load(f)
                    records.append(rec)
                except EOFError:
                    break
        updated = False
        for i in range(len(records)):
            if records[i]['Username'] == name:
                records[i]['Age'] = new_age
                updated = True
        with open('User.dat', 'wb') as f:
            for rec in records:
                pickle.dump(rec, f)
        if updated:
            print("✅ Age updated successfully!\n")
        else:
            print("❌ User not found.\n")
    except FileNotFoundError:
        print("❌ No records to update.\n")

def deleteUser(name):
    try:
        with open('User.dat', 'rb') as f:
            records = []
            while True:
                try:
                    rec = pickle.load(f)
                    records.append(rec)
                except EOFError:
                    break
        with open('User.dat', 'wb') as f:
            for rec in records:
                if rec['Username'] != name:
                    pickle.dump(rec, f)
        print("✅ User record deleted (if existed).\n")
    except FileNotFoundError:
        print("❌ No user records found.\n")

# ================= MAIN MENU ==================
while True:
    print("\n=========== BOOK RECORD MENU ===========")
    print("1. Insert Book Record")
    print("2. Display All Book Records")
    print("3. Search Book by Author Name")
    print("4. Search Book by Book ID")
    print("5. Update Book Price")
    print("6. Delete Book by Book ID")
    print("=========== USER RECORD MENU ===========")
    print("7. Insert User Record")
    print("8. Display All User Records")
    print("9. Search User by Name")
    print("10. Update User Age")
    print("11. Delete User Record")
    print("12. Exit")
    print("========================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insertRec()
    elif choice == 2:
        readRec()
    elif choice == 3:
        r = input("Enter Author Name to search: ")
        SearchAuthorName(r)
    elif choice == 4:
        bid = input("Enter Book ID to search: ")
        SearchBookID(bid)
    elif choice == 5:
        r = input("Enter Author Name: ")
        m = int(input("Enter new Price: "))
        updatePrice(r, m)
    elif choice == 6:
        bid = input("Enter Book ID to delete: ")
        deleteRec(bid)
    elif choice == 7:
        insertUser()
    elif choice == 8:
        readUser()
    elif choice == 9:
        name = input("Enter Username to Search: ")
        SearchUser(name)
    elif choice == 10:
        name = input("Enter Username to Update: ")
        new_age = int(input("Enter new Age: "))
        UpdateAge(name, new_age)
    elif choice == 11:
        name = input("Enter Username to delete: ")
        deleteUser(name)
    elif choice == 12:
        print("🚪 Exiting program... Bye!")
        break
    else:
        print("❌ Invalid choice! Try again.\n")
