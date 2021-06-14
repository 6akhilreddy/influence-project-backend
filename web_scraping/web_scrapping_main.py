from bs4 import BeautifulSoup
import requests
import json
import textdistance as td

from web_scraping.mock import instagram_mock_strategies, social_media_mock_strategies, organic_growth_strategies, fashion_strategies, music_strategies, photography_strategies

from web_scraping.current_Instagram_trends.instagram_web_scrapper_1 import InstagramWebScrapper1
from web_scraping.current_Instagram_trends.instagram_web_scrapper_2 import InstagramWebScrapper2
from web_scraping.current_Instagram_trends.instagram_web_scrapper_3 import InstagramWebScrapper3
from web_scraping.current_Instagram_trends.instagram_web_scrapper_4 import InstagramWebScrapper4
from web_scraping.current_Instagram_trends.instagram_web_scrapper_5 import InstagramWebScrapper5

from web_scraping.social_media_marketing.social_media_web_scrapper_1 import SocialMediaWebScrapper1
from web_scraping.social_media_marketing.social_media_web_scrapper_2 import SocialMediaWebScrapper2
from web_scraping.social_media_marketing.social_media_web_scrapper_3 import SocialMediaWebScrapper3
from web_scraping.social_media_marketing.social_media_web_scrapping_4 import SocialMediaWebScrapper4

from web_scraping.organic_growth_strategies.organic_web_scrapper_1 import OrganicWebScrapper1
from web_scraping.organic_growth_strategies.organic_web_scrapper_2 import OrganicWebScrapper2
from web_scraping.organic_growth_strategies.organic_web_scrapper_3 import OrganicWebScrapper3
from web_scraping.organic_growth_strategies.organic_web_scrapping_4 import OrganicWebScrapper4

from web_scraping.fashion.fashion_web_scrapper_1 import FashionWebScrapper1

from web_scraping.music.music_web_scrapper_1 import MusicWebScrapper1

from web_scraping.photography.photo_web_scrapper_1 import PhotoWebScrapper1


