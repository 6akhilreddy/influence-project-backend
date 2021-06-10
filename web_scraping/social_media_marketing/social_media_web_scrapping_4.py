from bs4 import BeautifulSoup
import requests

class SocialMediaWebScrapper4:
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
            if idx > 19:
                break
            #clean the heading data
            encodedTxt = (heading.text.encode('ascii', 'ignore')).decode("utf-8")
            headingArr = encodedTxt.split('.')
            headingArr.pop(0)
            headingtxt = ' '.join(headingArr)
            headingData.append(headingtxt)
            description = ""
            tempValue = heading
            while tempValue.next_sibling and tempValue.next_sibling.name != 'h2':
                description+='\n'+str(tempValue.next_sibling)
                tempValue = tempValue.next_sibling
            contentData.append(description)

        processeddata["heading"] = headingData
        processeddata["content"] = contentData
        return processeddata