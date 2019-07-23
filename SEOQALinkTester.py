#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import random
import time
import sys
import requests
import datetime

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--incognito')

keys = Keys()
x = datetime.datetime.now()

data = ("""
https://www.website.com/uk/
""")

strip_data = data.strip()
split_data = strip_data.splitlines()
# print(split_data)

class webQA:
	def __init__(self):
		self.driverChrome = webdriver.Chrome(options = options, executable_path='/Users/Your.name/Downloads/chromedriver')

	def openLinks(self):
		browser = self.driverChrome
		browser.get('http://www.website.com/uk')
		time.sleep(2)
		try:
			usernameEntry = browser.find_element_by_id('username')
			usernameEntry.click()
			usernameEntry.send_keys('username')
			time.sleep(.5)
			passwordEntry = browser.find_element_by_id("password")
			passwordEntry.click()
			passwordEntry.send_keys('password')
			passwordEntry.send_keys(Keys.ENTER)
		except:
			pass	
		tabNum = 0
		for split in split_data:
			tabNum +=1
			browser.execute_script("window.open('new window')")
			browser.switch_to.window(browser.window_handles[tabNum])
			time.sleep(1) 
			browser.get(split)
			print(split)
			try:
				usernameEntry = browser.find_element_by_tag_name('username')
				usernameEntry.click()
				usernameEntry.send_keys(self.username)
				time.sleep(.5)
				passwordEntry = browser.find_element_by_id("password")
				passwordEntry.click()
				passwordEntry.send_keys(self.password)
				passwordEntry.send_keys(Keys.ENTER)
			except:
				pass

			# print alt text for all images
			print('--------------------------------------------------------------------')	
			print('ALT TEXT')
			print('--------------------------------------------------------------------')
			images = browser.find_elements_by_tag_name("img")
			for image in images :
				print(image.get_attribute("alt"))	
				# page title print
			print('--------------------------------------------------------------------')	
			time.sleep(.5)
			page_title = browser.find_element_by_css_selector('meta[name="title"]')
			print('Page title: ', end ='')
			print(page_title.get_attribute('content'))
			print('--------------------------------------------------------------------')	
			# print all SEO and meta data
			print('SEO META DATA')
			print('--------------------------------------------------------------------')
			print('TWITTER')
			# print(twitter_card.get_attribute('content'))
			# twitter meta data
			twitter_site = browser.find_element_by_css_selector("meta[name='twitter\\:site']")
			print('twitter site: ', end ='')
			print(twitter_site.get_attribute('content'))
			twitter_creator = browser.find_element_by_css_selector("meta[name='twitter\\:creator']")
			print('twitter creator: ', end ='')
			print(twitter_creator.get_attribute('content'))
			url_twitter = browser.find_element_by_css_selector("meta[name='twitter\\:url']")
			print('twitter url: ', end ='')
			print(url_twitter.get_attribute('content'))	
			twitter_title = browser.find_element_by_css_selector("meta[name='twitter\\:title']")
			print('twitter title: ', end ='')
			print(twitter_title.get_attribute('content'))
			twitter_description = browser.find_element_by_css_selector("meta[name='twitter\\:description']")
			print('twitter dexcription: ', end ='')
			print(twitter_description.get_attribute('content'))		
			# Facebook meta data
			print('--------------------------------------------------------------------')	
			print('FACEBOOK')
			facebook_site = browser.find_element_by_css_selector("meta[property='og:site_name']")
			print('Facebook site: ', end ='')
			print(facebook_site.get_attribute('content'))
			url_facebook = browser.find_element_by_css_selector("meta[property='og\\:locale']")
			print('facebook language: ', end ='')
			print(url_facebook.get_attribute('content'))	
			facebook_title = browser.find_element_by_css_selector("meta[property='og\\:title']")
			print('facebook title: ', end ='')
			print(facebook_title.get_attribute('content'))
			facebook_description = browser.find_element_by_css_selector("meta[property='og\\:description']")
			print('facebook description: ', end ='')
			print(facebook_description.get_attribute('content'))
			# break between
			print('--------------------------------------------------------------------')	
			print('OTHER META DATA')	
			# other meta data
			item_prop = browser.find_element_by_css_selector("meta[property='og\\:country-name']")
			print('country name: ', end ='')
			print(item_prop.get_attribute('content'))	
			item_prop = browser.find_element_by_css_selector("meta[itemprop='name']")
			print('item prop name: ', end ='')
			print(item_prop.get_attribute('content'))		
			canonical_link = browser.find_element_by_css_selector('link[rel="canonical"')
			print('canonical link: ', end ='')
			print(canonical_link.get_attribute('href'))			
			item_prop = browser.find_element_by_css_selector("meta[itemprop='keywords']")
			print('Keywords: ', end ='')
			print(item_prop.get_attribute('content'))	
			site_code = browser.find_element_by_css_selector("meta[name='sitecode']")
			print('Site code: ', end ='')
			print(site_code.get_attribute('content'))				
			print('---------------------------------------------------------------------------')	

			# print all link status and broken links 
			links = browser.find_elements_by_css_selector("a")

			for link in links:
				try:
					r = requests.head(link.get_attribute('href'))
					print(link.get_attribute('href'), r.status_code)
				except:
					continue
			print('broken Links check is complete for  website')			

run = webQA()
run.openLinks()
