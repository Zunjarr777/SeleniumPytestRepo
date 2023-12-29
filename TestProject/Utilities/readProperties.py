import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getAppURL():
        url = config.get('common data', 'google_url')
        # url = config.get('common data', 'google_url')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common data', 'password')
        return password
