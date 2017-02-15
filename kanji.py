# -*- coding: utf-8 -*-
import sys, json, urllib
reload(sys)  
sys.setdefaultencoding('utf8')

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders


def email_file(info):
	SUBJECT = "Updated Kanji List"
	msg = MIMEMultipart()
	msg['Subject'] = SUBJECT 
	msg['From'] = "Kanji Bot"
	msg['To'] = ', '.join("esytsai@berkeley.edu")
	part = MIMEBase('application', "octet-stream")
	part.set_payload(open("kanji.txt", "rb").read())
	Encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="kanji.txt"')
	msg.attach(part)
	server = smtplib.SMTP("smtp.mail.yahoo.com","587")
	server.ehlo()
	server.starttls()
	server.login(info[0], info[1])
	server.sendmail(info[0] + "@yahoo.com", "esytsai@berkeley.edu", msg.as_string())
	server.quit()
	print("File sent to esytsai@berkeley.edu")


def main():
	while True:
		text = raw_input("")
		if text == "":
			print "No input"
		elif text[:5] == "email":
			text = text[5:].replace(' ','').split(',')
			email_file(text)
		elif text == "q":
			print("Quitting...")
			sys.exit(0)
		else: 
			print "Processed:" + text
			url = "http://www.transltr.org/api/translate?text=" + text + "&to=en&from=ja"
			definition = json.loads(urllib.urlopen(url).read())['translationText']
			print "Definition:" + definition
			url2 = "http://api.nihongoresources.com/dict/find/" + text
			hiragana = json.loads(urllib.urlopen(url2).read())[0]['reb'][0]
			print "Hiragana:" + hiragana
			file = open("kanji.txt", "a")
			file.write(text + ", " + hiragana + ", " + definition + "\n",)
			file.close()


if __name__ == '__main__':
	main()