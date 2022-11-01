while True:
    print("\nSelect an option from the menu ")
    print("1. Add Donor")
    print("2. View all donors")
    print("3. Search a donor")
    print("4. Update donor")
    print("5. Delete donor")
    print("6.exit\n")

    choice = int(input("Enter an option: "))
    if(choice == 1):
        print("Donor data entry selected")
    elif(choice == 2):
        print("View Donor")
    elif(choice == 3):
        print("Searching a Donor")
    elif (choice == 4):
        print("update Donor")
    elif(choice == 5):
        print("delete a Donor")
    elif(choice==6):
        break