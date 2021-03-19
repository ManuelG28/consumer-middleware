import requests

class Consumer:
    def __init__(self, email, password):
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
        response = requests.post("http://127.0.0.1:8000/api/register", {
            'email': self.get_email(),
            'password': self.get_password(),
            'name': self.get_email()
        }).json()

        return response

    def login(self):
        response = requests.post("http://127.0.0.1:8000/api/login", {
            'email': self.get_email(),
            'password': self.get_password(),
        }).json()
        
        self.set_acces_token(response["access_token"])
        return response
    
