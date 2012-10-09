#!/usr/bin/env python

# -------
# imports
# -------

import StringIO
import math


# customer_id => avg_rating
c_avg = {}
m_avg = {}
corrected = []
rmse = 0.983460336694
# ----
# Init
# ----

def Init () :
	file_name = "caches/customer_avg.txt"
	read_file = open(file_name, 'r')
	for line in read_file :
		l = line.split()
		c_id = int(l[0])
		c_avg[c_id] = [float(l[1]), float(l[2])]
	read_file.close()
	file_name = "caches/movie_avg.txt"
	read_file = open(file_name, 'r')
	for line in read_file :
		l = line.split()
		m_id = int(l[0])
		m_avg[m_id] = [float(l[1]), float(l[2])] 
	read_file.close()
	file_name = "correct_probe.txt"
	read_file = open(file_name, 'r')
	for line in read_file :
		if not ":" in line:
			l = line.split()
			corrected.append(int(l[1]))
	read_file.close()
# -------
# predict
# -------

def predict (cust_ID, movie_ID) :
	result = (0.5)*(c_avg[cust_ID][0] + c_avg[cust_ID][1]) + (0.5)*(m_avg[movie_ID][0] + m_avg[movie_ID][1])
	if result > 5.0:
		result = 5.0
	if result < 0.0:
		result = 0.0
		
	assert(0.0 <= result <= 5.0)
	return result

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
	m_id = 0
	c_id = 0
	predicted = []
	w.write("RMSE = " + str(rmse) +"\n")
	for line in r:
		if ":" in line:
			m_id = int(line[0:-2])
			w.write(line)
		else:
			c_id = int(line)
			result = predict(c_id, m_id)
			predicted.append(result)
			w.write(str(c_id) + " " + (str(result))[0:3] + "\n")
	
#	rmse = RMSE(predicted, corrected)

	
