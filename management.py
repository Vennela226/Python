# High-Level Python Program: Library Management System

library = {}

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    library[book_id] = {"Title": title, "Author": author}
    print("Book added successfully!\n")

def view_books():
    if not library:
        print("No books available.\n")
        return

    print("\n--- Available Books ---")
    for book_id, details in library.items():
        print(f"Book ID: {book_id}, Title: {details['Title']}, Author: {details['Author']}")
    print()

def search_book():
    book_id = input("Enter Book ID to search: ")
    if book_id in library:
        book = library[book_id]
        print(f"Found → Title: {book['Title']}, Author: {book['Author']}\n")
    else:
        print("Book not found.\n")

def count_books():
    print(f"Total number of books: {len(library)}\n")

def main_menu():
    while True:
        print("===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Count Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            count_books()
        elif choice == "5":
            print("Exiting Program. Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")

main_menu()
