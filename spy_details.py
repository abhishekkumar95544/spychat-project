from datetime import datetime
#details of spy

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#chatmessage details
class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('kumar', 'Mr.', 24, 4.7)

friend_one = Spy('Rakesh', 'Mr.', 2.9, 28)
friend_two = Spy('sara jack', 'Ms.', 4.39, 21)
friend_three = Spy('No', 'Dr.', 4.95, 37)


friends = [friend_one, friend_two, friend_three]
