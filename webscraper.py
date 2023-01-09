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
#gui library
import tkinter as tk
from tkinter import * 
from tkinter import ttk

listPathuser = ''
URLuser = ''
def savelist():
  listPathuser = (txt.get())
  return(listPathuser)
def savelink():
  URLuser = (txt2.get())
  return(URLuser)


def extractSource(url):
  try:
    browser = webdriver.Firefox()
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.add_argument("--headless")
    browser = webdriver.Firefox(options=fireFoxOptions)
    browser.get(url)
    browser.implicitly_wait(5)
    body = browser.find_element(By.XPATH, "//body[1]")
    return body.text
    
    browser.quit()
  finally:
    try:
      browser.quit()
    except:
      pass
      
def getData(body, wordlist):
  htmlSplit = []
  goodWords = []
  wordCount = 0
  table = PrettyTable()

  htmlSplit = body.split(" ")
  for x in htmlSplit:
    x = x.strip()
    x = re.sub('[^a-zA-Z\d\s:]', '', x)
    if x.lower() in wordlist:
      goodWords.append(x)
      wordCount += 1 

  goodWords = Counter(goodWords)
  goodWords = dict(sorted(goodWords.items(), key=lambda item: item[1]))

  #table.field_names = ["Keyword", "Times used"]
  #print(goodWords)
  #for k, v in goodWords.items():
    #table.add_row([k,v])
  
  # initialize the tkinter GUI
  meow = Toplevel(root)
  meow.title("Webscrapbrr")
  meow.geometry("220x230")
  #meow.pack_propagate(0)
  meow.resizable(0, 0)
  #columns
  columns = ['Keyword', 'Count']
  #treeview
  tree = ttk.Treeview(meow, columns=columns, show='headings')
  #treeview headings
  tree.heading('Keyword', text='Keyword')
  tree.heading('Count', text='Count')
 
  for column in columns:  # foreach column
    tree.column(column, width=100)  # set the columns size to 50px

    # foreach row of goodwords insert the row into the treeview.
  for row in goodWords.items():
    tree.insert("", "end", values=row)

  tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
  scrollbar = ttk.Scrollbar(meow, orient=tk.VERTICAL, command=tree.yview)
  tree.configure(yscroll=scrollbar.set)
  scrollbar.grid(row=0, column=1, sticky='ns')

def main(): 

  wordList = []
  with open(savelist()) as f:
    for word in f:
      word = word.strip()
      word = word.lower()
      wordList.append(word)  

  getData(extractSource(savelink()), wordList)


# create root window
root = Tk()

# root window title and dimension
root.title("Webscrapbrr")
# Set geometry(widthxheight)
root.geometry('400x100')

# adding a label to the root window
lbl1 = Label(root, text = "Wordlist Path")
lbl1.grid()
lbl2 = Label(root, text = "Website Link")
lbl2.grid()

# adding Entry Field
txt = Entry(root, width=20)
txt.grid(column =1, row =0)
txt2 = Entry(root, width=20)
txt2.grid(column =1, row=1)




# button widget 
btn = Button(root, text = "Save List" ,
			fg = "red", command=savelist)
btn2 = Button(root, text = "Save Link" ,
			fg = "blue", command=savelink)
btn3 = Button(root, text = "RUN" ,
			fg = "green", command= main)
# Set Button Grid
btn.grid(column=2, row=0)
btn2.grid(column=2, row=1)
btn3.grid(column=1, row=3)
# Execute Tkinter
root.mainloop()
