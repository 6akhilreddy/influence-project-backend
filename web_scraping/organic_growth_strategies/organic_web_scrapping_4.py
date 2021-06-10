from bs4 import BeautifulSoup
import requests

class OrganicWebScrapper4:
    def __init__(self) -> None:
        pass

    def getStrategy(self, url):
        processeddata = {}
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        allHeadings = soup.find_all('h2')
        headingData = []
        contentData = []
        for idx, heading in enumerate(allHeadings):
            description = heading.next_sibling
            if idx > 1:
                #clean the heading data
                headingArr = heading.text.split(' ')
                headingArr.pop(0)
                headingtxt = ' '.join(headingArr)
                headingData.append(headingtxt)
                contentData.append(str(description))

        processeddata["heading"] = headingData
        processeddata["content"] = contentData
        return processeddata