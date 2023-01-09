#!/usr/bin/env python3

import requests
import re
import random
import time
 
def extractSource(username):
    useragents = open('useragents.txt').read().splitlines()
    with open('websitelist.txt') as f:
        for site in f:
          site = site.strip()
          site = site + username
          useragent = random.choice(useragents)
          headers = {
            "User-Agent": useragent
          }
          r = requests.get(site, headers=headers)
          if r.status_code == 200:
            match = re.search(username, r.text)
            if match != "":
              print("Account found on: " + site)
              time.sleep(3)
          elif r.status_code != 200:
              print("Account not found on: " + site + "[Status Code: " + str(r.status_code) +"]")
              time.sleep(3)
              

  
def getData(body, site, username):
  htmlSplit = body.split(" ")
  print(htmlSplit)
  time.sleep(5)
  for x in htmlSplit:
    x = x.strip()
    if x == username:
      print("Acount found on: " + site)

def main():
  
  userName = input("Enter a username : ")
  
  extractSource(userName)

if __name__ == "__main__":
    main()