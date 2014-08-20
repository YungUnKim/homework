def guess(record):
	#-All Code Here-
	import random
	x,y = 0,0
	num = 0
	latest = record.get_latest()
	latest_one = record.get_history_at(1, direction = 'BACKWARD')
	latest_two = record.get_history_at(2, direction = 'BACKWARD')
	latest_three = record.get_history_at(3, direction = 'BACKWARD')

	while True:
		if record.get_status_at(x,y) == Board.Status.EMPTY and x in range(0,10) and y in range(0,10):
			break
		else:
			if latest["result"] == Record.Status.HIT:
				if latest["result"] == Record.Status.SINK :
					x = random.randint(0,9)
					y = random.randint(0,9)					
				elif latest["result"] != Record.Status.SINK :
					if latest_one and latest["result"] == Record.Status.HIT and latest_one["result"] == Record.Status.HIT and num<3 :
						x = latest["guess"]['x'] + (latest_one["guess"]['x'] - latest["guess"]['x']) 
						y = latest["guess"]['y'] + (latest_one["guess"]['y'] - latest["guess"]['y'])
						num += 1
					else:
						x = random.randint(0,9)
						y = random.randint(0,9)
			elif latest["result"] != Record.Status.HIT:
				x = random.randint(0,9)
				y = random.randint(0,9)
	#-All Code End-
	return x,y