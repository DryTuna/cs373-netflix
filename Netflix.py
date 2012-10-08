# -------
# imports
# -------

import StringIO
import math


# customer_id => avg_rating
c_avg = {}
m_avg = {}

def Init():
    file_name = "caches/customer_avg.txt"
    read_file = open(file_name, 'r')
    for line in read_file :
        l = line.split()
        c_id = int(l[0])
        try :
            v = c_avg[c_id]
            v[0] += float(l[1])
        except KeyError :
                c_avg[c_id] = float(l[1])
    read_file.close()
    
    file_name = "caches/movie_avg.txt"
    read_file = open(file_name, 'r')
    for line in read_file :
        l = line.split()
        m_id = int(l[0])
        try :
            v = m_avg[m_id]
            v[0] += float(l[1])
        except KeyError :
                m_avg[m_id] = float(l[1])
    read_file.close()
    
def predict(custID, movieID):
    return c_avg[custID]

# ---------
# sqrt_diff
# ---------

def sqre_diff (x, y):
	return (x - y)**2

# ----
# RMSE
# ----

def RMSE (p, c):
	assert len(p) == len(c)
	assert len(c) > 0
	n = len(c)
	total = sum(map(sqre_diff, p, c), 0.0)
	return math.sqrt(total/n)    
