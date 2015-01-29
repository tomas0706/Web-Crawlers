from music.items import MusicItem
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from ConfigParser import *
import MySQLdb
import urllib
import re

SPIDER_NAME = "music"
SITE_URL = "https://www.apple.com/itunes/charts/songs/"
DOMAIN = "apple.com"

TITLES_XPATH = "//li";
RANK_PATH = "./strong/text()";
NAME_XPATH = "./h3/a/text()";
ARTIST_XPATH = "./h4/a/text()";
PHOTO_XPATH = "./a[1]/img/@src";

def extract_rank(rank_list):
	rank = ""
	for item in rank_list:
		rank += item;
	length = len(rank);
	return rank[0:(length -1)];


class MySpider(BaseSpider):
	name = SPIDER_NAME;
	allowed_domains = [DOMAIN];
	start_urls = [SITE_URL];
    
	def parse(self, response):
		hxs = HtmlXPathSelector(response);
		titles = hxs.select(TITLES_XPATH);
		musics = [];
        
		for title in titles:
			music = MusicItem();
        
			music['rank'] = extract_rank(title.select(RANK_PATH).extract());
			music['name'] = title.select(NAME_XPATH).extract();
			music['artist'] = title.select(ARTIST_XPATH).extract();
			music['photo'] = title.select(PHOTO_XPATH).extract();
			musics.append(music);
		return musics;

