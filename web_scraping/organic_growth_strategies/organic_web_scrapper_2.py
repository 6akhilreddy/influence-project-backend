from bs4 import BeautifulSoup
import requests

class OrganicWebScrapper2:
    def __init__(self) -> None:
        pass

    def getStrategy(self, url):
        processeddata = {}
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        p_elements = soup.find_all('p')

        p_strong_elements = []

        for element in p_elements:
            if element.find('strong') is not None:
                if not 'Figure' in element.text:
                    p_strong_elements.append(element)
        headingData = []
        contentData = []
        for idx, heading in enumerate(p_strong_elements):
            description = heading.next_sibling
            if idx > 14:
                break
            #clean the heading data
            headingData.append(heading.text)
            description = ""
            tempValue = heading
            count =0
            while tempValue.next_sibling and count < 10:
                description+='\n'+str(tempValue.next_sibling)
                tempValue = tempValue.next_sibling
                count+=1
            contentData.append(description)

        processeddata["heading"] = headingData
        processeddata["content"] = contentData
        return processeddata