import csv

from main import find_ucs_rout

# loading the problems to two different lists

with open("problems.csv", 'r') as file:
    csvreader = csv.reader(file)
    source = []
    target = []
    paths = []

    for row in csvreader:
        source.append(int(row[0]))
        target.append(int(row[1]))

with open("results/UCSRuns.txt", 'w') as file:
    for i in range(101):
        ucs_path = find_ucs_rout(source[i], target[i])
        cost_path = find_ucs_rout(source[i], target[i], 1)
        # take 4 digits after the decimal point in cost_path
        cost_path = round(cost_path, 4)
        for node in ucs_path:
            file.write("%s " % node.index)
        file.write(" - ")
        file.write("%s" % cost_path)

        file.write("\n")




