class User:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    def get_name(self):
        print("the name of the user is:",self.name)
    def get_age(self):
        print("the age of the user is ",self.age)

vivek=User("vivek",11,"test@gmail.comd")
# print("hello ther")
vivek.get_age()
vivek.get_name()