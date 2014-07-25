#-*- coding: utf-8 -*-
# JTBC 뉴스 속보 xml문서 파싱하기

import urllib
from xml.etree.ElementTree import parse

xml = urllib.urlopen('http://fs.jtbc.joins.com/RSS/newsflash.xml')	# 속보

tree = parse(xml)		# xml 파싱하여 나뭇가지 구조 얻기
root = tree.getroot()	# root태그 얻어오기
num = 0
number = 0 
for parent in root.getiterator():	# root태그부터 시작하여 모든 태그를 반복
	for child in parent.findall("item"):	# item 태그를 모두 반복
		num += 1 
		print "%d"%(num)+ " "+ child.find("title").text
#		print child.findtext("link")
		
		# 뉴스 내용 보기
#		print child.findtext("description")

print  "\n"
news = raw_input('보고 싶은 뉴스를 선택하세요 : ')
for parent in root.getiterator():	
	for child in parent.findall("item"):	
		number += 1
		if int(news) == number :
			print child.find("title").text
			print child.findtext("link")