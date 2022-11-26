#sigal graboys 319009304
import Node
from PriorityQueue import PriorityQueue



def best_first_graph_search(source, target, use):
    node = Node.Node(source,target)
    frontier = PriorityQueue()
    frontier.insert(node)
    closed_list = set()
    while frontier.not_empty():
        frontier.sort()
        node = frontier.pop()
        if node.index == target:
            del node.path[-1]
            index = target
            parent = node.path[-1]
            path = node.update_path(node.finding_path())
            path_cost = node.path_cost_g_function + node.cost_function(node.path[-1].index, target)
            new_node = Node.Node(index,target, parent, path, path_cost)
            node.path.append(new_node)
            if use == 0:
                return node.path
            if use == 1:
                return new_node.path_cost_g_function
        closed_list.add(node)
        for child in node.expand():
            if child.index not in [c.index for c in closed_list] and child not in frontier.frontier:
                frontier.insert(child)
            frontier.swap_nodes(child)
    return None


def a_star_best_first_graph_search(source, target, use, h):
    node = Node.Node(source,target)
    frontier = PriorityQueue()
    frontier.insert(node)
    closed_list = set()
    while frontier.not_empty():
        frontier.sort_heuristic()
        node = frontier.pop()
        if node.index == target:
            del node.path[-1]
            index = target
            parent = node.path[-1]
            path = node.update_path(node.finding_path())
            path_cost = node.path_cost_g_function + node.cost_function(node.path[-1].index, target)
            path_huristic_cost = node.path_cost_g_function +node.cost_function(node.path[-1].index, target) + 0 # h function between juntction to it self since we reached the distanation.

            new_node = Node.Node(index,target, parent, path, path_cost, path_huristic_cost)
            node.path.append(new_node)
            if use == 0:
                return node.path
            if use == 1:
                return new_node.path_g_h_function
            if use == 2:
                return h(Node.junction_list[source].lat, Node.junction_list[source].lon)
        closed_list.add(node)
        for child in node.expand():
            if child.index not in [c.index for c in closed_list] and child not in frontier.frontier:
                frontier.insert(child)
            frontier.huristic_swap_nodes(child)
    return None
