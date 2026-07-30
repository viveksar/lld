from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    def __init__(self) -> None:
        pass
    def send(self,message):
        pass

class EmailService(NotificationChannel):

    def send(self, message):
        print("Email service called and message send:",message)

class SmsService(NotificationChannel):
    def send(self,message):
        print("SMS serice called and message send:",message)

class NotificationService:
    def __init__(self,channel:NotificationChannel) -> None:
        self.channel=channel
    def send_notification(self,message):
        self.channel.send(message)

email=EmailService()
sms=SmsService()
email_service=NotificationService(email)
sms_service=NotificationService(sms)
# notification_service=NotificationService()
email_service.send_notification("You have been send a email")
sms_service.send_notification("Sms has been send to tyou")