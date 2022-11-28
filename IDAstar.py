# sigal graboys 319009304
from numpy import inf
import Node
from Node import huristic_function
from load_roads import junction_list
new_limit = 0


# implement the limited dfs for nodes
def limited_dfs(node, target, f_limit):
    global new_limit
    new_f = node.path_g_h_function
    if new_f > f_limit:
        new_limit = min(new_f, new_limit)
        return None, new_limit
    if node.index == target:
        return node.finding_path(), node.path_g_h_function
    for child in node.expand():
        solution, child_f_limit = limited_dfs(child, target, f_limit)
        if solution is not None:
            return solution, child_f_limit
        f_limit = min(f_limit, child_f_limit)
    return None, f_limit


def ida_star_function(source, target):
    global new_limit
    node = Node.Node(source, target)
    source_junction = junction_list[source]
    target_junction = junction_list[target]
    new_limit = huristic_function(source_junction.lat, source_junction.lon, target_junction.lat, target_junction.lon)
    while True:
        print(new_limit)
        f_limit = new_limit
        new_limit = float('inf')
        solution, f_limit = limited_dfs(node, target, f_limit)
        if solution is not None:
            return solution
        if f_limit == inf:
            return None
