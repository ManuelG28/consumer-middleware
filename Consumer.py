import requests

class Consumer:
    def __init__(self, email, password, name=''):
        self.__email = email
        self.__name = ''
        self.__password = password
        self.__ip = ''
        self.__access_token = ''
        self.__port = 0

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_ip(self):
        return self.__access_token

    def set_ip(self, ip):
        self.__ip = ip

    def get_access_token(self):
        return self.__access_token

    def set_acces_token(self, token):
        self.__access_token = token

    def get_port(self):
        return self.__port

    def set_ip(self, port):
        self.__port = port

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def sign_in(self):
        response = requests.post("http://54.164.144.28/api/register", {
            'email': self.get_email(),
            'password': self.get_password(),
            'name': self.get_email()
        }).json()

        if 'message' in response:
            for error in response['errors']:
                print(error)

        else:
            return response

    def login(self):
        response = requests.post("http://54.164.144.28/api/login", {
            'email': self.get_email(),
            'password': self.get_password(),
        }).json()

        if 'message' in response:
            return response["message"]

        else:
            self.set_acces_token(response["access_token"])
            return response

    def update_user_info(self):
        head = {'Authorization': 'Bearer ' + self.get_access_token()}
        response = requests.get("http://54.164.144.28/api/user-info",headers = head).json()
        self.set_name(response["name"])
    
    def get_message(self,queue_name):
        head = {'Authorization': 'Bearer ' + self.get_access_token()}
        params = {"queue":queue_name}
        response = requests.get("http://54.164.144.28/api/queue/pull", params = params, headers = head).json()

        if "errors" in response:
            print(response["errors"])

        elif not response["messages"]:
            print("This queue <",queue_name,"> has not messages yet",'\n')
        else:
            message = response["messages"]
            print("Message: ", message[0]["body"])
            print("Date sent: ", message[0]["date"])
    
    def get_queues(self):
        head = {'Authorization': 'Bearer ' + self.get_access_token()}
        response = requests.get("http://54.164.144.28/api/queue/list", headers = head).json()
        if not response:
            print("This server has not queues yet")

        else:
            for queue in response[0]:
                print("Queue name:",queue["name"])
                print("Created at:",queue["created_at"],'\n')


