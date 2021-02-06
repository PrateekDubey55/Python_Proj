record_dictionary = {
    1: {
        'Name': 'Prateek',
        'Age': 21,
        'Contact': 1234568970
    },
    2: {
        'Name': 'Shyam',
        'Age': 22,
        'Contact': 6549873210
    },
    3: {
        'Name': 'Madhur',
        'Age': 21,
        'Contact': 4567891230
    }
}
while True:
    cmd_input = eval(input("\n1. Insert \t2. Update \t3. Delete \t4. Retrieve All \t5. Enter Name to find data\nEnter a command: "))
    if cmd_input == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        contact = int(input("Enter Contact Number: "))
        i = len(record_dictionary) + 1
        record_dictionary[i] = {}
        record_dictionary[i]['Name'] = name.title()
        record_dictionary[i]['Age'] = age
        record_dictionary[i]['Contact'] = contact
        i = int(input("Press 0 to exit or any other key to conitnue\n"))
        if(i == 0) : break
    elif cmd_input == 2:
        flag = 0
        name = input("Enter Name to update: ").title()
        status = input("Enter to update \t1. Name \t2. Age \t3. Contact\n")
        if status == 1:
            new_Name = input("Enter New Name: ")
            for s_id,s_info in record_dictionary.items():
                for key,value in s_info.items():
                    if value == name:
                        flag = 1
                        record_dictionary[s_id]['Name'] = new_Name
                        print("Record Updated")
                        break
            if flag == 0:
                print("No Record Found!!!")
        elif status == 2:
            new_Age = input("Enter New Age: ")
            for s_id,s_info in record_dictionary.items():
                for key,value in s_info.items():
                    if value == name:
                        flag = 1
                        record_dictionary[s_id]['Age'] = new_Age
                        print("Record Updated")
                        break
            if flag == 0:
                print("No Record Found!!!")
        elif status == 3:
            new_Contact = input("Enter New Contact: ")
            for s_id,s_info in record_dictionary.items():
                for key,value in s_info.items():
                    if value == name:
                        flag = 1
                        record_dictionary[s_id]['Contact'] = new_Contact
                        print("Record Updated")
                        break
            if flag == 0:
                print("No Record Found!!!")
        else: 
            print("WRONG INPUT!!!")
            break
        i = int(input("Press 0 to exit or any other key to conitnue\n"))
        if(i == 0) : break
    elif cmd_input == 3:
        flag = 0
        name = input("Enter Name to delete: ").title()
        for s_id,s_info in record_dictionary.items():
            for key,value in s_info.items():
                if value == name:
                    flag = 1
                    del(record_dictionary[s_id])
                    print("Record deleted")
                    break
        if flag == 0:
            print("No Record Found!!!")
        i = int(input("Press 0 to exit or any other key to conitnue\n"))
        if(i == 0) : break
    elif cmd_input == 4:
        for s_id, s_info in record_dictionary.items():
            print("\nStudent ID: ",s_id)
            for key,value in s_info.items():
                print(key + ':',value)
        i = int(input("Press 0 to exit or any other key to conitnue\n"))
        if(i == 0) : break
    elif cmd_input == 5:
        flag = 0
        name = input("Enter Name: ").title()
        for s_id,s_info in record_dictionary.items():
            for key,value in s_info.items():
                if value == name:
                    flag = 1
                    print(record_dictionary[s_id])
                    break
        if flag == 0: 
            print("No Record Found!!!")
        i = int(input("Press 0 to exit or any other key to conitnue\n"))
        if(i == 0) : break
    else:
        print("Invalid Input!")
        i = int(input("Press 0 to exit or any other key to conitnue\n"))
        if(i == 0) : break