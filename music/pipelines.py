# -*- coding: utf-8 -*-
import sys; sys.path.append("/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages")
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MusicPipeline(object):
	def __init__(self):
		self.conn = MySQLdb.connect(user="root",passwd="ts0706",db="music")
		self.cursor = self.conn.cursor()
		self.conn.commit()

	def process_item(self, item, spider):
		try:
			self.cursor.execute("""INSERT INTO itunes (rank, name, artist, photo) VALUES (%s, %s, %s, %s)""", (item['rank'], item['name'], item['artist'], item['photo']))
			self.conn.commit();
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
	
		return item
