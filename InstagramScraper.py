
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
from selenium.webdriver.common.keys import Keys

print("....................Welcome to Left V Right - Instagram....................")
print(" - This program fetches two images from instagram and aligns them horizontally for comparison - \n")
#please understand that this was commissioned, this is not my idea lol

instas = sys.argv[1:]
if(len(instas)>0):
    igOne = instas[0]
    igTwo = instas[1]
else:
    igOne = input("Who would you like to find first?")
    igOne = igOne.replace(' ',"+")
    igTwo = input("Downloading a picture of {0}. Who else?".format(igOne))
    igTwo = igTwo.replace(' ',"+")

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
#options.binary_location=r'C:\Users\Dametreuss\AppData\Local\Google\Chrome SxS\Application\chrome.exe'
#options.binary_location=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
options.add_experimental_option("prefs",prefs)
options.add_argument('--no-proxy-server')
#chrome_options.add_argument('-headless')
#driver = webdriver.Chrome(chrome_options=chrome_options)
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"  #  complete
#caps["pageLoadStrategy"] = "eager"  #  interactive
#caps["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(desired_capabilities=caps, chrome_options=options)
driver.set_page_load_timeout(30)
#driver.get('https://www.reddit.com/r/nsfw')

driver.implicitly_wait(20)

def instaScrape(query): #
    driver.get('https://google.com')
    # driver.implicitly_wait(1)
    driver.find_element_by_name("q").send_keys(query +" instagram  -hashtag")
    driver.find_element_by_name("q").send_keys(Keys.ENTER)
    # driver.implicitly_wait(1)
    theurl = driver.find_element_by_xpath("(//a[contains(@href,'instagram.com/')])[1]").get_attribute('href')
    user=theurl.split('/')[3]
    print(user)
    # newUrl = 'https://saveig.com/' + user[3]
    driver.get('https://saveinsta.app/')
    # driver.implicitly_wait(5)
    driver.find_element_by_class_name('icon-photo').click()
    driver.find_element_by_class_name('icon-photo').click()
    driver.find_element_by_id('s_input').send_keys(user)
    driver.find_element_by_class_name('btn-default').click()
    # driver.implicitly_wait(15)
    driver.find_element_by_class_name('btn-secondary').click()
    # driver.implicitly_wait(10)
    link = driver.find_element_by_xpath("(//a[contains(@href,'instagram.com/')])[1]").get_attribute('href')
    # print(link)
    

 
def combiner():
    size = 1080,1080
    im1 = Image.open('igOne.jpg')
    im2 = Image.open('igTwo.jpg')
  
    im1.thumbnail(size, Image.ANTIALIAS)
    im1.save('instaOne.jpg')
    im2.thumbnail(size, Image.ANTIALIAS)
    im2.save('instaTwo.jpg')
    im1 = Image.open('instaOne.jpg')
    im2 = Image.open('instaTwo.jpg')
    dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst
    
# time.sleep(3)
instaScrape(igOne)
# driver.implicitly_wait(1)
# driver.find_element_by_id('s_input').send_keys(user)

theUrl= driver.find_element_by_xpath("(//a[contains(@class,'abutton')])[{0}]".format(random.randint(1,10))).get_attribute('href')
# print(fixed_link)
while(".mp4" in theUrl or "cdn.xyz" in theUrl):
    theUrl= driver.find_element_by_xpath("(//a[contains(@class,'abutton')])[{0}]".format(random.randint(1,10))).get_attribute('href')
    print("Found a video, choosing again")
fixed_link=theUrl.replace('dl=1','')

instaScrape(igTwo)
# driver.implicitly_wait(1)
theNextUrl= driver.find_element_by_xpath("(//a[contains(@class,'abutton')])[{0}]".format(random.randint(1,10))).get_attribute('href')
while(".mp4" in theNextUrl or "cdn.xyz" in theNextUrl):
    theNextUrl= driver.find_element_by_xpath("(//a[contains(@class,'abutton')])[{0}]".format(random.randint(1,10))).get_attribute('href')
    print("Found a video, choosing again")
# while(".mp4" in theNextUrl):
#     theNextUrl= driver.find_element_by_xpath("(//a[contains(@class,'abutton')])[{0}]".format(random.randint(2,8))).get_attribute('href')
#     print("Found a video, choosing again")
next_fixed_link=theNextUrl.replace('dl=1','')
print(next_fixed_link)

driver.quit()

urllib.request.urlretrieve(fixed_link,'igOne.jpg')

urllib.request.urlretrieve(next_fixed_link,'igTwo.jpg')

finalIm = combiner().convert('RGB')
finalIm.save('igOutput.jpg')
print("Complete.")
output = Image.open('igOutput.jpg')
output.show()




