import scrapy

class PaperSpider(scrapy.Spider):
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