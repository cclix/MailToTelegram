#!/usr/bin/python

import email, sqlite3, glob, os
from email.header import Header, decode_header, make_header
from sendtelegram import SendTelegram
from loadblacklist import LoadBlacklist
from loadconfig import LoadConfig

os.system("offlineimap")

conn = sqlite3.connect('mail.db')
c = conn.cursor()
c.execute('CREATE TABLE if not exists mails(ID INTEGER PRIMARY KEY AUTOINCREMENT, MAILID TEXT, MAILFROM TEXT, MAILTO TEXT, MAILSUBJECT TEXT, MAILBODY TEXT, SENT INTEGER)')

lbl = LoadBlacklist()
lbl.loadlist()
blacklist = lbl.getlist()

lc = LoadConfig()
lc.loadconfig()
mailpath = lc.getconfig('mailpath')

telegram = SendTelegram()
telegram.setToken(lc.getconfig('bottoken'))

for data in glob.glob(mailpath):
  f = open(data,"r")
  mail = f.read()
  f.close()  
  
  msg = email.message_from_string(mail)

  mailid = msg['Message-ID']
  mailid = mailid.encode('base64','strict');
  mailfrom = msg['from']

  mailto = msg['to']
  mailsubject = msg['subject']
  subjecttext = ""
  for text, encoding in email.Header.decode_header(mailsubject):
    subjecttext += text+" "
  subjecttext = str(subjecttext)
  mailbody = ""

  for part in msg.walk():
      if part.get_content_type() == 'text/plain':
          mailbody += part.get_payload()

  mailbody = str(mailbody)

  for entry in blacklist:
    if not entry in mailfrom:
      result = ""
      for row in c.execute("SELECT MAILID FROM mails WHERE MAILID='"+mailid+"' LIMIT 1"):
        result = row[0]

      if not result == mailid:
        telegramtext = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (mailfrom, mailto, subjecttext, mailbody)
        telegramtext = telegramtext[:4096]
        telegram.sendText(telegramtext)
        mailfrom = mailfrom.encode('base64','strict');
        mailto = mailto.encode('base64','strict');
        subjecttext = subjecttext.encode('base64','strict');
        mailbody = mailbody.encode('base64','strict');

        c.execute("INSERT INTO mails VALUES (null, '"+mailid+"', '"+mailfrom+"', '"+mailto+"', '"+subjecttext+"', '"+mailbody+"', 0)")
conn.commit()
conn.close()
