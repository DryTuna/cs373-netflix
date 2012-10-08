#!/usr/bin/env python


# -------
# imports
# -------

import sys
import random

def probe (w):
	file1 = "probe.txt"
	read1 = open(file1)
	dictionary = []
	m_id = 1
	for line in read1:
		dictionary += [str(line),]
	read1.close()
	m = 1
	for key in dictionary :
		if ":" in key :
			m = int(key[0:-2])
			w.write(str(key))
		else :
			c = int(key)
			file2 = "training_set/mv_"+'%0*d' % (7,m)+".txt"
			read2 = open(file2)
			for line in read2 :
				l2 = line.split(',')
				if not ":" in line :
					if int(l2[0]) == c :
						w.write(str(c)+" "+str(l2[1])+"\n")
					#dictionary[key] = int(l2[1])
						break
			read2.close()
				

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

# --------
# year_avg
# --------		

def year_avg (w):
	dict_1 = {}
	file_name = "movie_avg.txt"
	read_file = open(file_name, 'r')
	for line in read_file:
		l = line.split()
		dict_1[int(l[0])] = float(l[1])
	read_file.close()
	
	dict_2 = {}
	file_name = "movie_titles.txt"
	read_file = open(file_name, 'r')
	for line in read_file:
		l = line.split(',')
		m_id = int(l[0])
		y_id = str(l[1])
		try :
			v = dict_2[y_id]
			v[0] += dict_1[m_id]
			v[1] += 1
		except KeyError :
			dict_2[y_id] = [dict_1[m_id], 1]
	read_file.close()

	for k in dict_2 :
		v = dict_2[k]
		result = str(k) + " " + str(v[0]/v[1]) +"\n"
		w.write(result)

# ------
# offset
# ------

def offset (w):
	avg = 3.32740868729
	file_name = "temp.txt"
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
#year_avg (sys.stdout)
#avg (sys.stdin)
#offset (sys.stdout)
probe(sys.stdout)
