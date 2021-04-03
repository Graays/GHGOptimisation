import time

from utils.csvreader import *

req = 0
while(not(req >=1 and req <= 6)):
    req = input("Select a dataset between 1 and 6 : \n")
    try:
        req = int(req)
    except:
        print("Valuetype 'int' expected")
        req = 0

req = str(req)
# Starting the clock
tic = time.time()

# "servers" list represents the catalog of available servers with specs
servers = csvreader('data/servers_catalog.csv')

# "requests list represents the list of services that needs to be sorted through servers
requests = csvreader('data/ctstfr0280_input_{}.csv'.format(req))

print(requests)

toc = time.time()
print("Time elapsed : {} seconds".format(toc-tic))