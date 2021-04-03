import numpy as np
import csv
c = csv.writer(open("../../../../BEMa321/sortie6.csv", "w", newline='\n'))
servers = """tiny1,2000,100,200,4,1
tiny2,3000,150,500,8,1
tiny3,2500,100,500,6,1
classic1,6000,1000,1000,16,8
classic2,11000,2000,2000,32,16
classic3,6000,3000,2000,32,16
classic4,15000,3500,4000,32,32
classic5,12000,3000,1000,64,24
classic6,11500,3000,4000,16,24
large1,25000,10000,10000,64,64
large2,25000,8000,8000,32,40
large3,40000,15000,20000,128,80
storage1,13000,600,20000,8,4
storage2,10000,300,10000,8,1
storage3,15000,1000,25000,8,4
compute1,12000,4000,1000,16,40
compute2,13000,4500,500,16,48
compute3,16200,6000,1000,16,64
memory1,10000,1000,500,32,4
memory2,14000,1300,1000,128,8"""
server = []
for i in servers.splitlines()[1:]:
    server += [[i.split(',')[0]] + [int(x) for x in i.split(',')[1:]]]

services = """"""

service = []
st = services.splitlines()
years = int(st[0])
for i in st[1:]:
    service += [[i.split(',')[0]] + [int(x) for x in i.split(',')[1:]]]

def verifcond(a,b):
    result = False
    for i in range(len(a)):
        if a[i] <= b[i]:
            result = True
            continue
        else:
            return False
    return result

def bilanc(id,n):
    return server[id][1] + n * server[id][2]

def condservice(i):
    return service[i][1:4]
def condserveur(i):
    return server[i][3:6]

result = []


def couples(service,server):
    for i in range(len(service)):
        for j in range(len(server)):
            if verifcond(condservice(i),condserveur(j)):
                result.append([i,j])

    return(result)


data = couples(service,server)

def optimisation(data,time,serv):
    solution = []
    best = []
    opti = 500000000
    for i in range(len(data)):
        if data[i][0] == serv:
            solution.append([i,bilanc(data[i][1],time)])
            if bilanc(data[i][1],time) <= opti:
                opti = bilanc(data[i][1],time)

                best = data[i]
    return(best)


print(optimisation(data,5,0))

for i in range(len(service)):

    c.writerow([server[optimisation(data,5,i)[1]][0],service[optimisation(data,5,i)[0]][0]])


