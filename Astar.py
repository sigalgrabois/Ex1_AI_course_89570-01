
from ways.tools import compute_distance
from main import huristic_function
from best_first_graph_searches import a_star_best_first_graph_search
from Node import junction_list



# huristic function
def calculate_distance(lat1, lon1, lat2, lon2):
    return compute_distance(lat1, lon1, lat2, lon2)


def a_star_function(source, target, use=0, h=lambda x, y, z, w,t: huristic_function(x, y, z, w)):

    node_path = a_star_best_first_graph_search(source, target, use, h(x=0, y=0, z=junction_list[target].lat, w=junction_list[target].lon))
    return node_path

