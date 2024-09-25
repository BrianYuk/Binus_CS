grocery = []
choice = 0

while choice != 4:
    print("[1] Add Item")
    print("[2] View List")
    print("[3] Remove item")
    print("[4] Quit")
    choice = int(input("Enter choice: "))

    match choice:
        case 1: 
            add = input("Enter the item to add: ")
            grocery.append(add)
            print("Item", add, "added to your grocery list.")
        case 2:
            if len(grocery) > 0:
                for item in grocery:
                    print(item)
            else:
                print("Nothing in list.")
        case 3:
            remove = input("Remove an item from list: ")
            grocery.removed(remove)
            print(f"{remove} has been removed from basket.")
        case 4:
            print("Exiting...")
            break
        case _: print("Invalid command")

"""
same as your calculator, remember to add input validation and error handling. the code shouldnt crash when an item is not found in the list
it should just give feedback to the user! overall the code is still good, just a little incomplete.
"""
