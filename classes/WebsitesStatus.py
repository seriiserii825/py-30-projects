import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus
class WebsitesStatus:
    def __init__(self):
        self.websites = []
        self.user_agent = self.getUserAgent()
        self.file_path = "data/websites.csv"
    def getWebsites(self):
        self.csvToArray()
        return self.websites
    def csvToArray(self):
        try:
            with open(self.file_path, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if 'https://' in row[0]:
                        self.websites.append(row[0])
                    else:
                        self.websites.append('https://' + row[0])
        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    def getUserAgent(self):
        user_agent = UserAgent()
        return user_agent.chrome
    def getStatusDescription(self, status_code: int):
        for value in HTTPStatus:
            if value == status_code:
                return f'({value} {value.name}) {value.description}'
        return f'(???) Unknown status code'

    def checkWebsite(self, website: str, user_agent):
        try:
            code: int = requests.get(website, headers={'User-Agent': user_agent}).status_code
            print(f"Website: {website} - Status code: {code} - Description: {self.getStatusDescription(code)}")
        except requests.exceptions.RequestException as e:
            print(f'Error checking {website}: {e}')
