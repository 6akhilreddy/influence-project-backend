from bs4 import BeautifulSoup
import requests

class InstagramWebScrapper5:
    def __init__(self) -> None:
        pass

    def getStrategy(self, url):
        processeddata = {}
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        allHeadings = soup.find_all("h3")
        headingData = []
        contentData = []
        for idx, heading in enumerate(allHeadings):
            if idx > 11:
                break
            description = heading.find_next_sibling("p")
            #clean the heading data
            headingArr = str(heading.b.text).split(' ')
            headingArr.pop(0)
            headingtxt = ' '.join(headingArr)
            headingData.append(headingtxt)
            contentData.append(str(description))

        processeddata["heading"] = headingData
        processeddata["content"] = contentData
        return processeddata