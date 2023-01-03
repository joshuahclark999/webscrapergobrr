#!/usr/bin/env python3

import requests
import random
from bs4 import BeautifulSoup
from collections import Counter

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By

def getUserAgent():
  userAgents = []
  with open('useragent.txt') as ua:
    for agent in ua:
      agent = agent.strip()
      userAgents.append(agent)
  agentNum = random.random() * len(userAgents)
  newAgent = userAgents[int(agentNum)]
  return newAgent
  

def getProxy():
  proxies = []
  with open('proxylist.txt') as pl:
    for proxy in pl:
      proxy = proxy.strip()
      proxies.append(proxy)
  proxyNum = random.random() * len(proxies)
  newProxy = proxies[int(proxyNum)]
  return newProxy
  
  

def extractSource(url):
  # proxies = {
  #   'http': 'http://9ec8a99403081b4a7dfdf7ccfa2c19bc66f56e68:@proxy.zenrows.com:8001',
  #   'https': 'http://9ec8a99403081b4a7dfdf7ccfa2c19bc66f56e68:@proxy.zenrows.com:8001'
  # } 
  # userAgent = {'User-Agent':getUserAgent()}
  # source = requests.get(url, headers=userAgent, proxies=proxies, verify=False).textwordl
  # return source
  try:
    browser = webdriver.Firefox()
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.add_argument("--headless")
    browser = webdriver.Firefox(options=fireFoxOptions)
    browser.get(url)
    browser.implicitly_wait(10)
    body = browser.find_element(By.XPATH, "//body[1]")
    print(body.text)
    
    browser.close()
  finally:
    try:
      browser.close()
    except:
      pass
      
def getData(source, wordlist):
  soup = BeautifulSoup(source,"html.parser")
  body = soup.findAll()
  htmlSplit = []
  goodWords = []
  
  print(body)
  # for body in names:
  #   htmlSplit = body.text.split()
  #   for x in wordlist:
  #     if x in htmlSplit or x.lower() in htmlSplit:
  #      goodWords.append(x)

  goodWords = Counter(goodWords)
  print(goodWords)
    

def main():
  
  # listPathuser = input("Enter a path to a list :> ")
  URLuser = input("Enter job listing link :> ")  
  wordList = []
  # with open(listPathuser) as f:
  #   for word in f:
  #     word = word.strip()
  #     wordList.append(word)  
  extractSource(URLuser)
  # getData(extractSource(URLuser), wordList)
  
if __name__ == "__main__":
    main()