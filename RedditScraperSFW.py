from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import ctypes
import os
import time
import glob
import requests
#from lxml import html
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import numpy as np
from PIL import Image
import random
import sys
#from webdriver_manager.chrome import ChromeDriverManager

print("........................Welcome to Left V Right - Reddit....................")
print(" - This program fetches two images from Reddit and aligns them horizontally for comparison - \n")
queries = sys.argv[1:]
if(len(queries)>0):
    queries = sys.argv[1:]
    imageOne = queries[0]
    imageTwo = queries[1]
else:
    imageOne = input("Who would you look to find? ")
    imageOne = imageOne.replace(' ',"+")
    imageTwo = input("Downloading a picture of {0}. Who else? ".format(imageOne))
    imageTwo = imageTwo.replace(' ',"+")


options = webdriver.ChromeOptions()
#options.binary_location=r'C:\Users\Dametreuss\AppData\Local\Google\Chrome SxS\Application\chrome.exe'
#options.binary_location=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
options.add_argument('--no-proxy-server')
#options.add_argument('-headless')

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"  #  eager normal or complete

driver = webdriver.Chrome(desired_capabilities=caps, chrome_options=options)
driver.set_page_load_timeout(30)
driver.switch_to.window(driver.current_window_handle)
   
def combiner():
    size = 720,1080
    im1 = Image.open('resizeone.jpg')
    im2 = Image.open('resizetwo.jpg')

    im1.thumbnail(size, Image.ANTIALIAS)
    im1.save('imageOne.jpg')
    im2.thumbnail(size, Image.ANTIALIAS)
    im2.save('imageTwo.jpg')

    im1 = Image.open('imageOne.jpg')
    im2 = Image.open('imageTwo.jpg')
    dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

#Get First Link
driver.get('https://www.reddit.com/search/?q={0}+wallpaper+url:i.redd.it+url:.jpg+nsfw:no+NOT+with+NOT+and+NOT+vs+NOT+pick+NOT+%26&&sort=top'.format(imageOne))
driver.implicitly_wait(2)
firstUrl = driver.find_element_by_xpath("(//a[contains(@href,'i.redd.it/')])[{0}]".format(random.randint(1,6))).get_attribute('href')

#Get Second Link
driver.get('https://www.reddit.com/search/?q={0}+wallpaper+url:i.redd.it+url:.jpg+nsfw:no+NOT+with+NOT+and+NOT+vs+NOT+pick+NOT+%26&&sort=top'.format(imageTwo))
driver.implicitly_wait(2)
nextUrl = driver.find_element_by_xpath("(//a[contains(@href,'i.redd.it/')])[{0}]".format(random.randint(1,6))).get_attribute('href')

driver.quit()

#Download files
urllib.request.urlretrieve(firstUrl,'resize{0}.jpg'.format("one"))
urllib.request.urlretrieve(nextUrl,'resize{0}.jpg'.format("two"))

#Combine Them
finalIm = combiner().convert('RGB')
finalIm.save('output.jpg')
print("Complete.")
output = Image.open('output.jpg')
output.show()
