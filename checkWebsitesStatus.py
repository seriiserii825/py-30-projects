from classes.WebsitesStatus import WebsitesStatus


def checkWebsitesStatus():
    wb = WebsitesStatus()
    websites = wb.getWebsites()
    print(f"websites: {websites}")
