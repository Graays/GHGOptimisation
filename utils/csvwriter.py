import csv
import time

def csvwriter(result,method,):
    res = []

    c = csv.writer(open("output/result-{}-meth{}.csv".format(time.strftime("%m-%H%M", time.gmtime(time.time())), method), "w",newline='\n'))
    for i in result:
        c.writerow(i)

    return(res)