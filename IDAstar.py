from numpy import inf

import Node


# implement the limited dfs for nodes
def limited_dfs(node, target, f_limit):
    new_f = node.path_g_h_function
    if new_f > f_limit:
        new_limit = min(f_limit, new_f)
        return None, new_limit
    if node.index == target:
        return node.finding_path(), node.path_g_h_function
    for child in node.expand():
        solution, child_f_limit = limited_dfs(child, target, f_limit)
        if solution is not None:
            return solution, child_f_limit
        f_limit = min(f_limit, child_f_limit)
    return None, f_limit


def ida_star_function(source, target, use, huristic_function):
    node = Node.Node(source)
    source_junction = Node.junction_list[source]
    target_junction = Node.junction_list[target]
    new_limit = huristic_function(source_junction.lat, source_junction.lon, target_junction.lat, target_junction.lon)
    while True:
        f_limit = new_limit
        new_limit = inf
        solution, f_limit = limited_dfs(node, target, f_limit)
        if solution is not None:
            return solution
        if f_limit == inf:
            return None
