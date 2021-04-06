import csv
import time

def resolution(catalog, services, duration):

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
        return catalog[id][1] + n * catalog[id][2]

    def condservice(i):
        return services[i][1:4]

    def condserveur(i):
        return catalog[i][3:6]

    servicelen = len(services)
    serverlen = len(catalog)
    sizeserver = range(serverlen)
    sizeservice = range(servicelen)


    def couples():
        result = []
        for i in sizeservice:
            for j in sizeserver:

                if verifcond(condservice(i),condserveur(j)):
                    result.append([i,j])

        return(result)




    def optimisation(data,time,serv):
        best = []
        opti = 500000000
        for i in range(len(data)):
            if data[i][0] == serv:
                temp = bilanc(data[i][1],time)
                if temp <= opti:
                    opti = bilanc(data[i][1],time)

                    best = data[i]
        return(best)


    data = couples()
    output = []

    for i in sizeservice:
        temp = optimisation(data,duration,i)
        output.append([catalog[temp[1]][0],services[temp[0]][0]])

    return(output)
