import configparser

config=configparser.RawConfigParser()  #
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod                   #static method can be accessed using class name without using object
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password