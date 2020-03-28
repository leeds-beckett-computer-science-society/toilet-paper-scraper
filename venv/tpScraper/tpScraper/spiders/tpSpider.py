import scrapy
import socks 
import sockets 
import stem.process

class PaperSpider(scrapy.Spider):
    # anonymise scraping by using tor proxy
    SOCKS_PORT=7000 

    tor_process = stem.process.launch_tor_with_config(
        config = {
            'SocksPort': str(SOCKS_PORT),
        },
    )
    socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5,
                          addr="127.0.0.1",
                          port=SOCKS_PORT)
    socket.socket = socks.socksocket

    #------------------------- scrapy script----------------------------#
    name = 'toiletPaper'

    start_urls = ['https://www.tesco.com/groceries/en-GB/search?query=toilet%20paper&icid=tescohp_sws-1_m-ft_in-toilet%20paper_ab-226-b_out-toilet%20paper']

    def parse(self, response):

        product_url = ("https://www.tesco.com"+str(response.xpath("//*[@class='sc-bRBYWo hviAvs'][href]").extract_first()))
        product_price = response.xpath("//*[@class='value']").extract_first()

        print(product_url)
        print(product_price)

        for product in response.xpath("//*[@class='product-list--list-item']"):

            product_url = "https://www.tesco.com"+product.xpath("").extract_first()
            product_price = product.xpath("").extract_first()

            # yield {
            #     'product_url': product_url,
            #     'product_price': product_price
            # }

    #------------------------- scrapy script----------------------------#
    tor_process.kill()
