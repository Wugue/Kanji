# -*- coding: utf-8 -*-
import sys, json, urllib
reload(sys)  
sys.setdefaultencoding('utf8')


def main():
	while True:
		text = raw_input("")
		if text == "":
			print "No input"
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