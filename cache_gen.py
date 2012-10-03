#!/usr/bin/env python


# -------
# imports
# -------

import sys
import random

def generate (w):
	for m_id in range (1, 17771) :
		file_name = "training_set/mv_"+'%0*d' % (7, m_id)+".txt"
		read_file = open(file_name, 'r')
		sum_rating = 0
		count = -1
		for line in read_file :
			if count >= 0 :
				l = line.split(',')
				sum_rating += int(l[1])
			count += 1
		read_file.close()
		avg_rating = float(sum_rating) / count
		result = str(m_id) + " " + str(avg_rating) + "\n"
		w.write(result)

# ----
# main
# ----

generate(sys.stdout)
