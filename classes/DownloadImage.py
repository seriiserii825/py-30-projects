class DownloadImage:
    def __init__(self):
        self.image_name = ""
        self.file_path = ""
        self.extension = ""
        self.extenstion_list = [".jpg", ".jpeg", ".png", ".gif"]
        self.init()

    def getExtensionFromUrl(self, url):
        for ext in self.extenstion_list:
            if ext in url:
                return ext
        return None
        
    def init(self):
        url = input("Enter the URL of the image: ")
        if url == "":
            print("URL cannot be empty")
            return
        self.image_name = input("Enter the name of the image without extension: ")
        if self.image_name == "":
            print("Image name cannot be empty")
            return
        self.extension = self.getExtensionFromUrl(url)
        folder = input("Enter folder to save the image: ")
        if folder == "":
            self.file_path = f"{self.image_name}{self.extension}"
        else:
            self.file_path = f"{folder}/{self.image_name}{self.extension}"

