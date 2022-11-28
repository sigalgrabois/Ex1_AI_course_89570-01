# sigal graboys 319009304
import csv

from main import find_astar_route

# loading the problems to two different lists

with open("problems.csv", 'r') as file:
    csvreader = csv.reader(file)
    source = []
    target = []
    paths = []

    for row in csvreader:
        source.append(int(row[0]))
        target.append(int(row[1]))

with open("results/AStarRuns.txt", 'w') as file:
    for i in range(101):
        astar_path = find_astar_route(source[i], target[i])
        cost_path = find_astar_route(source[i], target[i], 1)
        # take 4 digits after the decimal point in cost_path
        cost_path = round(cost_path, 4)
        huristic_path = find_astar_route(source[i], target[i], 2)
        # take 4 digits after the decimal point in huristic_path
        huristic_path = round(huristic_path, 4)

        for node in astar_path:
            file.write("%s " % node.index)

        file.write('-')
        file.write("%s" % cost_path)
        file.write('-')
        file.write("%s" % huristic_path)

        file.write("\n")
