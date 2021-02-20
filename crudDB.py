#prior to import connector...
# install it on windows cmd by using the following command
# python -m pip install mysql-connector-python

#import connector
import mysql.connector

#create connection
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'pydata'
)

#create cursor object
myCursor = conn.cursor()

#to check whether connection is eastablished 
if conn:
    print('Connection Successful!!!')
else:
    print('Connection Failed...')

#to check the databases
# myCursor.execute('Show Databases')
# for x in myCursor:
#     print(x)

#to create database, one time process per database
#myCursor.execute('Create Database pyData')

#to create table, one time process per table
#myCursor.execute('Create Table studentdata (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age INT, contact VARCHAR(20))')

#to check table created or not
# myCursor.execute('Show Tables')
# for x in myCursor:
#     print(x)

#function for inserting data
def insertData():
    name = input('Enter Name: ').title()
    age = input('Enter Age: ')
    contact = input('Enter Contact: ')
    sqlQuery = 'Insert Into studentdata (name, age, contact) Values (%s,%s,%s)'
    values = (name, age, contact)
    myCursor.execute(sqlQuery, values)
    conn.commit()
    print(myCursor.rowcount, 'record(s) inserted')

#function to update data
def updateData():
    idN = input('Enter ID Number to Update: ')
    sql = 'Select * from studentdata where id = %s'
    myCursor.execute(sql,(idN,))
    result = myCursor.fetchall()
    if len(result) == 0:
        print('No Record Found!!!')
    else:
        print('\nWhat do you want to update?')
        ip = input('1.Name 2.Age 3.Contact \nPlease select any one: ')
        if ip == '1':
            name = input('Enter New Name: ').title()
            sql = 'Update studentdata Set name = %s where id = %s'
            val = (name, idN)
            myCursor.excute(sql,val)
            conn.commit()
            print(myCursor.rowcount, 'record(s) changed')
        elif ip == '2':
            age = input('Enter New Age: ')
            sql = 'Update studentdata set age = %s where id = %s'
            val = (age, idN)
            myCursor.execute(sql,val)
            conn.commit()
            print(myCursor.rowcount, 'record(s) changed')
        elif ip == '3':
            contact = input('Enter New Contact: ')
            sql = 'Update studentdata set contact = %s where id = %s'
            val = (contact, idN)
            myCursor.execute(sql,val)
            conn.commit()
            print(myCursor.rowcount, 'record(s) changed')

#function to delete data
def deleteData():
    idN = input('Enter ID Number to Delete: ')
    sql = 'Select * from studentdata where id = %s'
    myCursor.execute(sql,(idN,))
    result = myCursor.fetchall()
    if len(result) == 0:
        print('No Record Found!!!')
    else:
        sql = 'Delete from studentdata where id = %s'
        myCursor.execute(sql,(idN,))
        conn.commit()
        print(myCursor, 'record(s) deleted')

#function to read all the data
def retrieveAll():
    myCursor.execute('Select * from studentdata')
    result = myCursor.fetchall()
    for x in result:
        print(x)

#function to read selected data
def readSelected():
    name = input('Enter Name to Get Data: ').title()
    sql = 'Select * from studentdata where name = %s'
    myCursor.execute(sql,(name,))
    result = myCursor.fetchall()
    if len(result) == 0:
        print('No Record Found!!!')
    else:
        for x in result:
            print(x)

#main function 
def main():
    while True:
        cmd_input = input("\n0.Exit 1.Insert 2.Update 3.Delete 4.Retrieve All 5.Enter Name to find data\nEnter a command: ")
        if cmd_input == '0':
            conn.close()
            break
        elif cmd_input == '1':
            insertData()
        elif cmd_input == '2':
            updateData()
        elif cmd_input == '3':
            deleteData()
        elif cmd_input == '4':
            retrieveAll()
        elif cmd_input== '5':
            readSelected()
        else:
            print('Invalid Input...')

if __name__ == '__main__':
    main()