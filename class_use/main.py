from student import Student

from db_handler import StudentDB

database = StudentDB(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'pydata')

database.connect_db()

def main():
    while True:
        cmd_input = input("\n0.Exit 1.Insert 2.Update 3.Delete 4.Retrieve All 5.Retrieve Selected\nEnter a command: ")
        if cmd_input == '0':
            database.disconnect_db()
            exit(0)
        elif cmd_input == '1':
            name = input('Enter Name: ').title()
            age = input('Enter Age: ')
            contact = input('Enter Contact: ')
            student = Student(name, age, contact)
            database.insertData(student)
        elif cmd_input == '2':
            rno = input("Enter Roll Number to Update: ")
            result = database.readSelected(rno)
            if(result != None):
                new_name = input("Enter New Name (if applicable): ")
                new_age = input("Enter New Age (if applicable): ")
                new_contact = input("Enter New Contact (if applicable): ")
                student = Student(new_name, new_age, new_contact)
            else:
                print(f'No Record Found for roll number {rno}')
                continue
            if(database.updateData(rno, student)):
                print("Information Updated Successfully!!!")
            else:
                print("Update Failed...")
        elif cmd_input == '3':
            rno = input("Enter Roll Number to Delete: ")
            database.deleteData(rno)
        elif cmd_input == '4':
            database.retrieveAll()
        elif cmd_input== '5':
            rno = input("Enter Roll Number to Search: ")
            result = database.readSelected(rno)
            if(result != None):
                for x in result:
                    print(x)
            else:
                print(f'No Record Found for this {rno}')
        else:
            print('Invalid Input...')

main()