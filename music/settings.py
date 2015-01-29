# -*- coding: utf-8 -*-

# Scrapy settings for music project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'music'

SPIDER_MODULES = ['music.spiders']
NEWSPIDER_MODULE = 'music.spiders'

ITEM_PIPELINES = [
	'music.pipelines.MusicPipeline',
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'music (+http://www.yourdomain.com)'
