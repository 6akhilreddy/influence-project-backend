from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class InstagramWebScrapper4:
    def __init__(self) -> None:
        pass

    def getStrategy(self, url):
        processeddata = {}
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url,headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, "html.parser")
        allHeadings = soup.find_all(class_="ez-toc-section")
        headingData = []
        contentData = []
        for idx, heading in enumerate(allHeadings):
            if idx > 11:
                break
            description = ""
            tempValue = heading.parent.next_sibling.next_sibling
            while tempValue.next_sibling.name != 'h2':
                description+='\n'+str(tempValue.next_sibling)
                tempValue = tempValue.next_sibling
            #clean the heading data
            headingArr = heading.get('id').split('_')
            headingArr.pop(0)
            headingtxt = ' '.join(headingArr)
            headingData.append(headingtxt)
            contentData.append(str(description))
            
        processeddata["heading"] = headingData
        processeddata["content"] = contentData
        return processeddata