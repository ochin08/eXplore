# Library System using Hashing
library = {
    "001": "Data Structures and Algorithms",
    "002": "Python Programming",
    "003": "Artificial Intelligence",
    "004": "Cybersecurity Essentials"
}

# Function para hanapin ang libro at ipakita sa loob ng box
def find_book(book_id):
    book = library.get(book_id)
    if book:
        box_width = len(book) + 4  # Adjust width based on book title length, extra padding
        print("╔" + "═" * box_width + "╗")
        print(f"║ {book.center(box_width - 2)} ║")  # Centering the title within the box
        print("╚" + "═" * box_width + "╝")
    else:
        print("❌ Book not found!")

# Function para magdagdag ng libro
def add_book(book_id, book_title):
    if book_id in library:
        print("❌ Book ID already exists!")
    else:
        library[book_id] = book_title
        print(f"✅ Book '{book_title}' added successfully!")

# Function para mag-delete ng libro
def delete_book(book_id):
    if book_id in library:
        removed = library.pop(book_id)
        print(f"✅ Book '{removed}' deleted successfully!")
    else:
        print("❌ Book ID not found!")

# Function para i-display lahat ng books
def display_books():
    if library:
        print("\n📚 Available Books:")
        for book_id, title in library.items():
            print(f"📖 {book_id}: {title}")
    else:
        print("❌ No books available!")

# Function para mag-update ng book title
def update_book(book_id, new_title):
    if book_id in library:
        library[book_id] = new_title
        print(f"✅ Book ID {book_id} updated to '{new_title}'!")
    else:
        print("❌ Book ID not found!")

# Menu System
while True:
    print("\n===== 📖 LIBRARY SYSTEM MENU 📖 =====")
    print("1️⃣  Find a Book")
    print("2️⃣  Add a New Book")
    print("3️⃣  Delete a Book")
    print("4️⃣  Display All Books")
    print("5️⃣ Update Book Title")
    print("6️⃣ Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        book_id = input("Enter Book ID to find: ")
        find_book(book_id)
    
    elif choice == "2":
        book_id = input("Enter New Book ID: ")
        book_title = input("Enter Book Title: ")
        add_book(book_id, book_title)
    
    elif choice == "3":
        book_id = input("Enter Book ID to delete: ")
        delete_book(book_id)
    
    elif choice == "4":
        display_books()
    
    elif choice == "5":
        book_id = input("Enter Book ID to update: ")
        new_title = input("Enter New Title: ")
        update_book(book_id, new_title)
    
    elif choice == "6":
        print("👋 Exiting Library System. Goodbye!")
        break
    
    else:
        print("❌ Invalid choice! Please enter a number between 1-6.")
