from classes.WebsitesStatus import WebsitesStatus


def checkWebsitesStatus():
    wb = WebsitesStatus()
    websites: list[str] = wb.getWebsites()
    for website in websites:
        wb.checkWebsite(website, wb.user_agent)
