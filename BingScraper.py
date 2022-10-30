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

print("....................Welcome to Left V Right - Bing/Google....................")
print(" - This program fetches two images from bing/google and aligns them horizontal - \n")
queries = sys.argv[1:]
if(len(queries)):
    imageOne = queries[0]
    imageTwo = queries[1]
else:
    imageOne = input("What/Who would you lke to find?")
    imageOne = imageOne.replace(' ',"+")
    imageTwo = input("Downloaded a picture of {0}. What else?".format(imageOne))
    imageTwo = imageTwo.replace(' ',"+")

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument(r'--load-extension=C:\Users\damet\Desktop\New folder\Programming\Github_Projects\Personal_WIP_Directory\discordbot_CLEAN\extension')
#chrome_options.add_argument('-headless')
#driver = webdriver.Chrome(chrome_options=chrome_options)
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"  #  complete
#caps["pageLoadStrategy"] = "eager"  #  interactive
#caps["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(desired_capabilities=caps, chrome_options=chrome_options)
driver.set_page_load_timeout(30)
# driver.maximize_window()

driver.implicitly_wait(20)
def googleScrape(query):
    driver.get('https://www.google.com/search?q={0}+file:jpg&tbm=isch&tbs=iar:t,isz:l'.format(query))
    # time.sleep(3)
    driver.find_element_by_xpath("(//div[contains(@class,'rg_bx rg_di rg_el ivg-i')])[{0}]".format(random.randint(1,10))).click()
    # driver.implicitly_wait(3)
    driver.find_element_by_xpath("//span[text()='View image']").click()
    driver.close()
    tab = driver.window_handles[0]
    driver.switch_to.window(tab)

def nsfwCheck():
    driver.get('https://www.bing.com/images/search?q=riley+reid+nsfw&FORM=HDRSC2')
    # time.sleep(3)
    driver.find_element_by_xpath("//span[text()='Turn it off']").click()
    # driver.implicitly_wait(4)
    driver.find_element_by_class_name("ss_pp_txt").click()


def bingScrape(query):
    driver.get('https://www.bing.com/images/search?q={0}=+filterui:imagesize-large+filterui:aspect-tall'.format(query))
    # driver.implicitly_wait(4)
    driver.find_element_by_xpath("(//img[contains(@class,'mimg')])[{0}]".format(random.randint(1,15))).click()
    # driver.implicitly_wait(4)
    driver.switch_to.frame("OverlayIFrame")
    # time.sleep(3)
    driver.find_element_by_xpath("//div[contains(@class,'action imgsrc nofocus')]").click()
    driver.close()
    tab = driver.window_handles[0]
    driver.switch_to.window(tab)
    
def combiner():
    size = 800,1200
    im1 = Image.open('bingOne.jpg')
    im2 = Image.open('bingTwo.jpg')
   
    im1.thumbnail(size, Image.ANTIALIAS)
    im1.save('bingOne.jpg')
    im2.thumbnail(size, Image.ANTIALIAS)
    im2.save('bingTwo.jpg')
    im1 = Image.open('bingOne.jpg')
    im2 = Image.open('bingTwo.jpg')
    dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst
    

# nsfwCheck() #eh em..
bingScrape(imageOne)
theUrl= driver.current_url
# driver.implicitly_wait(3)
bingScrape(imageTwo)
theNextUrl= driver.current_url
# driver.implicitly_wait(3)
driver.quit()

opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'whatever')
filename, headers = opener.retrieve(theUrl, 'bingOne.jpg')
filename, headers = opener.retrieve(theNextUrl, 'bingTwo.jpg')

finalIm = combiner().convert('RGB')
finalIm.save('bingOutput.jpg')
print("Complete.")
output = Image.open('bingOutput.jpg')
output.show()




