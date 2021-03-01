#import connector
import mysql.connector

from student import Student

class StudentDB:
    config = {
        'host': None,
        'user': None,
        'password': None,
        'database': None,
        'raise_on_warnings': False
    }

    Table_Name = 'studentdata'
    connection = None

    def __init__(self, host, user, password, database):
        self.config["host"] = host
        self.config["user"] = user
        self.config["password"] = password
        self.config["database"] = database

    def connect_db(self):
        self.connection = mysql.connector.connect(**self.config, buffered=True)
        if(self.connection):
            print('Connection Successful!!!')
        else:
            print('Connection Failed...')
    
    def disconnect_db(self):
        self.connection.close()

    def insertData(self, student):
        try:
            cursor = self.connection.cursor()
            sqlQuery = f'''Insert Into {self.Table_Name} (name, age, contact)
            Values ("{student.get_name()}",
            "{student.get_age()}",
            "{student.get_contact()}")'''
            cursor.execute(sqlQuery)
            self.connection.commit()

        except mysql.connector.Error as e:
            if("Duplicate" in str(e)):
                print(f'Roll no: {student.get_roll_no()}  already exists')
            else:
                print(f'error  :  {e}')

        finally:
            cursor.close()
        
    def readSelected(self, rno):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = f'''Select * from {self.Table_Name} WHERE id = "{rno}"'''
            cursor.execute(sql)
            row = cursor.fetchone()
            if(row != None):
                return row
            else:
                return None
        
        except mysql.connector.Error as e:
            print(f'error  :  {e}')
            return None

        finally:
            cursor.close()

    def retrieveAll(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = f'''Select * from {self.Table_Name}'''
            cursor.execute(sql)
            result = cursor.fetchall()
            if(len(result)):
                for x in result:
                    print(x)
            else:
                print("No students in database")
        
        except mysql.connector.Error as e:
            print(f'Error Message : {e}')
        
        finally:
            cursor.close()

    def deleteData(self, rno):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = f'''Delete from {self.Table_Name} where id = "{rno}"'''
            cursor.execute(sql)
            if(cursor.rowcount):
                self.connection.commit()
                print(f'Student with roll number {rno} is deleted')
                return True
            else:
                print(f'Student with roll number {rno} does not exist')
                return False

        except mysql.connector.Error as e:
            print(f'Error message  :  {e}')
            return False

        finally:
            cursor.close()

    def updateData(self, rno, student):
        try:
            cursor = self.connection.cursor(dictionary=True)
            sql = f'''Update {self.Table_Name} set 
            name = "{student.get_name()}",
            age = "{student.get_age()}",
            contact = "{student.get_contact()}" where id = {rno}'''
            cursor.execute(sql)
            self.connection.commit()
            if(cursor.rowcount):
                return True
            else:
                return False
        
        except mysql.connector.Error as e:
            print(f'Error Message  :  {e}')
            return False
        
        finally:
            cursor.close()
