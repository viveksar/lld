from user import User
from userRepository import UserRepository

vivek=User("vivek",22,"afas")
abc=User("fasf",3543,"sdfasdf")

userrepo=UserRepository("test db","username","password")

userrepo.save_to_db(vivek)
userrepo.delete_from_db(abc)