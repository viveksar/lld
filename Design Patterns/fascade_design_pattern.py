class UserService:
    def login(self,username,password):
        print(f"login occured for {username} with {password}")

    def getdetails(self,user):
        print("Thise are the details of the",user)

class OrderService:
    def get_order(self,user):
        print("The user has 10 order pending")

class ApiGateway:
    def __init__(self,user,order) -> None:
        self.userService:UserService=user
        self.orderService:OrderService=order

    def login(self,username,password):
        self.userService.login(username,password)
    def get_details(self,user):
        self.userService.getdetails(user)
    def getOrder(self,user):
        self.orderService.get_order(user)
    def data(self):
        print("hello")

os=OrderService()
us=UserService()
ag=ApiGateway(us,os)
ag.data()
ag.login("test","abc")
ag.get_details("test")
ag.getOrder("test")