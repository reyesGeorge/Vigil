
import scrapy 
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector
from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings



import pandas as pd


class firstSpider(scrapy.Spider): 
  name = "basic2" 
  # custom_settings = { 'DOWNLOD_DELAY': 1 }
  #  start_urls = ['URL1','URL2']


  start_urls = [ 
    f"https://www.google.com/search?q=hey"
    ]


  # custom_settings = { 'DOWNLOD_DELAY': 1, 'ROBOTSTXT_OBEY': False}
  # headers = {} 
  # params = {}
  # def start_requests(self):
  #   start_urls = [ 
  #   "https://www.google.com/search?q=journal+dev"
  #  ]
  #   for url in start_urls:
  #     yield scrapy.Request(url, headers=headers, params=params,callback = self.parse)
  #   else:
  #     pass
  
  def parse(self, response):
    df = pd.DataFrame()
    xlink = LinkExtractor()
    link_list=[]
    link_text=[]
    divs = response.xpath('//div')
    text_list=[]
    header_list=[]
    for h3 in divs.xpath('text()'):
        if len(str(h3.get())) > 2:
            header_list.append(h3.get())
        else:
            pass
        
    
    # df['links']=link_list
    # df['link_text']=link_text
    # df['text_meta'] = text_list
    df['header'] = header_list
    df.iloc[4:]
    # return df
    df.to_csv('serpData.csv')


if __name__ == "__main__":
  # process = CrawlerProcess()
  process = CrawlerProcess(get_project_settings())
  process.crawl('basic2', firstSpider)
  process.start()