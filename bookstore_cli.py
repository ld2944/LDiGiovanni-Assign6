import sqlite3

db_name="bookstore.db"

def divider() -> None:
    print("\n" + "~" *50)

def pause() -> None:
    input("\n Please click Enter to continue to the bookstore page!")

def menu() -> None:
    divider()
    print("Menu")
    print("1. View all biography categories")
    print("2. View all books")
    print("3. View books in each category")
    print("4. Search for books by title")
    print("5. Add a new book to our store")
    print("6. Update a book price")
    print("7. Delete a book")
    print("8: Compare 2 book prices")
    print("9. Quit")

def welcome() -> None:
    divider()
    print("Welcome to the Biography Bookstore!")
    print("Use our menu page to search for and manage your biographies.")
    pause()

def view_categories(cursor: sqlite3.Cursor) -> None:
    cursor.execute("SELECT categoryId, categoryName, categoryImage FROM category")

    rows = cursor.fetchall()

    divider()
    print("Biography Categories")

    if rows:
        for row in rows:
            print(row)
    else:
        print("No categories found")

def view_books(cursor: cursor.sqlite3.Cursor) -> None:
     cursor.execute("SELECT bookId, title, author, image FROM book ORDER BY bookId ASC")
     
     rows = cursor.fetchall()
     divider()
     print("All Biographies")
     
     if rows:
        for row in rows:
            print(row)
     else:
        print("No biographies found")

def view_books_categories(cursor: cursor.sqlite3.Cursor) -> None:
    category_Id=input("Enter a category ID: ").strip()
    cursor.execute(
        """
        SELECT category.categoryName, book.title, book.author, book.image 
        FROM book JOIN category ON book.categoryId=category.categoryId
        WHERE category.categoryId=?
        ORDER BY book.title
        """,
        (category_Id,)
        )
    
    rows=cursor.fetchall()

    divider()
    print("Books in category")

    if rows:
        for row in rows:
            print(row)

    else:
        print("No books found")
    
def search_title(cursor:sqlite3.Cursor) -> None:
    title_keyword=input("Enter a title keyword: ").strip()

    cursor.execute(
        """
        SELECT title, author, image, price
        FROM book
        WHERE title LIKE ?
        ORDER BY title ASC
        """,
        (f"%{title_keyword}%",)
    )

    rows=cursor.fetchall()

    divider()
    print("Matching books:")

    if rows:
        for row in rows:
            print(row)

    else:
        print("No books found")

def add_book(cursor: sqlite3.Cursor) -> None:
    try:
        category_id = int(input("Enter category id: ").strip())
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        isbn = input("Enter ISBN: ").strip()
        price = float(input("Enter price: ").strip())
        image = input("Enter image filename: ").strip()
        read_now = int(input("Enter readNow (0 or 1): ").strip())

        cursor.execute(
            """
            INSERT INTO book (categoryId, title, author, isbn, price, image, readNow)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (category_id, title, author, isbn, price, image, read_now)
        )

        divider()
        print("Book added.")

    except ValueError:
        divider()
        print("Invalid input.")
    except sqlite3.IntegrityError as error:
        divider()
        print("Database error:", error)
    

def update_price(cursor: sqlite3.Cursor) -> None:
    try:
        book_id = int(input("Enter book id: ").strip())
        new_price = float(input("Enter the new price: ").strip())
        
        cursor.execute(
        """
        UPDATE book
        SET price=?
        WHERE bookId=?
        """,
        (new_price,book_id)
    )
        divider()
        if cursor.rowcount==0:
            print("No book found")
        else:
            print("The price has been updated")

    except ValueError:
        divider()
        print("Input is invalid")
    
    except sqlite3.IntegrityError as error:
        divider()
        print("Database error: ", error)

def delete_book(cursor: sqlite3.Cursor) -> None:
    try:
        book_id=int(input("Enter the book ID of the book you want to delete: ").strip())
        
        cursor.execute("DELETE FROM book WHERE bookId=?",
        (book_id,)
    )
        divider()
        if cursor.rowcount==0:
            print("No book found")
        else:
            print("The book has been deleted")
    except ValueError:
        divider()
        print("Invalid input.")

def compare_price(cursor: sqlite3.Cursor) -> None:
    book1 = int(input("Enter the first book ID: "))
    book2 = int(input("Enter the second book ID: "))

    cursor.execute(
        """
        SELECT title, price
        FROM book
        WHERE bookId = ? OR bookId = ?
        """,
        (book1, book2)
    )

    rows = cursor.fetchall()


    divider()
    print("Compare prices:")

    if rows:
        for row in rows:
            print(row)
    else:
        print("No books found")

def main() -> None:
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()

        welcome()

        while True:
            menu()
            option=input("Choose an option: "). strip()

            if option=="1":
                view_categories(cursor)
                pause()
            elif option=="2":
                view_books(cursor)
                pause()
            elif option=="3":
                view_books_categories(cursor)
                pause()
            elif option=="4":
                search_title(cursor)
                pause()
            elif option=="5":
                add_book(cursor)
                pause()
            elif option=="6":
                update_price(cursor)
                pause()
            elif option=="7":
                delete_book(cursor)
                pause()
            elif option=="8":
                compare_price(cursor)
                pause()
            elif option=="9":
                divider()
                print("We hope you visit our bookstore again")
                break
            else:
                divider()
                print("Please type in a valid option")
                pause()


if __name__ == "__main__":
    main()
                


