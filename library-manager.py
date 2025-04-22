library:list = []

def add_a_book(library):
    
    title = input("Enter books title").lower()
    author= input("Enter author name").lower()
    Genre = input("Enter Genera").lower()
    year = input("Enter books publication year")
    isread =input("Have you read this book (yes/no)").lower()
    
    new_book = {
        "title":title,
        "author":author,
        "Genre":Genre,
        "year":year,
        "isread":isread
    }
    
    library.append(new_book)
    print(f"your book{title} has been added ")
    
def remove_a_book(library):
    remove_by_title = input("Enter book title").lower()
    selected_book = next((book for book in library if book["title"]==remove_by_title),None)
    if selected_book :
           library.remove(selected_book)
           print("your book has been removed")
           
def display_all_book(library):
    if library:
        for book in library:
            print(
                f"""
                title: {book["title"]}
                author: {book["author"]}
                Genre: {book["Genre"]}
                year: {book["year"]}
                isread: {book["isread"]}
                """
            )
    else:
        print("your library is empty")
        
def search_a_book(library):
    search_input = input("Enter your book title").lower()
    searched_book = next((book for book in library if book["title"]==search_input),None)
       #print(searched_book)
    if searched_book:  
           print(f"""
            **Title:** {searched_book['title']}  
            **Author:** {searched_book['author']}  
            **Genre:** {searched_book['Genre']}  
            **Publication Year:** {searched_book['year']}  
            **Read:** {"Yes" if searched_book["isread"] else "No"}
            """)
    else:
       print("Book not found")
       
def display_statistics(library):
    total_books = len(library)
    read_book = sum(1 for book in library if book["isread"])  
    percentage_read = (read_book/ total_books) * 100 if total_books > 0 else 0  
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")  
    
def main():
     while True:
        print("\nMenu")
        print("1) Add a book")
        print("2) Remove a book")
        print("3) Search the library")
        print("4) Display all books")
        print("5) Display statistics")
        print("6) Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_a_book(library)
        elif choice == '2':
            remove_a_book(library)
        elif choice == '3':
            search_a_book(library)
        elif choice == '4':
            display_all_book(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("Happy to assist you Goodbye!")
            break
        else:
            print("Invalid choice, please try again!")    
                    
main()            