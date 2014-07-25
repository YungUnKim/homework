
import urllib
import json

htmltext = urllib.urlopen("http://codingsroom.com/likelion/json_example2.php")

data = json.load(htmltext)

print "MEM_NUM        age        job       MEM_CODE          etc "
for data_list in data['data']:
	print "%5s %11s %15s %12s       "%(data_list['MEM_NUM'], data_list['age'], data_list['job'], data_list['MEM_CODE']),
	if data_list['age'] > 50 and data_list['job'] == 'Programmer' :
		print 'Master old'
	elif data_list['age'] > 50 :
		print 'old'
	elif data_list['job'] == 'Programmer' :
		print 'Master'
	else:
		print ""