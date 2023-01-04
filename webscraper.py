#!/usr/bin/env python3

import requests
import re
from collections import Counter
from prettytable import PrettyTable

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
  
def extractSource(url):
  browser = webdriver.Firefox()
  fireFoxOptions = webdriver.FirefoxOptions()
  fireFoxOptions.add_argument("--headless")
  browser = webdriver.Firefox(options=fireFoxOptions)
  browser.get(url)
  browser.implicitly_wait(5)
  body = browser.find_element(By.XPATH, "//body[1]")
  return body.text
    
  browser.quit()
   
def getData(body, wordlist):
  htmlSplit = []
  goodWords = []
  wordCount = 0
  table = PrettyTable()

  htmlSplit = body.split(" ")
  for x in htmlSplit:
    x = x.strip()
    x = re.sub('[^+a-zA-Z\d\s:]', '', x)
    if x.lower() in wordlist:
      goodWords.append(x)
      wordCount += 1 

  goodWords = Counter(goodWords)
  goodWords = dict(sorted(goodWords.items(), key=lambda item: item[1]))

  table.field_names = ["Keyword", "Times used"]
  
  for k, v in goodWords.items():
    table.add_row([k,v])

  print(table)


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