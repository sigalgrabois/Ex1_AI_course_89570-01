from ways import load_map_from_csv
from ways.info import SPEED_RANGES
import main

roads = (load_map_from_csv())
junction_list = roads.junctions()


class Node:
    def __init__(self, index, parent=None, path=[], path_cost=0, heuristic_cost=0):
        self.index = index
        self.parent = parent
        self.path = path
        self.path_cost_g_function = path_cost
        self.path_g_h_function = heuristic_cost

    def expand(self) -> []:
        children_list = []
        junction = junction_list[self.index]
        for link in junction.links:
            index = link.target
            parent = self
            path = self.update_path(self.finding_path())
            path_cost = self.path_cost_g_function + self.cost_function(self.index, link[1])
            junction_son = junction_list[index]
            total_huristic_cost = self.path_cost_g_function + main.huristic_function(lat1=junction_son.lat,
                                                                                     lon1=junction_son.lon,
                                                                                     )
            new_node = Node(index, parent, path, path_cost, total_huristic_cost)
            children_list.append(new_node)
        return children_list

    def finding_path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def update_path(self, path_parent):
        path_list = path_parent
        path_list.append(self)
        return path_list

    def update_heuristic_cost(self, heuristic_cost):
        self.path_g_h_function = self.path_g_h_function + heuristic_cost

    def cost_function(self, source, target):

        if (self.index or source) == target:
            return 0
        # finding the distance
        source_junction = junction_list[source]
        links_connceted_to_source = source_junction.links
        for link in links_connceted_to_source:
            if link[1] == target:
                target_link = link
                break

        # finding the speed
        speed = (SPEED_RANGES[link.highway_type][1])
        return ((target_link.distance) / (1000)) / speed
