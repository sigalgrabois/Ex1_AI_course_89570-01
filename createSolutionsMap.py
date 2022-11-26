import csv
import random

import matplotlib.pyplot as plt

import IDAstar
from ways import draw
from Node import roads



# loading the problems to two different lists
def create_map():
    with open("problems.csv", 'r') as file:
        csvreader = csv.reader(file)
        source = []
        target = []
        paths = []

        for row in csvreader:
            source.append(int(row[0]))
            target.append(int(row[1]))

        # for i in range(10):
        choice = random.randint(0, len(source) - 1)

    path = IDAstar.ida_star_function(source[choice], target[choice])
    draw.plot_path(roads, path)
    plot_path(roads, path)



