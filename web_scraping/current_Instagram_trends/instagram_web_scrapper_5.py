from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class InstagramWebScrapper5:
    def __init__(self) -> None:
        pass

    def getStrategy(self, url):
        processeddata = {}
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url,headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, "html.parser")
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