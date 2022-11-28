#sigal graboys 319009304
import csv
from main import find_ucs_rout, find_astar_route
import time



# loading the problems to two different lists

with open("ten_problems.csv", 'r') as file:
    csvreader = csv.reader(file)
    source = []
    target = []
    paths = []

    for row in csvreader:
        source.append(int(row[0]))
        target.append(int(row[1]))
UCS_time_sum = 0
# run UCS on the 10 random problems
for i in range(10):
    start = time.time()
    ucs_path = find_ucs_rout(source[i], target[i])
    end = time.time()
    UCS_time_sum += end - start
avg_UCS_time = UCS_time_sum/10
print ("avg UCS time: ", avg_UCS_time, "\n")

# run A* on the 10 random problems
A_star_time_sum = 0
for i in range(10):
    start = time.time()
    astar_path = find_astar_route(source[i], target[i])
    end = time.time()
    A_star_time_sum += end - start
AVG_A_star_time = A_star_time_sum/10
print ("avg A* time: ", AVG_A_star_time, "\n")

 # run IDA* on the 10 random problems
IDA_star_time_sum = 0
for i in range(10):
    start = time.time()
    ida_star_path = find_astar_route(source[i], target[i])
    end = time.time()
    IDA_star_time_sum += end - start
AVG_IDA_star_time = IDA_star_time_sum/10
print ("avg IDA* time: ", AVG_IDA_star_time, "\n")

