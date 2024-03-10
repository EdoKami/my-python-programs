from time import sleep

while True:
    print("Hello! You can register your information here.")
    sleep(1)
    print("\n"
          "1. Add\n"
          "2. Remove\n"
          "3. Search\n"
          "0. Exit")
    sleep(1)

    Option = int(input("Choose your option: "))

    if Option == 0:
        print("Exiting the program. Goodbye!")
        break

    elif Option == 1:
        User = input("User: ")
        while True:
            try:
                Age = int(input("Age: "))
                break
            except ValueError:
                print("Age must be a number!")
        Email = input("Email: ")
        password = input("Password: ")
        with open("Save.txt", 'a') as file:
            file.write(f"Name: {User}, Password: {password}, Age: {Age}, Email: {Email}\n")

    elif Option == 2:
        remove_user = input("User to remove: ")
        password_for_removal = input("Password: ")

        with open("Save.txt", "r") as file:
            lines = file.readlines()

        with open("Save.txt", "w") as file:
            found = False
            remove_criteria = f"Name: {remove_user}, Password: {password_for_removal}"
            for line in lines:
                if remove_criteria not in line:
                    file.write(line)
                else:
                    found = True

            if found:
                print("User removed successfully!")
            else:
                print("User not found or password incorrect.")

    elif Option == 3:
        search_name = input("Search name: ")
        Verify_Password = input("Password: ")

        with open("Save.txt", "r") as file:
            lines = file.readlines()

        found = False
        search_criteria = f"Name: {search_name}, Password: {Verify_Password}"
        for line in lines:
            if search_criteria in line:
                found = True
                print("Entry found!")
                print("Entry Details:", line)
                break

        if not found:
            print("Entry not found or password incorrect.")

    else:
        print("Wrong option!")
