# displayMenu:
# displays a menu with options
# DO NOT MODIFY THIS FUNCTION
import Library as Library

if __name__ == "__main__":

    def display_menu():
        print("Select a numerical option:")
        print("======Main Menu=====")
        print("1. Read book file")
        print("2. Read user file")
        print("3. Print book list")
        print("4. Get rating")
        print("5. Find number of books user rated")
        print("6. View ratings")
        print("7. Get average rating")
        print("8. Add a user")
        print("9. Checkout a book")
        print("10. Get recommendations (not implemented yet)")
        print("11. Quit")


    if __name__ == "__main__":

        my_lib = Library.Library()
        choice = "-1"

        while choice != 11:
            display_menu()
            choice = input()
            try:
                choice = int(choice)
            except:
                print("Invalid input")
                continue

            if choice == 1:
                filename = input("Enter a book file name:\n")
                a = int(my_lib.read_books(filename))
                if a == -1:
                    print('No books saved to the database.')
                if a == -2:
                    print('Database is already full. No books were added.')
                if a == int(my_lib.get_size_books()):
                    print("Database is full. Some books may have not been added.")
                if a != -1 and a != -2 and a != int(my_lib.get_size_books()):
                    print('Total books in the database:', a)

            elif choice == 2:
                filename = input("Enter a user file name:\n")
                b = int(my_lib.read_ratings(filename))
                if  b == -1:
                    print("No users saved to the database.")
                if b == -2:
                    print("Database is already full. No users were added.")
                if b == int(my_lib.get_size_users()):
                    print("Database is full. Some users may have not been added.")
                if b != -1 and b != -2 and b != int(my_lib.get_size_users()):
                    print('Total users in the database:', b)

            elif choice == 3:
                if int(my_lib.get_num_users()) == 0 or int(my_lib.get_num_books()) == 0:
                    print('Database has not been fully initialized.')
                else:
                    my_lib.print_all_books()

            elif choice == 4:
                if int(my_lib.get_num_users()) == 0 or int(my_lib.get_num_books()) == 0:
                    print('Database has not been fully initialized.')
                else:
                    # Get a user name from the user's input
                    username = input('Enter user name:\n')
                    # Get a book title from the user's input
                    booktitle = input('Enter book title:\n')
                    c = int(my_lib.get_rating(username,booktitle))
                    if c == 0:
                        print(username,'has not rated', booktitle)
                    if c == -3:
                        print(username,'or', booktitle, 'does not exist')
                    if c != 0 and c != -3:
                        print(username, 'rated', booktitle, 'with', c)

            elif choice == 5:
                if int(my_lib.get_num_users()) == 0 or int(my_lib.get_num_books()) == 0:
                    print('Database has not been fully initialized.')
                else:
                    username = input('Enter user name:\n')
                    d = int(my_lib.get_count_read_books(username))
                    if d == 0:
                        print(username,'has not rated any books')
                    if d == -3:
                        print(username,'does not exist')
                    if d != 0 and d != -3:
                        print(username, 'rated', d, 'books')

            elif choice == 6:
                if int(my_lib.get_num_users()) == 0 or int(my_lib.get_num_books()) == 0:
                    print('Database has not been fully initialized')
                else:
                    username = input('Enter user name:\n')
                    my_lib.view_ratings(username)

            elif choice == 7:
                if int(my_lib.get_num_users()) == 0 or int(my_lib.get_num_books()) == 0:
                    print('Database has not been fully initialized.\n')
                else:
                    booktitle = input('Enter book title:\n')
                    a = my_lib.calc_avg_rating(booktitle)
                    if int(a) == -3:
                        print(booktitle, 'does not exist\n')
                    else:
                        print('The average rating for', booktitle, 'is', a)
                        print()
                continue

            elif choice == 8:
                username = input('Enter the new user\'s name:\n')
                b = my_lib.add_user(username)
                if b == -2:
                    print("Database is full.", username,"was not added")
                    print()
                if b == 0:
                    print(username, 'already exists in the library')
                    print()
                if b != -2 and b != 0:
                    print('Welcome to the library,', username)
                    print()
                continue

            elif choice == 9:
                if int(my_lib.get_num_users()) == 0 or int(my_lib.get_num_books()) == 0:
                    print('Database has not been fully initialized.')
                    print()

                else:
                    username = input('Enter the new user\'s name:\n')
                    booktitle = input('Enter book title:\n')
                    newrating = int(input('Enter rating for the book:\n'))
                    c = my_lib.check_out_book(username, booktitle, newrating)
                    if c == -4:
                        print('Rating is not valid')
                        print()
                    if c == -3:
                        print(username, 'or', booktitle, 'does not exist')
                        print()
                    if c != -4 and c!= -3:
                        print("Hope you enjoyed your book; the rating has been updated.")
                        print()
                continue

            elif choice == 10:
                # haven't decided what to do..lol
                continue

            elif choice == 11:
                print("Goodbye!")

            else:
                print("Invalid input")

            print()
