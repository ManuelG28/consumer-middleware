from Consumer import Consumer


def home():

    print("----------------Welcome to Consumer APP----------------")
    print("You can select one of these options:")

    while (True):

        print("1. Login\n2. Sign in\n3. Exit")
        print("-------------------------------------------------------")
        option = input()

        if option == '1':
            email = input("Please insert your e-mail: ")
            password = input("Please insert your password: ")
            consumer = Consumer(email, password)
            consumer.login()
            consumer.update_user_info()
            crud_queue(consumer)

        elif option == "2":
            email = input("Please insert your e-mail: ")
            password = input("Please insert your password: ")
            name = input("Please insert your name: ")
            consumer = Consumer(email, password, name)
            consumer.sign_in()

        elif option == "3":
            print("Kind Regards!")
            break

        else:
            print("Please insert a valid option.")


def crud_queue(consumer):

    while(True):

        print("----------------Welcome",
              consumer.get_name(), "-----------------")
        print("1. List of queues \n2. Get messages in a queue \n3. Exit")
        print("-------------------------------------------------------")
        option = input()

        if option == '1':
            consumer.get_queues()

        elif option == '2':
            queue_name = input("Please enter the queue name where you want to get all the of messages: ")
            consumer.get_message(queue_name)

        elif option == "3":
            print("Kind Regards!")
            break

        else:
            print("Please insert a valid option.")

home()
