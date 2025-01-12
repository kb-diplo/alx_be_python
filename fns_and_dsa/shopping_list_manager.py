def display_menu():  
    print("Shopping List Manager")  
    print("1. Add Item")  
    print("2. Remove Item")  
    print("3. View List")  
    print("4. Exit")  

def main():  
    shopping_list = []  
    while True:  
        display_menu()  
        choice = int(input("Enter your choice: "))  

        if choice == 1:  
            shopping_list.append(input("Enter the item to add: "))  
        elif choice == 2:  
            shopping_list.remove(input("Enter the item to remove: "))  
        elif choice == 3:  
            print("Shopping list:")  
            print(shopping_list)  
        elif choice == 4:  
            print("Goodbye!")  
            break  
        else:  
            print("Invalid choice. Please try again.")  

if __name__ == "__main__":  
    main()
