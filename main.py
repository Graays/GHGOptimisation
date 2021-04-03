import time
import subprocess
import sys

from utils.csvreader import *

req = 1

while(not(req >=1 and req <= 6)):
    req = input("Select a dataset between 1 and 6 : \n")
    try:
        req = int(req)
    except:
        print("Valuetype 'int' expected")
        req = 0

meth = 0
while(not(meth >=1 and meth <= 1)):
    req = input("Select a method between 1 and # : \n")
    try:
        meth = int(req)
    except:
        print("Valuetype 'int' expected")
        meth = 0

# Starting the clock
tic = time.time()

# "servers" list represents the catalog of available servers with specs
servers = csvreader('data/servers_catalog.csv')

# "requests list represents the list of services that needs to be sorted through servers
requests = csvreader('data/ctstfr0280_input_{}.csv'.format(req))



print(subprocess.run([sys.executable,'methods/method{}/resolution.py'.format(meth)]))


toc = time.time()
print("Time elapsed : {} seconds".format(toc-tic))