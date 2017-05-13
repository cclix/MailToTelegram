#!/usr/bin/python

class LoadBlacklist:

  list = []

  def loadlist(self):
    tmplist = []
    f = open("./config/blacklist.txt","r")
    for counter, data in enumerate(f.readlines()):
      tmplist.append([])
      item = data
      item = item.replace('\n', '')
      item = item.replace('\n', '')
      tmplist[counter] = item 
    f.close()
    self.list = tmplist
    #print len(self.list)
    #print self.list    

  def getlist(self):
    return self.list
