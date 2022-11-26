#sigal graboys 319009304
import csv
import numpy as np
import matplotlib.pyplot as plt


heuristic_cost = np.array(0)
path_cost = np.array(0)

with open("results/AStarRuns.txt", 'r') as file:
    csvreader = csv.reader(file)
    heuristic_cost = np.array(0)
    path_cost = np.array(0)

    for row in csvreader:
        r = row[0]
        path, cost, huristic = r.split('-')
        path_cost = np.append(path_cost, float(cost))
        heuristic_cost = np.append(heuristic_cost, float(huristic))

x = heuristic_cost
y = path_cost
plt.plot(x, y, 'o')
a, b = np.polyfit(x, y, 1)
plt.plot(x, a*x + b, color = 'red')
plt.xlabel('huristic cost(in hours)')
plt.ylabel('path cost (in hours)')
plt.title('huristic cost vs path cost')
plt.show()

