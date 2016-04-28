import scrapy
from indeed.items import IndeedItem
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import random
import re

class URLScraper(scrapy.Spider):
    name = "url_scraper"
    start_urls = []
    #start_urls = [line.rstrip("\n") for line in open('./links')]
    def parse(self, response):
        test = str(response.url)
        yield IndeedItem(test=test)

class MainScraper(scrapy.Spider):
    name = "main_scraper"
    start_urls = [line.rstrip("\n") for line in open ('./indeedurls')]
    #start_urls = ['https://smartjobs.qld.gov.au/jobtools/jncustomsearch.viewFullSingle?in_organid=14904&in_jncounter=221514880&in_site=Indeed']
    #start_urls = ['http://au.indeed.com/jobs?q=&l=australia&fromage=last&sort=date']
        
    def parse_original_url(self, response):
        item = response.meta['item']
        item['original_link'] = response.url
        original_html = response.xpath('//body').extract()
        original_plain_text = BeautifulSoup(response.xpath('//body').extract_first()).get_text()
        emails = []
        telephone_numbers = []

        re_email = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
        re1 = r'(0[1-8]{1,1} [0-9]{3,5} [0-9]{3,5})'
        re2 = r'(\([0-9]{2,2}\).[0-9]{3,5}.[0-9]{3,5})'
        re3 = r'\+61.[0-9]{1,1}.[0-9]{2,5}.[0-9]{2,5}.[0-9]{2,5}'

        
        e1 = re.search(re_email, original_plain_text, re.I)
        if e1:
            emails.append(e1.group())
        t1 = re.search(re1, original_plain_text, re.I)
        t2 = re.search(re2, original_plain_text, re.I)
        t3 = re.search(re3, original_plain_text, re.I)
        if t1:
            telephone_numbers.append(t1.group())
        if t2:
            telephone_numbers.append(t2.group())
        if t2:
            telephone_numbers.append(t3.group())
        try:    
            item['original_link_emails'] = emails[0]
            item['original_link_emails2'] = emails[1]
            item['original_link_emails3'] = emails[2]
        except:
            pass
        try:                
            item['original_link_telephones'] = telephone_numbers[0]
            item['original_link_telephones2'] = telephone_numbers[1]
            item['original_link_telephones3'] = telephone_numbers[2]
        except:
            pass
        original_plain_text = None
        original_html = None
        
        item['original_plain_text'] = original_plain_text
        item['original_html'] = original_html
        
        image_link = item['image_link']
        try:
            image_link = "http://au.indeed.com" + image_link
        except:
            image_link = None
            yield item
        if image_link != None:
            request = scrapy.Request(image_link, callback=self.parse_image_src)
            request.meta['item'] = item
            yield request

    def parse_image_src(self, response):
        item = response.meta['item']
        try:
            image_src_link = response.css('div#cmp-header-logo img').xpath("@src").extract()
        except:
            image_src_link = None
        item['image_src_link'] = image_src_link
        return item 

    def parse(self, response):
        for x in range (0, 10):
            range_lower = None
            range_upper = None
            job_title = None
            job_description = None
            job_location = None
            job_company = None
            job_date = None
            salary_description = None
            job_money_unchanged = None
            
            job_title = response.xpath('//h2/a/text()')[x].extract()
            job_description = response.css('span.summary::text')[x].extract()
            job_location = response.css('span.location span::text')[x].extract()
            job_company = None
            job_date = response.css('span.date::text')[x].extract()
            try:
                job_money = response.css('td.snip nobr::text')[x].extract()
                job_money = str(job_money)
                job_money_unchanged = job_money 

                if re.search(r' a year', job_money):
                    job_money = job_money.split(' a year')[0]    
                    salary_description = 'a year'
                if re.search(r' an hour', job_money):
                    job_money = job_money.split(' an hour')[0]    
                    salary_description = 'an hour'
                if re.search(r'-', job_money):
                    range_lower = job_money.split(" - ")[0]
                    range_upper = job_money.split(" - ")[1]
            except:
                job_money = None
            
            try:
                job_company = response.xpath('//div['+ str(x+4) +']/span[1]/span/a/text()').extract_first()
                if job_company == None:
                    job_company = response.xpath('//div['+ str(x+4) +']/span[1]/span/text()').extract_first()
                if job_company == None:
                    job_company = "Nothing"
            except:
                job_company = None
            try:
                image_link = response.xpath('//div['+ str(x+4) +']/span[1]/span/a/@href').extract_first()
            except:
                image_link = None
                
            half_link = response.xpath('//h2/a').xpath("@href")[x].extract()
            full_link = "http://au.indeed.com" + half_link
            item = IndeedItem()
            item['jobNumber'] = x
            item['job_title'] = job_title
            item['job_description'] = job_description
            item['job_location'] = job_location
            item['job_company'] = job_company
            item['job_date'] = job_date
            item['job_money'] = job_money
            item['range_upper'] = range_upper
            item['job_money_unchanged'] = job_money_unchanged
            item['range_lower'] = range_lower
            item['salary_description'] = salary_description
            item['image_link'] = image_link
            request = scrapy.Request(full_link, callback=self.parse_original_url)
            request.meta['item'] = item
            yield request
