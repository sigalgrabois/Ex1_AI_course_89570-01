#sigal graboys 319009304
''' this class is a priority queue that is used in the different searches '''
class PriorityQueue:

    def __init__(self):
        self.frontier = []

    def sort(self):
        self.frontier.sort(key=lambda node: node.path_cost_g_function)

    def sort_heuristic(self):
        self.frontier.sort(key=lambda node: node.path_g_h_function)

    def insert(self, node):
        self.frontier.append(node)

    def append(self):
        self.append()

    def pop(self):
        return self.frontier.pop(0)

    def not_empty(self):
        if len(self.frontier) == 0:
            return False
        return True

    def is_node_in_frontier(self, node):
        for frontierNode in self.frontier:
            if node.index == frontierNode.index:
                return True

    def swap_nodes(self, node):
        for frontierNode in self.frontier:
            if node.index == frontierNode.index:
                if node.path_cost_g_function < frontierNode.path_cost_g_function:
                    self.frontier.remove(frontierNode)
                    self.frontier.append(node)

    def huristic_swap_nodes(self, node):
        for frontierNode in self.frontier:
            if node.index == frontierNode.index:
                if node.path_g_h_function < frontierNode.path_g_h_function:
                    self.frontier.remove(frontierNode)
                    self.frontier.append(node)
