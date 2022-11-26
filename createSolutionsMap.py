import csv
from random import random

from matplotlib import pyplot as plt

import IDAstar
from ways.draw import plot_path
from load_roads import roads
import numpy as np

# def create_map ():
#         import matplotlib.pyplot as plt
#         with open("problems.csv", 'r') as file:
#                 csvreader = csv.reader(file)
#                 source = []
#                 target = []
#                 paths = []
#                 for row in csvreader:
#                         source.append(int(row[0]))
#                         target.append(int(row[1]))
#                         path =  IDAstar.IDAstar(int(row[0]), int(row[1]))
#                         plot_path(roads, path)
#                         plt.show()

# loading the problems to two different lists

#
# choice = random.randint(0, len(source) - 1)
source = 145001
target = 145018
path = IDAstar.ida_star_function(source, target)
path_index = []
for junction in path:
    path_index.append(junction.index)

plot_path(roads, path_index)
plt.show()
