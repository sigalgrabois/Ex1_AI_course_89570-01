import csv

import numpy as np
from matplotlib import pyplot as plt
from load_roads import roads
import IDAstar
from ways.draw import plot_path

# not have been used - since we told we can choose 10 problems with not long runtime
def random_ten_problems():
    random_problems = []
    # create a list of source and target
    with open('problems.csv', 'r') as f:
        reader = csv.reader(f)
        rows = np.random.randint(100, size=10)
        i = 0
        for row in reader:
            random_problems.append(row)
            if i in rows:
                source = int(row[0])
                target = int(row[1])
                random_problems.append([source, target])
            i += 1

    # save the 10 random problems to a csv file
    ten_problems = open('ten_problems.csv', 'w', newline='')
    writer = csv.writer(ten_problems, delimiter=',')
    cvs_reader = csv.writer(ten_problems)
    for problem in random_problems:
        writer.writerow([f"{problem[0]} {problem[1]}"])
    ten_problems.close()

    # random_problems()

source = []
target = []

# loading the 10 problems to two different lists
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
