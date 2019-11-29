from __future import print_function, division

import sys

age_sum = 0
counter = 1


for line in sys.stdin:  # This sys.stdin is taking the output from average_age_map.py (which prints data[0])
	line = line.strip()

	if line:
		try:
			counter += 1
			age_sum += float(line.strip().replace('\n', ''))
		except:
			pass

print(age_sum / counter)