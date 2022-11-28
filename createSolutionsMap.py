# sigal graboys 319009304
import csv
from random import random

from matplotlib import pyplot as plt

import IDAstar
from ways.draw import plot_path
from load_roads import roads
import numpy as np


    # choose a 10 random problems
    # random_ten_problems ()
    # read the problems from the csv file
# with open('ten_problems.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#         source = int(row[0])
#         target = int(row[1])
#         # run the IDAstar algorithm
#         path = IDAstar.ida_star_function(source, target)
#         path_index = []
#         for node_junc in path:
#             path_index.append(node_junc.index)
#         # plot the path
#         plot_path(roads, path_index)
#         plt.show()


# def random_ten_problems():
#     random_problems = []
#     # create a list of source and target
#     with open('problems.csv', 'r') as f:
#         reader = csv.reader(f)
#         rows = np.random.randint(100, size=10)
#         ind = 0
#
#         for row in reader:
#             random_problems.append(row)
#             if ind in rows:
#                 source = int(row[0])
#                 target = int(row[1])
#                 random_problems.append([source, target])
#             ind += 1
#
#     # save the 10 random problems to a csv file
#     ten_problems = open('ten_problems.csv', 'w', newline='')
#     writer = csv.writer(ten_problems, delimiter=',')
#     cvs_reader = csv.writer(ten_problems)
#     for problem in random_problems:
#         writer.writerow([f"{problem[0]} {problem[1]}"])
#     ten_problems.close()
#

source = 39598

target = 39604



path = IDAstar.ida_star_function(source, target)
path_index = []
for junction in path:
    path_index.append(junction.index)

plot_path(roads, path_index)
plt.show()
