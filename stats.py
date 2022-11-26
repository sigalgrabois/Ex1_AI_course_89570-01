'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''
import collections
from collections import namedtuple
from ways import load_map_from_csv
from ways.info import ROAD_TYPES

def calcMinMaxBranch(roads):
    # init max and min branch factor to be the first element
    for junction in roads.junctions():
        max_branch_factor = len(junction[3])
        min_branch_factor = len(junction[3])
        break
    # calc branching factors - min and max
    for junction in roads.junctions():
        if len(junction[3]) < min_branch_factor:
            min_branch_factor = len(junction[3])
        if len(junction[3]) > max_branch_factor:
            max_branch_factor = len(junction[3])
    return  max_branch_factor, min_branch_factor

def calcLinkDistance (linksList):
    # init params
    sumLinkDistance = 0
    for link in linksList:
        max = link[2]
        min = link[2]
        break

    # calc avg
    for link in linksList:
        sumLinkDistance += link[2]
        # calc max
        if max < link[2]:
            max = link[2]
        # calc min
        if min > link[2]:
            min = link[2]
    avg = (sumLinkDistance / len(linksList))
    return max, min, avg

def map_statistics(roads):
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    # creating links list for all the juctions
    linksList = [];
    # link type histogram:
    high_way_type_list = []
    # calc number of juctions
    number_junctions = len(roads.junctions())
    for link in roads.iterlinks():
        linksList.append(link);
        high_way_type_list.append(ROAD_TYPES[link.highway_type])
    # calc the branching factors
    max_branch_factor, min_branch_factor = calcMinMaxBranch(roads)
    # link distance
    max_link_distance, min_link_distance, avg_link_distance = calcLinkDistance(linksList)

    histogram = collections.Counter(high_way_type_list)
    sorted_dict = collections.OrderedDict(histogram)
    return {
        'Number of junctions': number_junctions,
        'Number of links': len(linksList),
        'Outgoing branching factor': Stat(max=max_branch_factor, min=min_branch_factor,
                                          avg=(len(linksList)) / number_junctions),
        'Link distance': Stat(max=max_link_distance, min=min_link_distance, avg=avg_link_distance),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram': histogram,  # tip: use collections.Counter
    }

def print_stats():
    # change
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1
    print_stats()
