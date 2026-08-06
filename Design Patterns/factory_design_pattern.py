 from abc import ABC, abstractmethod

class NotificationType(ABC):
    @abstractmethod
    def send_notification(self,content):
        pass

class EmailNotification(NotificationType):
    def send_notification(self, content):
        print("Email has been send with the content: ",content)

class WhatsappNotification(NotificationType):
    def send_notification(self, content):
        print("Notification has been send wit content:",content)

class NotificationFactory():
    # def __init__(self) -> None:
    #     self.notificationproviders=[]
    # def add_type(self,type:str):
    #     self.notificationproviders.append(type)
    def provide_notofication_object(self,type:str|None)->NotificationType|None:
        if type=='email':
            return EmailNotification()
        elif type=='whatsapp':
            return WhatsappNotification()
        else:
            raise ValueError("Service is not registered")

class NotificationService():
    def send_notification(self,factory:NotificationFactory,type:str|None,message:str):
        try:
            notification_obj=factory.provide_notofication_object(type)
            # if notification_obj:
            notification_obj.send_notification(message)
            # else:
            #     print("Notification cannot be send as service is not registered.")
        except Exception as ex:
            print("some error:",ex)
factory=NotificationFactory()
email=EmailNotification()
whatsapp=WhatsappNotification()
# factory.add_type("email")
# factory.add_type("whatsapp")
ns=NotificationService()
ns.send_notification(factory,"email","what is up")
ns.send_notification(factory,"whatsapp","this is message for mobile")
ns.send_notification(factory,"dafsf","fasdf")