from user import User

class UserRepository:
    def __init__(self,db,user,password):
        self.db=db
        self.user=user
        self.password=password

    def save_to_db(self,user:User):
        print(f"User:{user.name} has been saved to db:{self.db}")

    def delete_from_db(self,user:User):
        print(f"User:{user.name} with email {user.email} has been deleted")

print("hello there workd")