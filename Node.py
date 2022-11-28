# sigal graboys 319009304
import load_roads
from ways.info import SPEED_RANGES
from ways.tools import compute_distance
'''this class represent a node in the roads map'''

# huristic function for Astar and IDAstar
def huristic_function(lat1=0, lon1=0, lat2=0, lon2=0):
    distance = compute_distance(lat1, lon1, lat2, lon2)
    return distance / 110


class Node:
    def __init__(self, index, target=0, parent=None, path=[], path_cost=0, heuristic_cost=0):
        self.index = index
        self.parent = parent
        self.path = path
        self.path_cost_g_function = path_cost
        self.path_g_h_function = heuristic_cost
        self.target = target
        self.target_lat, self.target_lon = load_roads.junction_list[target].lat, load_roads.junction_list[target].lon
# expand the node and return the children list
    def expand(self) -> []:
        children_list = []
        junction = load_roads.junction_list[self.index]
        for link in junction.links:
            index = link.target
            parent = self
            path = self.update_path(self.finding_path())
            path_cost = self.path_cost_g_function + self.cost_function(self.index, link[1])
            junction_son = load_roads.junction_list[index]
            total_huristic_cost = path_cost + huristic_function(junction_son.lat,
                                                                junction_son.lon, self.target_lat,
                                                                self.target_lon)
            new_node = Node(index, self.target, parent, path, path_cost, total_huristic_cost)
            children_list.append(new_node)
        return children_list
# used to set each node's path
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

# used to calculate the cost of each node (g function)
    def cost_function(self, source, target):

        if (self.index or source) == target:
            return 0
        # finding the distance
        source_junction = load_roads.junction_list[source]
        links_connceted_to_source = source_junction.links
        for link in links_connceted_to_source:
            if link[1] == target:
                target_link = link
                break

        # finding the speed
        speed = (SPEED_RANGES[link.highway_type][1])
        return ((target_link.distance) / (1000)) / speed
