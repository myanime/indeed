#!/bin/bash          
export PATH=/usr/local/bin:$PATH
cd /home/myanime/indeed_australia/indeed/static/
echo Hello World >> ./runcounter
date +%d-%m-%Y_%H:%M > date
cd /home/myanime/indeed_australia/indeed/static/output
python deduplicate.py
sleep 20
echo Starting_Scrapy
cd /home/myanime/indeed_australia/indeed/
scrapy crawl main_scraper -o /home/myanime/indeed_australia/indeed/static/output/out_cron.csv

