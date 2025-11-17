import json

# Initial Library Data
library = {
    "001": {"title": "Data Structures and Algorithms", "author": "Mark Allen", "publisher": "McGraw-Hill"},
    "002": {"title": "Python Programming", "author": "John Doe", "publisher": "Packt"},
    "003": {"title": "Artificial Intelligence", "author": "Jane Smith", "publisher": "Elsevier"},
    "004": {"title": "Cybersecurity Essentials", "author": "Michael Brown", "publisher": "Wiley"}
}

# Function to save library to a file
def save_library():
    with open('library.json', 'w') as f:
        json.dump(library, f)
    print("✅ Library saved to 'library.json'.")

# Function to load library from a file
def load_library():
    global library
    try:
        with open('library.json', 'r') as f:
            library = json.load(f)
        print("✅ Library loaded from 'library.json'.")
    except FileNotFoundError:
        print("❌ No previous library data found, starting with default data.")

# Function to find a book by ID or title (case-insensitive)
def find_book(book_id_or_title):
    book_id_or_title = book_id_or_title.lower()
    found = False
    max_length = 0  # To track the longest title for consistent box width
    book_details = {}

    for book_id, book_info in library.items():
        if book_id == book_id_or_title or book_info['title'].lower() == book_id_or_title:
            found = True
            book_details = book_info
            max_length = len(book_info['title'])  # Set max_length based on found book title
            break
    
    if found:
        # Calculate box width based on longest title
        box_width = max_length + 15  # Adjust width based on title length with extra padding
        print("╔" + "═" * box_width + "╗")
        print(f"║ {book_details['title'].center(box_width - 2)} ║")
        print(f"║ Author: {book_details['author'].ljust(box_width - 10)} ║")
        print(f"║ Publisher: {book_details['publisher'].ljust(box_width - 13)} ║")
        print("╚" + "═" * box_width + "╝")
    else:
        print("❌ Book not found!")


# Function to add a new book
def add_book(book_id, book_title, author, publisher):
    if book_id in library:
        print("❌ Book ID already exists!")
    else:
        library[book_id] = {"title": book_title, "author": author, "publisher": publisher}
        print(f"✅ Book '{book_title}' added successfully!")

# Function to delete a book by ID
def delete_book(book_id):
    if book_id in library:
        removed = library.pop(book_id)
        print(f"✅ Book '{removed['title']}' deleted successfully!")
    else:
        print("❌ Book ID not found!")

# Function to display all books sorted by title
def display_books():
    if library:
        sorted_books = sorted(library.items(), key=lambda item: item[1]['title'])
        print("\n📚 Available Books:")
        for book_id, book_info in sorted_books:
            print(f"📖 {book_id}: {book_info['title']} (Author: {book_info['author']}, Publisher: {book_info['publisher']})")
    else:
        print("❌ No books available!")

# Function to update a book's title, author, or publisher
def update_book(book_id, new_title=None, new_author=None, new_publisher=None):
    if book_id in library:
        if new_title:
            library[book_id]["title"] = new_title
        if new_author:
            library[book_id]["author"] = new_author
        if new_publisher:
            library[book_id]["publisher"] = new_publisher
        print(f"✅ Book ID {book_id} updated!")
    else:
        print("❌ Book ID not found!")

# Menu System
load_library()  # Load previous library data if available

while True:
    print("\n===== 📖 LIBRARY SYSTEM MENU 📖 =====")
    print("1️⃣  Find a Book (by ID or Title)")
    print("2️⃣  Add a New Book")
    print("3️⃣  Delete a Book")
    print("4️⃣  Display All Books")
    print("5️⃣  Update Book Information")
    print("6️⃣  Save Library")
    print("7️⃣  Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        book_id_or_title = input("Enter Book ID or Title to find: ")
        find_book(book_id_or_title)
    
    elif choice == "2":
        book_id = input("Enter New Book ID: ")
        book_title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        publisher = input("Enter Publisher: ")
        add_book(book_id, book_title, author, publisher)
    
    elif choice == "3":
        book_id = input("Enter Book ID to delete: ")
        delete_book(book_id)
    
    elif choice == "4":
        display_books()
    
    elif choice == "5":
        book_id = input("Enter Book ID to update: ")
        new_title = input("Enter New Title (leave blank to skip): ")
        new_author = input("Enter New Author (leave blank to skip): ")
        new_publisher = input("Enter New Publisher (leave blank to skip): ")
        update_book(book_id, new_title, new_author, new_publisher)
    
    elif choice == "6":
        save_library()
    
    elif choice == "7":
        print("👋 Exiting Library System. Goodbye!")
        break
    
    else:
        print("❌ Invalid choice! Please enter a number between 1-7.")
