from spy_details import spy, Spy, ChatMessage, friends
from termcolor import colored
from steganography.steganography import Steganography

STATUS_MESSAGES = ['My name is Kumar, Abhishek Kumar', 'Seen, whole completed.', 'Working on secret task , Sir']
#describing the details
print "Hello! Let\'s get started the new application","orange"
#Giving detais about spy
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)
def add_status():
    #updating the status
    updated_status_message = None
    if spy.current_status_message != None:
        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        #Printing that you don't have any status message
        print 'You don\'t have any status message currently \n'
    default = raw_input("Do you want to select from the older status (y/n)? ")
    if default.upper() == "N":
        #New updating status
        new_status_message = raw_input("What status message do you want to set? ")
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            #updating the new status message
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1
#Read the status message
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1
#selection of message
        message_selection = int(raw_input("\nChoose from the above messages "))


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'
#update status message
    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'
#Return update message
    return updated_status_message


def add_friend():
#details of new friend
    new_friend = Spy('','',0,0.0)
#new friend name
    new_friend.name = raw_input("Please add your friend's name: ")
    #new friend saluation
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
#new friend name
    new_friend.name = new_friend.salutation + " " + new_friend.name
#new friend age
    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)
#new friend rating
    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)

def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1
#choice of friend
    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1
#returm friend choice
    return friend_choice_position

#sending the message
def send_message():

    friend_choice = select_a_friend()
#providing the image deatails
    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)
#describing the new chat message
    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)
#printingthe scret messgage
    print "Your secret message image is ready!"

#reading  the message
def read_message():

    sender = select_a_friend()
#outputing the path
    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"

#reading the chat history
def read_chat_history():

    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name

#spying the age
    if spy.age > 12 and spy.age < 50:

#authentication completing
        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True
#whole of the
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)
#choice of the menu
                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'

if existing == "Y":
    start_chat(spy)
else:
#spying the chats
    spy = Spy('','',0,0.0)
#name of the spy
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")
#age of the spy
        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)
#rating of the spy
        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)
#start chatting the boy
        start_chat(spy)
    else:
        #adding the valid spy name
        print 'Please add a valid spy name'

