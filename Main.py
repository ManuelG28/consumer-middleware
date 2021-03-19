from Consumer import Consumer

print("----------------Welcome to Consumer APP----------------")
print("You can select one of these options:")

def home():
    while (True):

        print("1. Login\n2. Sign in\n3. Exit")
        print("-------------------------------------------------------")
        option = input()

        if option == '1':
            email = input("Please insert your e-mail: ")
            password = input("Please insert your password: ")
            consumer = Consumer(email, password)
            consumer.login()
            print(consumer.get_access_token())
        elif option == "2":
            email = input("Please insert your e-mail: ")
            password = input("Please insert your password: ")
            name = input("Please insert your name: ")
            consumer = Consumer(email, password, name)
            print(consumer.sign_in())
        elif option == "3":
            print("Kind Regards!")
            break
        else:
            print("Please insert a valid option.")

home()