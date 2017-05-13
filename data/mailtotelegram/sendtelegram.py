#!/usr/bin/python

import urllib

bottoken = ''

class SendTelegram:

  def sendText(self, text):
    if len(text) > 4096:
      text = 'Text has more than 4096 characters.'
    
    if self.bottoken == '':
      print 'No token set.'
      return 
  
    params = urllib.urlencode({'chat_id': 107872976, 'text': text})
    f = urllib.urlopen("https://api.telegram.org/bot"+self.bottoken+"/sendMessage", params)
#    print f.read()
  
  def setToken(self, token):
    self.bottoken = token
