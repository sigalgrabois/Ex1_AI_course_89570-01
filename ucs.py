# sigal graboys 319009304
from best_first_graph_searches import best_first_graph_search


def ucs_function(source, target, use=0):
    # implrmrnt best graph search with cost function
    node_path = best_first_graph_search(source, target, use)
    if (use == 0):
        path_index = []
        for node in node_path:
            path_index.append(node.index)
        return path_index
    return node_path
