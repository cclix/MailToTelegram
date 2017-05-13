#!/usr/bin/python

class LoadConfig:

  list = []

  def loadconfig(self):
    tmplist = []
    f = open("./config/config.txt","r")
    for counter, data in enumerate(f.readlines()):
      data = data.split('=')
      tmplist.append([])
      key = data[0]
      key = key.replace('\n', '')
      key = key.replace('\n', '')
      value = data[1]
      value = value.replace('\n', '')
      value = value.replace(' ', '')
      tmplist[counter] = [key,value] 
    f.close()
    self.list = tmplist

  def getconfig(self, key):
    for value in self.list:
      if value[0].replace(' ', '') in key:
        return value[1]
  
