# Book class to represent a book in the library
class Book:
    def __init__(self, title, author):
        self.title = title  # Title of the book
        self.author = author  # Author of the book
        self.availability_status = True  # Availability status of the book (True if available)

# Library class to manage a collection of books
class Library:
    def __init__(self):
        self.books = []  # List to store books in the library

    # Method to add a book to the library
    def add_book(self, book):
        self.books.append(book)  # Append the book to the list
        print(f'Book "{book.title}" by author "{book.author}" added to library.')

    # Method to borrow a book from the library
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():  # Check for case-insensitive title match
                if book.availability_status:  # Check if the book is available
                    book.availability_status = False  # Mark the book as borrowed
                    print(f'You have borrowed "{book.title}".')
                    return
                else:
                    print(f'Sorry "{book.title}" is currently unavailable.')  # Book is not available
                    return
        print(f'Sorry, book titled "{title}" not found in the library.')  # Book not found

    # Method to return a borrowed book to the library
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():  # Check for case-insensitive title match
                if not book.availability_status:  # Check if the book was borrowed
                    book.availability_status = True  # Mark the book as available
                    print(f'Thank you for returning "{book.title}".')
                    return
                else:
                    print(f'Book title "{book.title}" was not borrowed')  # Book was not borrowed
                    return
        print(f'Sorry, book titled "{title}" not found in the library.')  # Book not found

    # Method to list all books in the library with their availability status
    def list_books(self):
        if not self.books:  # Check if there are no books in the library
            print('No books in the library')
            return
        print('Books in the library:')
        for book in self.books:
            # Determine the availability status
            if book.availability_status:
                status = "Available"
            else:
                status = "Unavailable"
            print(f'"{book.title}" by "{book.author}" - {status}')  # Print book details

    # Method to search for a book by title
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():  # Check for case-insensitive title match
                # Determine the availability status
                if book.availability_status:
                    status = "Available"
                else:
                    status = "Unavailable"
                print(f'Book found: "{book.title}" by "{book.author}" - {status}')  # Print book details
                return
        print(f'Sorry, book titled "{title}" not found in the library.')  # Book not found

    # Method to count and display the number of available books
    def count_available_books(self):
        count = 0  # Initialize count
        for book in self.books:
            if book.availability_status:  # Check if the book is available
                count += 1  # Increment count
        print(f'Number of available books: {count}')  # Print the count
        return count  # Return the count

# Main Program
def menu():
    library = Library()  # Create an instance of the Library class
    while True:
        # Display the menu options
        print("\nLibrary Management System")
        print("1. Add book")
        print("2. Borrow book")
        print("3. Return book")
        print("4. List books")
        print("5. Search book")
        print("6. Count Available Books")
        print("7. Exit")
        user_choice = input("Enter your choice: ")  # Get user input

        # Handle user choices
        if user_choice == "1":
            title = input("Enter the book title: ")  # Get book title
            author = input("Enter book author: ")  # Get book author
            book = Book(title, author)  # Create a new Book instance
            library.add_book(book)  # Add the book to the library
        elif user_choice == "2":
            title = input("Enter the book title to borrow: ")  # Get title of the book to borrow
            library.borrow_book(title)  # Borrow the book
        elif user_choice == "3":
            title = input("Enter the book title to return: ")  # Get title of the book to return
            library.return_book(title)  # Return the book
        elif user_choice == "4":
            library.list_books()  # List all books in the library
        elif user_choice == "5":
            title = input("Enter the book title to search: ")  # Get title of the book to search
            library.search_book(title)  # Search for the book
        elif user_choice == "6":
            library.count_available_books()  # Count and display available books
        elif user_choice == "7":
            print("Exiting the Library Management System. Goodbye!")  # Exit message
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

# Entry point of the program
if __name__ == "__main__":
    menu()  # Call the menu function to start the program