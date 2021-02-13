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

def insert(name, age, contact, i):
    record_dictionary[i] = {}
    record_dictionary[i]['Name'] = name.title()
    record_dictionary[i]['Age'] = age
    record_dictionary[i]['Contact'] = contact

def update(name, status):
    flag = 0
    if status == '1':
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
    elif status == '2':
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
    elif status == '3':
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

def deleteData(name):
    flag = 0
    record_dictionary1 = record_dictionary.copy()
    for s_id,s_info in record_dictionary1.items():
        for key,value in s_info.items():
            if value == name:
                flag = 1
                del(record_dictionary[s_id])
                print("Record deleted")
                break
    if flag == 0:
        print("No Record Found!!!")

def retrieve(name):
    flag = 0
    for s_id,s_info in record_dictionary.items():
        for key,value in s_info.items():
            if value == name:
                flag = 1
                print(record_dictionary[s_id])
                break
    if flag == 0: 
        print("No Record Found!!!")

def retrieveAll():
    for s_id, s_info in record_dictionary.items():
        print("\nStudent ID: ",s_id)
        for key,value in s_info.items():
            print(key + ':',value)
        
def main():
    while True:
        cmd_input = input("\n0.Exit 1.Insert 2.Update 3.Delete 4.Retrieve All 5.Enter Name to find data\nEnter a command: ")
        if cmd_input == '0':
            break
        if cmd_input == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            contact = int(input("Enter Contact Number: "))
            i = len(record_dictionary) + 1
            insert(name, age, contact, i)
        if cmd_input == '2':
            name = input("Enter Name to update: ").title()
            status = input("Enter to update \t1.Name\t2. Age\t3.Contact\n")
            update(name, status)
        if cmd_input == '3':
            name = input("Enter Name to delete: ").title()
            deleteData(name)
        if cmd_input == '4':
            retrieveAll()
        if cmd_input == '5':
            name = input("Enter Name: ").title()
            retrieve(name)
        else:
            print("Invalid Input!!!")

if __name__ == '__main__':
    main()