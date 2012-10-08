#!/usr/bin/env python

# -------
# imports
# -------

import StringIO
import math


# customer_id => avg_rating
c_avg = {}
m_avg = {}
rmse = 0.0

# ----
# Init
# ----

def Init () :
	file_name = "caches/customer_avg.txt"
	read_file = open(file_name, 'r')
	for line in read_file :
		l = line.split()
		c_id = int(l[0])
		c_avg[c_id] = float(l[1])
	read_file.close()
	file_name = "caches/movie_avg.txt"
	read_file = open(file_name, 'r')
	for line in read_file :
		l = line.split()
		m_id = int(l[0])
		m_avg[m_id] = float(l[1])
	read_file.close()

# -------
# predict
# -------

def predict (cust_ID, movie_ID) :
	return c_avg[cust_ID]

# ---------
# sqre_diff
# ---------

def sqre_diff (x, y) :
	assert 0.0 <= x <= 5.0
	assert 0.0 <= y <= 5.0
	return (x - y)**2

# ----
# RMSE
# ----

def RMSE (p, c) :
	assert len(p) == len(c)
	assert len(c) > 0
	n = len(c)
	total = sum(map(sqre_diff, p, c), 0.0)
	return math.sqrt(total/n)

# -----
# solve
# -----

def solve (r, w) :
	Init()
	w.write("RMSE = " + str(rmse))
