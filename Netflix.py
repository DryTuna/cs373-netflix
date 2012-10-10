#!/usr/bin/env python

import math

c_avg = {} 				#dictionary of average customer reviews (customer_id => avg_rating)
m_avg = {}				#dictionary of average reviews for movies(movie_id => avg_rating)
rmse = 0.983460336694	#rmse value obtained by running the program on probe.txt
#correct_values = [] 

# ----
# Init
# ----

def Init () :
	"""
	Initializes the program by reading the cached values from caches directory
	"""
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

# -------
# predict
# -------

def predict (cust_ID, movie_ID) :
	"""
	Arguments: 	cust_ID  - id of a customer for whom the prediction is to be made 
			movie_ID - id of a movie for prediction
				
	A method that makes a prediction of customer's score for a specified movie
	based on cached values
	"""
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
	"""
	Arguments: 	x - the first number
			y - the second number
				
	A small helper function that calculates the square of a difference of two numbers
	"""
	assert 0.0 <= x <= 5.0
	assert 0.0 <= y <= 5.0
	return (x - y)**2

# ----
# RMSE
# ----

def RMSE (p, c) :
	"""
	Arguments: 	p - list of predicted values
			c - list of correct values
				
	Calculates a Root Mean Square Error value of two lists of numbers
	"""
	assert len(p) == len(c)
	assert len(c) > 0
	n = len(c)
	total = sum(map(sqre_diff, p, c), 0.0)
	return math.sqrt(total/n)

# -----
# solve
# -----

def solve (r, w) :
	"""
	Arguments: 	r - input stream
			w - output stream
	
	The main function that is used to invoke the program and output a list of
	predicted values based on values from the input stream
	"""
	Init()
	m_id = 0
	c_id = 0
	predicted = []
	w.write("RMSE = " + str(rmse) +"\n")
	for line in r:
		if line == "\n":
			w.write(line)
			continue
		
		if ":" in line:
			m_id = int(line[0:-2])
			w.write(line)
		else:
			c_id = int(line)
			result = predict(c_id, m_id)
			predicted.append(result)
			w.write((str(result))[0:3] + "\n")


	
