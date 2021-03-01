class Student:
    name = None
    age = None
    contact = None

    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_contact(self):
        return self.contact
