from random import choice

from books import add_books,list_books,get_book
from members import add_members,memberdetail
from issue import issue_book,return_book,list_issues

def menu():
    while True:
        print("****Library Managment System****")
        print("1. Add Book")
        print("2. List Books")
        print("3. Get Book")
        print("4. Add Member")
        print("5. List Members")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. List Active Issues")
        print("9. Exit")

        choice=int(input("enter your choice: "))

        if choice==1:
            add_books(input("Enter the book title: "),input("Enter author's name: "),input("Enter the category: "))
            print("Book data added")

        elif choice==2:
            list = list_books("Enter 'Yes' if you available books or 'No': ")
            for books in list:
                print(books)

        elif choice==3:
            get_book(int(input("Enter the book id you want: ")))

        elif choice==4:
            add_members(input("Enter member's name"),int(input("Enter the member's phone: ")))

        elif choice==5:
            memberdetail(int(input('Enter the member id: ')))

        elif choice==6:
            issue_book(int(input("Enter the id of book: ")),int(input("Enter the id of member: ")))

        elif choice==7:
            return_book(int(input("Enter Issue Id: ")))

        elif choice==8:
            row=list_issues(input("Enter 'yes' if you want books not returned or 'no': "))
            for issue in row:
                print(issue)

        elif choice==9:
            print("Thank You")
            break

menu()


