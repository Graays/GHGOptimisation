import csv

def csvreader(file):
    res = []
    with open(file, newline='') as data:
        datasets = csv.reader(data, delimiter=' ', quotechar='|')
        for row in datasets:
            res += [[row[0].split(',')[0]] + [int(x) for x in row[0].split(',')[1:]]]
        return res