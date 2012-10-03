#!/usr/bin/env python


# -------
# imports
# -------

import sys
import random

# ---------
# movie_avg
# ---------

def movie_avg (w):
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

# ------------
# customer_avg
# ------------

def customer_avg (w):
	dictionary = {}
	for m_id in range (1, 17771) :
		file_name = "training_set/mv_"+'%0*d' % (7, m_id)+".txt"
		read_file = open(file_name, 'r')
		count = -1
		for line in read_file :
			if count >= 0 :
				l = line.split(',')
				c_id = int(l[0])
				try :
					v = dictionary[c_id]
					v[0] += float(l[1])
					v[1] += 1
				except KeyError :
					dictionary[c_id] = [float(l[1]), 1]
			else :
				count += 1
		read_file.close()
	for k in dictionary :
		v = dictionary[k]
		result = str(k) + " " + str(v[0]/v[1]) +"\n"
		w.write(result)

# ------
# offset
# ------

def offset (w):
	avg = 3.67410130345
	file_name = "customer_avg.txt"
	read_file = open(file_name, 'r')
	for line in read_file :
		l = line.split()
		o = float(l[1]) - avg
		result = str(l[0]) + " " + str(l[1]) + " " + str(o) + "\n"
		w.write(result)
	read_file.close()

# -------
# average
# -------

def avg (r):
	sum_rating = 0.0
	count = 0
	for line in r :
		l = line.split()
		sum_rating += float(l[1])
		count += 1
	avg = float(sum_rating) / count
	print str(avg)

# ----
# main
# ----

#movie_avg (sys.stdout)
#customer_avg (sys.stdout)
#avg (sys.stdin)
offset (sys.stdout)
