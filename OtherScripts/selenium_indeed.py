from selenium import webdriver
import time 
start_urls = ['http://au.indeed.com/jobs?q=&l=australia&rq=1&fromage=last',\
              'http://au.indeed.com/jobs?q=&l=australia&fromage=last&start=10',\
              'http://au.indeed.com/jobs?q=&l=australia&fromage=last&start=20',\
              'http://au.indeed.com/jobs?q=&l=australia&fromage=last&start=30',\
              'http://au.indeed.com/jobs?q=&l=australia&fromage=last&start=40',\
              'http://au.indeed.com/jobs?q=&l=australia&fromage=last&start=50',\
              'http://au.indeed.com/jobs?q=&l=australia&fromage=last&start=60']
driver = webdriver.Firefox()
driver.get(start_urls[1])
time.sleep(50)
driver.get(start_urls[2])
time.sleep(5)
driver.get(start_urls[3])
time.sleep(5)
driver.get(start_urls[4])
time.sleep(5)
driver.get(start_urls[5])
time.sleep(5)
