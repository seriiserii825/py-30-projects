import os
import requests

class DownloadImage:
    def __init__(self):
        self.image_name = ""
        self.url = ""
        self.file_path = ""
        self.extension = ""
        self.extenstion_list = [".jpg", ".jpeg", ".png", ".gif"]
        self.init()

    def getExtensionFromUrl(self):
        for ext in self.extenstion_list:
            if ext in self.url:
                return ext
        return None
        
    def init(self):
        self.url = input("Enter the URL of the image: ")
        if self.url == "":
            print("URL cannot be empty")
            return
        self.image_name = input("Enter the name of the image without extension: ")
        if self.image_name == "":
            print("Image name cannot be empty")
            return
        self.extension = self.getExtensionFromUrl()
        if self.extension is None:
            raise Exception("Invalid URL: No valid image extension found")

        folder = input("Enter folder to save the image: ")
        if folder == "":
            self.file_path = f"{self.image_name}{self.extension}"
        else:
            self.file_path = f"{folder}/{self.image_name}{self.extension}"
            if not os.path.exists(folder):
                os.makedirs(folder)

        if os.path.exists(self.file_path):
            raise Exception(f"File already exists: {self.file_path}")

    def download(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                with open(self.file_path, 'wb') as file:
                    file.write(response.content)
                print(f"Image downloaded successfully: {self.file_path}")
            else:
                print(f"Failed to download image. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")
