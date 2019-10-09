from util import Stack,Queue 

def retrieve_ancestors(ancestors,node):
    ancestor_nodes = []
    for edge in ancestors:
        if edge[1] is node:
            ancestor_nodes.append(edge[0])
    return ancestor_nodes




def earliest_ancestor(ancestors, starting_node):
    pass