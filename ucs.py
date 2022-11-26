
from best_first_graph_searches import best_first_graph_search


def ucs_function(source, target, use=0):
    node_path = best_first_graph_search(source, target, use)
    return node_path



