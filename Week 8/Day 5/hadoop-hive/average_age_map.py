from __future__ import print_function, division
from ast import literal_eval

import sys



for line in sys.stdin:
	try:
		data = line.replace('\n', "").split(', ')
		print(data[0])   # This creates a raw output for the aver_age_reduce.py file
		# So the output of this WHO:E average_age_map file will save a whole raw text output of each row in the csv file of data[0]
	except:
		pass
