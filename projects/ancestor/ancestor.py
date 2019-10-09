from util import Stack,Queue 

def retrieve_ancestors(ancestors,node):
    ancestor_nodes = []
    for edge in ancestors:
        if edge[1] is node:
            ancestor_nodes.append(edge[0])
    return ancestor_nodes




def earliest_ancestor(ancestors, starting_node):
    stack = Stack()
    stack.push([starting_node])
    visited.set()
    longest_chain = []

    while stack.size() > 0:
        path = stack.pop()
        current_node = path[-1]

        if current_node not in visited:
            visited.add(current_node)
        
        if not retrieve_ancestors(ancestors,current_node):
            if len(path) > len(longest_chain):
                longest_chain = path
            elif len(path) == len(longest_chain):
                if path[-1] < longest_chain[-1]:
                    longest_chain = path
        
        else:
            for next_node in retrieve_ancestors(ancestors, current_node):
                new_path = list(path)
                new_path.append(next_node)
                stack.push(new_path)
    
    result = longest_chain.pop()
    if result is starting_node:
        result = -1
    
    return result
