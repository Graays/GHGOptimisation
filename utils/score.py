from utils import csvreader as csv

def score(file,duration):

    score = 0

    catalog = [['tiny1',2000,100],
               ['tiny2', 3000, 150],
               ['tiny3', 2500, 100],
               ['classic1', 6000, 1000],
               ['classic2', 11000, 2000],
               ['classic3', 6000, 3000],
               ['classic4', 15000, 3500],
               ['classic5', 12000, 3000],
               ['classic6', 11500, 3000],
               ['large1', 25000, 10000],
               ['large2', 25000, 8000],
               ['large3', 40000, 15000],
               ['storage1', 13000, 600],
               ['storage2', 10000, 300],
               ['storage3', 15000, 1000],
               ['compute1', 12000, 4000],
               ['compute2', 13000, 4500],
               ['compute3', 16200, 6000],
               ['memory1', 10000, 1000],
               ['memory2', 14000, 1300]]
    output = csv.csvreader(file)
    print(output)
    for i in range(len(output)):
        for j in range(len(catalog)):
            if output[i][0] == catalog[j][0]:
                score += catalog[j][1] + duration * catalog[j][2]

    return score
