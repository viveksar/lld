from abc import abstractmethod,ABC
class NotificationService(ABC):
    def send(self,to,body,subject):
        pass

class EmailNotification(NotificationService):
    def send(self,to,body,subject):
        print(f"sendding email {to} with subject:{subject} and body is {body}")

class SendgridNotification:
    def send_email(self,to,body,subject):
        print("this is the send grid notification email")
        print(f"sendding email from send grid {to} with subject:{subject} and body is {body}")

class SendGridAdaptor(NotificationService):
    def __init__(self,sendGrid:SendgridNotification) -> None:
        self.sendGrid=sendGrid
    def send(self, to, body, subject):
        self.sendGrid.send_email(to,body,subject)

class Payment:
    def __init__(self,notificationservice:NotificationService) -> None:
        self.notification_service=notificationservice
    def place_order(self,to,body,subject):
        print("order placed now sending notification")
        self.notification_service.send(to,body,subject)

email=EmailNotification()
payment=Payment(email)
payment.place_order("test@gmail.com","body of email","subject of email")
sendgrid=SendgridNotification()
sendgridadaptor=SendGridAdaptor(sendgrid)
payment_new=Payment(sendgridadaptor)
payment_new.place_order("testnew@gmail.com","new body of email","new subject of email")