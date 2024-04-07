# Copyright (c) [2024] [Manisha Garg]
# Custom License: See LICENSE file in the project root for the full license terms.


from copy import deepcopy
import math
import numpy

def alpha(
    number_of_vertices, 
    shortest_len_mat, 
    edge_added, 
    distance ):
    '''
    We calculate what is the shortest length matrix for any graph, G
    We have vertices, V(G)
    For middle graph V(G) can change in the case we add or remove equivalence classes
    We have edges of the graph

    Args:
    number_of_vertices: |V(G)|
    shortest_len_mat: It is SLM in the previous step (i.e, for the parent)
    edge_added: edge we are adding = (x,y)
    '''
    x = edge_added[0]
    y = edge_added[1]
    shortest_len_mat = deepcopy(shortest_len_mat)
    #distance = 0 if equivalence_class_merged else 1 
    # It means we are deleting a class and hence two vertices.
    #  
    # (0 red in and 2 green in ) and (1 red out and 3 )
    for u in range(number_of_vertices):
        for v in range(u+1, number_of_vertices):
            value_1 = shortest_len_mat[u,v]
            value_2 = shortest_len_mat[u,x] + distance + shortest_len_mat[v,y]
            value_3 = shortest_len_mat[u,y] + distance + shortest_len_mat[v,x]
            min_val = min(value_1, value_2, value_3)
            shortest_len_mat[u,v] = min_val
            shortest_len_mat[v,u] = min_val
    return shortest_len_mat


def beta(
    number_of_vertices, 
    cycle_len_list, 
    shortest_len_mat, 
    edge_added,
    distance):

    x = edge_added[0]
    y = edge_added[1]
    shortest_len_mat = deepcopy(shortest_len_mat)
    cycle_len_list = deepcopy(cycle_len_list)
    
    for u in range(number_of_vertices):
        value_1 = cycle_len_list[u]
        value_2 = shortest_len_mat[u,x] + distance + shortest_len_mat[u,y]
        # Discuss with Igor
        min_val = min(value_1, value_2)
        cycle_len_list[u] = min_val
        
    return cycle_len_list

def girth(
    number_of_vertices, 
    edges_added, 
    shortest_len_mat, 
    cycle_len_list,
    action
    
    ):

    shortest_len_mat = deepcopy(shortest_len_mat)
    cycle_len_list = deepcopy(cycle_len_list)
    distance = 1
    distance_actual_link = 0.5
    
    if action == []:
        # We are in graph A or B and Not middle graph
        for edge in edges_added:
            assert(len(edges_added)==1)
            cycle_len_list = beta(number_of_vertices, cycle_len_list, shortest_len_mat, edge, 1)
            shortest_len_mat = alpha(number_of_vertices, shortest_len_mat, edge,  1)
    
    elif action[0] == 'nothingHappened':
        # Middle graph
        return [shortest_len_mat, cycle_len_list]
    
    elif action[0]=='addEdge':
        if(len(edges_added)!=0):
            for edge in edges_added:
                cycle_len_list = beta(number_of_vertices, cycle_len_list, shortest_len_mat, edge, distance_actual_link)
                shortest_len_mat = alpha(number_of_vertices, shortest_len_mat, edge,  distance_actual_link)

    elif action[0] == 'addClass':
        number_of_cols = len(shortest_len_mat)
        if number_of_cols == 0:
            raise ValueError("number_of_cols should not be 0, initialize SLM to be order m+n")
            #shortest_len_mat = numpy.matrix(numpy.ones((2,2)) * numpy.inf)
            #numpy.fill_diagonal(shortest_len_mat, 0)
            #cycle_len_list = numpy.array(numpy.ones(2) * numpy.inf)
        else:
            #adding rows and cols to shortest len matrix
            inf_array = numpy.ones(number_of_cols)*numpy.inf
            shortest_len_mat = numpy.append(shortest_len_mat, [inf_array], axis=0)
            shortest_len_mat = numpy.append(shortest_len_mat, [inf_array], axis=0)
            s = numpy.shape(shortest_len_mat)
            shortest_len_mat = numpy.column_stack((shortest_len_mat, numpy.ones(s[0])*numpy.inf))
            shortest_len_mat = numpy.column_stack((shortest_len_mat, numpy.ones(s[0])*numpy.inf)) 
            numpy.fill_diagonal(shortest_len_mat, 0)
            #adding new cols to cycle len matrix
            cycle_len_list = numpy.append(cycle_len_list, numpy.ones(2)*numpy.inf, axis=0)
            number_of_vertices = len(shortest_len_mat)
        for edge in edges_added:
            cycle_len_list = beta(number_of_vertices, cycle_len_list, 
                shortest_len_mat, edge,  distance_actual_link)
            shortest_len_mat = alpha(number_of_vertices, shortest_len_mat, 
                edge,  distance_actual_link)
    
    elif action[0] == 'mergeWithInversion' or action[0] == 'mergeWithoutInversion':
        distance_merge = 0
        assert(len(edges_added) == 2)
        for edge in edges_added:
            cycle_len_list = beta(number_of_vertices, cycle_len_list, 
                shortest_len_mat, edge,  distance_merge)
            shortest_len_mat = alpha(number_of_vertices, shortest_len_mat, 
                edge,  distance_merge)
    else:
        print("This should not happen")
    
    return [shortest_len_mat, cycle_len_list]