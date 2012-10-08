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
    
    file_name = "caches/movies_avg.txt"
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


def CalcRMSE():
    file_name = "probe.txt"
    read_file = open(file_name, 'r')
    m = 0
    #movie_id => [list of customers who reviewed the movie]
    dict = {}
    for line in read_file :
        if ":" in line:
            m = int(line[:-1])
        else:
            c_id = int(line)
            try :
                v = c_avg[c_id]
                v[0] += float(l[1])
            except KeyError :
                    c_avg[c_id] = float(l[1])
    read_file.close()
    
    