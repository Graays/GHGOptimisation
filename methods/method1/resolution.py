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


    def couples(service,server):
        result = []
        for i in range(len(service)):
            for j in range(len(server)):

                if verifcond(condservice(i),condserveur(j)):
                    result.append([i,j])

        return(result)




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


    data = couples(services, catalog)
    output = []

    for i in range(len(services)):
        temp = optimisation(data,duration,i)
        print(temp)
        output.append([catalog[temp[1]][0],services[temp[0]][0]])

    return(output)
