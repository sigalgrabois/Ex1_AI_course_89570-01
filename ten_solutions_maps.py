import csv
from matplotlib import pyplot as plt
from load_roads import roads
import IDAstar
from ways.draw import plot_path

source = []
target = []
paths = []
# loading the problems to two different lists
with open("ten_problems.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        source.append(int(row[0]))
        target.append(int(row[1]))

for i in range(10):
    path = IDAstar.ida_star_function(source[i], target[i])
    path_index = []
    for node_junc in path:
        path_index.append(node_junc.index)
    # plot the path
    plot_path(roads, path_index)
    plt.show()
