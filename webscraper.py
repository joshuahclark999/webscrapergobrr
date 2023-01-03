#!/usr/bin/env python3

import requests
import re
from collections import Counter

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
  
def extractSource(url):
  try:
    browser = webdriver.Firefox()
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.add_argument("--headless")
    browser = webdriver.Firefox(options=fireFoxOptions)
    browser.get(url)
    browser.implicitly_wait(10)
    body = browser.find_element(By.XPATH, "//body[1]")

    return body.text
    
    browser.close()
  finally:
    try:
      browser.close()
    except:
      pass
      
def getData(body, wordlist):
  htmlSplit = []
  goodWords = []
  htmlSplit = body.split(" ")
  for x in htmlSplit:
    x = x.strip()
    x = re.sub('[^a-zA-Z\d\s:]', '', x)
    if x.lower() in wordlist:
      goodWords.append(x)
  
  goodWords = Counter(goodWords)
  print(goodWords)
    

def main():
  
  listPathuser = input("Enter a path to a list :> ")
  URLuser = input("Enter job listing link :> ")  
  wordList = []
  with open(listPathuser) as f:
    for word in f:
      word = word.strip()
      word = word.lower()
      wordList.append(word)  

  getData(extractSource(URLuser), wordList)
  
if __name__ == "__main__":
    main()