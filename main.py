import time

from utils.csvreader import *
from utils.csvwriter import *
from utils.score import *

import methods.method1.resolution

req = 3
while(not(req >=1 and req <= 6)):
    req = input("Select a dataset between 1 and 6 : \n")
    try:
        req = int(req)
    except:
        print("Valuetype 'int' expected")
        req = 0

meth = 1
while(not(meth >=1 and meth <= 1)):
    req = input("Select a method between 1 and # : \n")
    try:
        meth = int(req)
    except:
        print("Valuetype 'int' expected")
        meth = 0

# Starting the clock


# "servers" list represents the catalog of available servers with specs
catalog = csvreader('data/servers_catalog.csv')

tic = time.time()

# "requests list represents the list of services that needs to be sorted through servers
temp = csvreader('data/ctstfr0280_input_{}.csv'.format(req))
services = temp[1:]
duration = int(temp[0][0])
del temp



csvwriter(eval("methods.method{}.resolution.resolution(catalog, services, duration)".format(meth)), meth)

toc = time.time()
print("Time elapsed : {} seconds".format(toc-tic))



