from bs4 import BeautifulSoup
import requests

class FashionWebScrapper1:
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
            if idx > 5:
                break
            #clean the heading data
            headingData.append(heading.next_sibling.text)
            description = ""
            tempValue = heading
            while tempValue.next_sibling and tempValue.next_sibling.name != 'h2':
                description+='\n'+str(tempValue.next_sibling)
                tempValue = tempValue.next_sibling
            contentData.append(description)

        processeddata["heading"] = headingData
        processeddata["content"] = contentData
        return processeddata