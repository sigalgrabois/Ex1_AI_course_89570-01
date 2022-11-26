
from best_first_graph_searches import a_star_best_first_graph_search
from ways import compute_distance


# huristic function
def calculate_distance(lat1, lon1, lat2, lon2):
    return compute_distance(lat1, lon1, lat2, lon2)


def huristic_function(lat1=0, lon1=0, lat2=0, lon2=0):
    distance = calculate_distance(lat1, lon1, lat2, lon2)
    return distance / 110


def a_star_function(source, target, use=0, h=lambda x, y, z, w: huristic_function(x, y, z, w)):
    node_path = a_star_best_first_graph_search(source, target, use, h)
    return node_path

