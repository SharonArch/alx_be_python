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
        try:
            choice = int(input("Enter your choice: "))   # 👈 must be int
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")
            continue

        if choice == 1:
            item = input("Enter the item to add: ")  # 👈 must match exactly
            shopping_list.append(item)
        elif choice == 2:
            item = input("Enter the item to remove: ")  # 👈 must match exactly
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item not found in the list.")
        elif choice == 3:
            print("\nYour Shopping List:")
            if shopping_list:
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

