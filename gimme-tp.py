# ------------------------------------------------------------------------------------------
# (C) 2020 Leeds Beckett Computer Science Society
# Authors:
# Bence Gadanyi
# Lucy McCall
# Samuel Lightowler
#
# server link: https://discord.gg/RDmKHe
#
# Descr: Web spider to search and alert available TP
#
#
# git: https://github.com/leeds-beckett-computer-science-society/toilet-paper-scraper.git
#
# ------------------------------------------------------------------------------------------

# shopping url:
# sainsburys: https://www.sainsburys.co.uk/webapp/wcs/stores/servlet/SearchDisplayView?catalogId=10241&storeId=10151&langId=44&krypto=0C8McsT1KrghpA75m2lcC2nPu3idj4G232wi0cOJQamGyXbwko%2Fj%2BCANLyQ4J%2Bqw2p8JFZYtb9Hf%2FmvEYreM%2BsWsfqe71saPpXK4whY%2BU5tdU0eHKhWtKS%2FEsSe%2BTGZicqBJr6nKLPKJHYbDqJGesKig68RoqTuj0ojzIWpIbY3KXyJoRQxmQvV2lUyWK%2FN9#langId=44&storeId=10151&catalogId=10241&categoryId=&parent_category_rn=&top_category=&pageSize=60&orderBy=RELEVANCE&searchTerm=toilet%20roll&beginIndex=0&hideFilters=true&categoryFacetId1=
# tesco: https://www.tesco.com/groceries/en-GB/search?query=toilet%20paper&icid=tescohp_sws-1_m-ft_in-toilet%20paper_ab-226-b_out-toilet%20paper
# wilko: https://www.wilko.com/en-uk/home/household/kitchen-rolls-toilet-rolls-tissues/toilet-rolls-wipes/c/420
# morrisons: https://groceries.morrisons.com/search?entry=toilet%20roll
# +44 7447410553

import sys
import scrapy
from scrapy.crawler import CrawlerProcess


def test_version_and_path():
    print(sys.version)
    print(sys.executable)
   

class PaperSpider(scrapy.Spider):
    name = 'toiletPaper'

    start_urls = ['https://www.tesco.com/groceries/en-GB/search?query=toilet%20paper&icid=tescohp_sws-1_m-ft_in-toilet%20paper_ab-226-b_out-toilet%20paper']

    def parse(self, response):
        for product in response.xpath("//div[@class='product-list--list-item']"):
            yield {
                'product_name': product.xpath(".//h3[@class='sc-kAzzGY iTLNpo']").extract_first(),
                'product_price': product.xpath(".//span[@class='value']").extract_first()
            }


class AlertModel:
    # function to alert user when available toilet paper is found    
    def alert_me():
        account_sid = 'ACec8291bcf1440c2af4ea082bb02bc345'
        auth_token = '8c753f55a73d965dd44e5d3446f732e4'
        client = Client(account_sid, auth_token)

        message = client.messages \
        .create(
            body="Quick, toilet paper found at: ",
            from_='+19032252880',
            to='447864844377, 447447410553'
        )

        print(message.sid)

    def tor():
        print('todo')


test_version_and_path()
# AlertModel.alert_me()

process = CrawlerProcess()
process.crawl(PaperSpider)
process.start()