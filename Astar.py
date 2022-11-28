# sigal graboys 319009304

from ways.tools import compute_distance
from best_first_graph_searches import a_star_best_first_graph_search
from load_roads import junction_list


# huristic function
def calculate_distance(lat1, lon1, lat2, lon2):
    return compute_distance(lat1, lon1, lat2, lon2)


def a_star_function(source, target, use=0):
    def huristic_function(lat1, lon1):
        distance = calculate_distance(lat1, lon1, junction_list[target].lat, junction_list[target].lon)
        return distance / 110

    node_path = a_star_best_first_graph_search(source, target, use, huristic_function)
    if use == 0:
        path_index = []
        for node in node_path:
            path_index.append(node.index)
        return path_index
    return node_path
