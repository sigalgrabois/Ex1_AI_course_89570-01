# sigal graboys 319009304
'''
This file should generate 100 random routing problems and write it to problems.cvs file
'''
import numpy as np
from ways import load_map_from_csv
import pandas as pd
import random
roads = load_map_from_csv()
junction_list = roads.junctions()

def problems_generate(roads):
    # create a list of source and target tuples
    source_list = []
    target_list = []
    token_junctions = []
    problems_num = 0

    # loop generating the sources
    while problems_num < 101:
        buffer_source_list = []
        # choose unselected junction
        # flag for regeneration of the chosen junction
        flag = 1
        while flag == 1:
            junction_index = random.randint(0, len(roads.junctions()) - 1)
            junction = junction_list[junction_index]
            if junction not in token_junctions:
                if len(junction.links) == 0 | len(junction.links) == 1:
                    continue
                token_junctions.append(junction)
                buffer_source_list.append(junction.index)
                flag = 0

        # find the links leading to connected junctions
        source_index = buffer_source_list[-1]
        links_list_source = junction_list[source_index].links

        i = 0
        flag = 0
        while i < 12:
            # check if the link is conncected to a junction
            if len(links_list_source) == 0:
                flag = 1
                break
            temp_link = random.choice(links_list_source)
            # check if the target is like the source
            if temp_link[1] == source_index:
                flag = 1
                break
            junction_check = junction_list[temp_link.target]
            if len(junction_check.links) == 0:
                flag = 1
                break
            source_index = temp_link[1]
            links_list_source = junction_list[source_index].links
            i = i + 1
        if source_index == buffer_source_list[-1]:
            continue
        if flag == 1:
            continue
        if (source_index == source_index + 1) or (source_index == source_index - 1):
            continue

        target_list.append(source_index)
        source_list.append(buffer_source_list[-1])
        problems_num = problems_num + 1
    # save the 100 random problems to a csv file
    problems = np.column_stack((source_list, target_list))
    pd_problems = pd.DataFrame(problems)
    pd_problems.to_csv('problems.csv', index=False, header=None)


if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1
    problems_generate(roads)
