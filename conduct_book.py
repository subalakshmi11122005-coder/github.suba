contacts = {}

while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact Added Successfully!")

    elif choice == "2":
        if contacts:
            print("\nContact List:")
            for name, details in contacts.items():
                print(f"Name: {name}, Phone: {details['Phone']}")
        else:
            print("No contacts found!")

    elif choice == "3":
        search = input("Enter Name to Search: ")

        if search in contacts:
            print("\nContact Found:")
            print("Name:", search)
            print("Phone:", contacts[search]["Phone"])
            print("Email:", contacts[search]["Email"])
            print("Address:", contacts[search]["Address"])
        else:
            print("Contact Not Found!")

    elif choice == "4":
        name = input("Enter Contact Name to Update: ")

        if name in contacts:
            contacts[name]["Phone"] = input("New Phone: ")
            contacts[name]["Email"] = input("New Email: ")
            contacts[name]["Address"] = input("New Address: ")
            print("Contact Updated Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "5":
        name = input("Enter Contact Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")