class WebScrappingMain:
    def __init__(self) -> None:
        pass
   
    # get the top 5 search results from the google
    def __getTopPagesBasedOnSearch(self, search):
        results = 5
        page = requests.get(f"https://www.google.com/search?q={search}&num={results}")
        soup = BeautifulSoup(page.content, "html.parser")
        links = soup.findAll("a")
        urls = []
        for link in links :
            link_href = link.get('href')
            if "url?q=" in link_href and not "webcache" in link_href:
                urls.append(link.get('href').split("?q=")[1].split("&sa=U")[0])
        return urls

    # filter the strategies based on the similar words and max content
    def __filterStartegies(self, strategies):

        # get the headings
        headings = []

        for s in strategies:
            headings.append(s['heading'])

        for i, h in enumerate(headings):
            print('total headings present in website - ', i+1, ' before filtering = ', len(h))

        for i in range(len(headings)-1):
            for headIdx, heading in enumerate(headings[i]):
                for j in range(i+1, len(headings)):
                    for checkIdx, check in enumerate(headings[j]):
                        # apply machine learning algorithm to find the similarity
                        similarity_value = td.sorensen.normalized_similarity(heading,check)
                        if similarity_value > 0.8:
                            print('-'*100)
                            print([heading], [check], [similarity_value])

                            heading_content = strategies[i]['content'][headIdx]
                            check_content = strategies[j]['content'][checkIdx]

                            #find the content similarity
                            content_similarity_value = td.sorensen.normalized_similarity(heading_content,check_content)

                            print('content similarity - ', [content_similarity_value])

                            if content_similarity_value > 0.5:
                                strategies[i]['content'][headIdx] += strategies[j]['content'][checkIdx]

                                # remove the similar strategy
                                strategies[j]['heading'].pop(checkIdx)
                                strategies[j]['content'].pop(checkIdx)
                            else:
                                # check which is having more content and remove the other
                                if len(strategies[i]['content'][headIdx]) > len(strategies[j]['content'][checkIdx]) :
                                    strategies[j]['heading'].pop(checkIdx)
                                    strategies[j]['content'].pop(checkIdx)
                                else:
                                    strategies[i]['heading'].pop(headIdx)
                                    strategies[i]['content'].pop(headIdx)
    
        headings = []
        for s in strategies:
            headings.append(s['heading'])

        print('-'*100)

        for i, h in enumerate(headings):
            print('total headings present in website - ', i+1, ' after filtering = ', len(h))


        print('-'*100)
        return strategies
    
    def __mergeStrategies(self, strategies):
        mergedStrategies = []

        for strategy in strategies:
            for heading, content in zip(strategy['heading'], strategy['content']):
                merge_heading_content = {'heading':heading, 'content':content}
                mergedStrategies.append(merge_heading_content)
        
        return mergedStrategies


    # get strategies specific to instagram
    def __getInstagramStrategies(self, keyword):
        # urls = self.__getTopPagesBasedOnSearch(keyword)

        if len(instagram_mock_strategies) == 0:

            strategies = []

            strategy1 = InstagramWebScrapper1()
            strategy2 = InstagramWebScrapper2()
            strategy3 = InstagramWebScrapper3()
            strategy4 = InstagramWebScrapper4()
            strategy5 = InstagramWebScrapper5()

            strategies.append(strategy1.getStrategy("https://www.cyberclick.net/numericalblogen/10-exciting-instagram-trends-to-keep-track-of"))
            strategies.append(strategy2.getStrategy("https://sproutsocial.com/insights/instagram-trends/"))
            strategies.append(strategy3.getStrategy("https://influencermarketinghub.com/instagram-marketing-trends-2021/"))
            strategies.append(strategy4.getStrategy("https://blog.kicksta.co/instagram-trends"))
            strategies.append(strategy5.getStrategy("https://blog.hootsuite.com/instagram-trends"))

            filtered_data = self.__filterStartegies(strategies)
            merged_data = self.__mergeStrategies(filtered_data)

            instagram_mock_strategies.extend(merged_data)
        

        return json.dumps(instagram_mock_strategies)
    
    def __getSocialMediaStrategies(self, keyword):
        # urls = self.__getTopPagesBasedOnSearch(keyword)
        if len(social_media_mock_strategies) == 0:

            strategies = []

            strategy1 = SocialMediaWebScrapper1()
            strategy2 = SocialMediaWebScrapper2()
            strategy3 = SocialMediaWebScrapper3()
            strategy4 = SocialMediaWebScrapper4()

            strategies.append(strategy1.getStrategy("https://www.entrepreneur.com/article/293321"))
            strategies.append(strategy2.getStrategy("https://buffer.com/library/social-media-marketing-strategy"))
            strategies.append(strategy3.getStrategy("https://sproutsocial.com/insights/social-media-marketing-strategy"))
            strategies.append(strategy4.getStrategy("https://influencermarketinghub.com/social-media-marketing-strategy/"))

            filtered_data = self.__filterStartegies(strategies)
            merged_data = self.__mergeStrategies(filtered_data)

            social_media_mock_strategies.extend(merged_data)

        return json.dumps(social_media_mock_strategies)
    
    def __getOrganicGrowthStrategies(self, keyword):
        # urls = self.__getTopPagesBasedOnSearch(keyword)
        if len(organic_growth_strategies) == 0:

            strategies = []
            strategy1 = OrganicWebScrapper1()
            strategy2 = OrganicWebScrapper2()
            strategy3 = OrganicWebScrapper3()
            strategy4 = OrganicWebScrapper4()

            strategies.append(strategy1.getStrategy("https://corporatefinanceinstitute.com/resources/knowledge/strategy/organic-growth"))
            strategies.append(strategy2.getStrategy("https://hingemarketing.com/blog/story/how-to-drive-organic-growth-5-proven-strategies-for-professional-services-firms"))
            strategies.append(strategy3.getStrategy("https://www.moengage.com/blog/how-to-build-a-growth-team"))
            strategies.append(strategy4.getStrategy("https://www.prophet.com/2013/12/10-quick-ways-to-drive-organic-growth"))

            filtered_data = self.__filterStartegies(strategies)
            merged_data = self.__mergeStrategies(filtered_data)

            organic_growth_strategies.extend(merged_data)


        return json.dumps(organic_growth_strategies)
    
    def __getFashionStrategies(self, keyword):
        # urls = self.__getTopPagesBasedOnSearch(keyword)
        if len(fashion_strategies) == 0:

            strategies = []
            strategy1 = FashionWebScrapper1()

            strategies.append(strategy1.getStrategy("https://shanebarker.com/blog/fashion-influencer-marketing"))

            filtered_data = self.__filterStartegies(strategies)
            merged_data = self.__mergeStrategies(filtered_data)

            fashion_strategies.extend(merged_data)


        return json.dumps(fashion_strategies)
    
    def __getMusicStrategies(self, keyword):
        # urls = self.__getTopPagesBasedOnSearch(keyword)
        if len(music_strategies) == 0:

            strategies = []
            strategy1 = MusicWebScrapper1()

            strategies.append(strategy1.getStrategy("https://www.ucraft.com/blog/7-tips-for-promoting-your-music-on-instagram"))

            filtered_data = self.__filterStartegies(strategies)
            merged_data = self.__mergeStrategies(filtered_data)

            music_strategies.extend(merged_data)


        return json.dumps(music_strategies)
    
    def  __getPhotoStrategies(self, keyword):
        # urls = self.__getTopPagesBasedOnSearch(keyword)
        if len(photography_strategies) == 0:

            strategies = []
            strategy1 = PhotoWebScrapper1()

            strategies.append(strategy1.getStrategy("https://justagirlandherblog.com/interior-photography-tips-for-bloggers"))

            filtered_data = self.__filterStartegies(strategies)
            merged_data = self.__mergeStrategies(filtered_data)

            photography_strategies.extend(merged_data)


        return json.dumps(photography_strategies)



        
    def getSearchedData(self, keyword):
        if "Instagram".upper() in keyword.upper() and "trends".upper() in keyword.upper():
            return self.__getInstagramStrategies(keyword)
        elif "Social".upper() in keyword.upper() and "Media".upper() in keyword.upper():
            return self.__getSocialMediaStrategies(keyword)
        elif "Organic".upper() in keyword.upper() and "growth".upper() in keyword.upper():
            return self.__getOrganicGrowthStrategies(keyword)
        elif "fashion".upper() in keyword.upper():
            return self.__getFashionStrategies(keyword)
        elif "music".upper() in keyword.upper():
            return self.__getMusicStrategies(keyword)
        elif "photography".upper() in keyword.upper():
            return self.__getPhotoStrategies(keyword)