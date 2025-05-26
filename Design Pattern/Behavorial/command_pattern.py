from abc import ABC, abstractmethod

class BaseCommand(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError("Please implement in subclass")

class EmailCommand(BaseCommand):
    def __init__(self, receiver, data):
        self.receiver = receiver
        self.data = data
    
    def execute(self):
        self.receiver.send_email(self.data)

class SMSCommand(BaseCommand):
    def __init__(self, receiver, data):
        self.receiver = receiver
        self.data = data
    
    def execute(self):
        self.receiver.send_sms(self.data)

class NotificationsService(object):
    def send_email(self, data):
        print("Sending email ", data)
    
    def send_sms(self, data):
        print("Sending SMS ", data)

class NotificationInvoker(object):
    def __init__(self):
        self.notification_history = []
    
    def invoke(self, command):
        self.notification_history.append(command)
        command.execute()

if __name__ == "__main__":
    invoker = NotificationInvoker()
    receiver = NotificationsService()

    email_command = EmailCommand(receiver, {"subject": "Test Email"})
    sms_command = SMSCommand(receiver, {"subject": "Test SMS"})

    invoker.invoke(email_command)
    invoker.invoke(sms_command)

    print(invoker.notification_history)
