# Copyright (c) [2024] [Manisha Garg]
# Custom License: See LICENSE file in the project root for the full license terms.

from copy import deepcopy 
import numpy, math


def adequacy_condition(parent_node, graph_vertices):
    
    edges_to_be_considered_for_the_cell = deepcopy(parent_node.edges_to_be_considered_for_the_cell) #lexicograhic order
    cells_created_so_far      = deepcopy(parent_node.cells_created_so_far)
    child_edges_considered    = deepcopy(parent_node.edges_considered)
    child_A_last_vertex_used  = deepcopy(parent_node.A_last_vertex_used)
    child_B_last_vertex_used  = deepcopy(parent_node.B_last_vertex_used)
    child_A_last_vertex_added = deepcopy(parent_node.A_last_vertex_added)
    child_B_last_vertex_added = deepcopy(parent_node.B_last_vertex_added)
    A_list_of_vertices_used   = deepcopy(parent_node.A_list_of_vertices_used) # used_vertices
    B_list_of_vertices_used   = deepcopy(parent_node.B_list_of_vertices_used)
    child_unused_edges = deepcopy(parent_node.unused_edges) # edges outside the range

    '''
        We will create children based on 
        1. adequacy condition 
        2. if they satisfy equivalence condition and 
        3. Girth condition
        4. leafage condition
    '''

        
    # All edges created so far are used in creation of cells
    # A check could be that the last vertex added is the last vetex used
        
        
    if(len(edges_to_be_considered_for_the_cell) == 0):
            
        '''
        For this case, 
        first we will add edges to the edges_to_be_considered so that we can draw first edge for the cell
        Test 1: last vertex used should be equal to last vertex added for both A and B
        '''
        
        assert(parent_node.A_last_vertex_added == parent_node.A_last_vertex_used)
        assert(parent_node.B_last_vertex_added == parent_node.B_last_vertex_used)

        if(child_A_last_vertex_used < graph_vertices['m1']-1) or (child_A_last_vertex_used > graph_vertices['m1']-1 and child_A_last_vertex_used < graph_vertices['m']-1):
            
            '''
            Just add a vertex to A and then create edges and proceed as in the case
            Update the following:
                last vertex added
                vertex list of used vertices
                edges to be considered
            '''
            
            vertex_label_a = child_A_last_vertex_added + 1
            for each_vertex in B_list_of_vertices_used:
                edges_to_be_considered_for_the_cell.append([vertex_label_a,each_vertex])
            A_list_of_vertices_used.append(vertex_label_a)
            child_A_last_vertex_added = max(child_A_last_vertex_added, vertex_label_a)

        elif (child_B_last_vertex_used < graph_vertices['n']-1):
            vertex_label_b = child_B_last_vertex_added + 1
            for each_vertex in A_list_of_vertices_used:
                edges_to_be_considered_for_the_cell.append([each_vertex, vertex_label_b])
            B_list_of_vertices_used.append(vertex_label_b)
            child_B_last_vertex_added = max(child_B_last_vertex_added, vertex_label_b)
        else:
            
            assert(child_B_last_vertex_used == graph_vertices['n']-1)
            assert(child_A_last_vertex_used == graph_vertices['m1']-1)
            assert(child_A_last_vertex_used != graph_vertices['m']-1)
            # This should not happen because it would mean we created all the possible cells
            # and we have valid partition
            
            vertex_label_a = child_A_last_vertex_added + 1
            for each_vertex in B_list_of_vertices_used:
                edges_to_be_considered_for_the_cell.append([vertex_label_a, each_vertex])
            A_list_of_vertices_used.append(vertex_label_a)
            child_A_last_vertex_added = max(child_A_last_vertex_added, vertex_label_a)
        
        '''
            Now we have created a nonempty set of edges
            We pick an edge
        '''

        first_edge_of_the_cell = edges_to_be_considered_for_the_cell.pop(0)
        child_edges_considered.append(first_edge_of_the_cell)
        child_unused_edges.remove(first_edge_of_the_cell)

        child_A_last_vertex_used = max(child_A_last_vertex_used, first_edge_of_the_cell[0])
        child_B_last_vertex_used = max(child_B_last_vertex_used, first_edge_of_the_cell[1])

        all_possible_children = cell_creation(
            first_edge_of_the_cell,
            child_A_last_vertex_added,
            child_B_last_vertex_added,
            child_A_last_vertex_used,
            child_B_last_vertex_used,
            A_list_of_vertices_used,
            B_list_of_vertices_used,
            edges_to_be_considered_for_the_cell,
            cells_created_so_far,
            child_unused_edges,
            child_edges_considered,
            graph_vertices
        )
        
    else:
        first_edge_of_the_cell = edges_to_be_considered_for_the_cell.pop(0)
        child_edges_considered.append(first_edge_of_the_cell)
        child_unused_edges.remove(first_edge_of_the_cell)
        
        child_A_last_vertex_used = max(child_A_last_vertex_used, first_edge_of_the_cell[0])
        child_B_last_vertex_used = max(child_B_last_vertex_used, first_edge_of_the_cell[1])

        all_possible_children = cell_creation(
            first_edge_of_the_cell,
            child_A_last_vertex_added,
            child_B_last_vertex_added,
            child_A_last_vertex_used,
            child_B_last_vertex_used,
            A_list_of_vertices_used,
            B_list_of_vertices_used,
            edges_to_be_considered_for_the_cell,
            cells_created_so_far,
            child_unused_edges,
            child_edges_considered,
            graph_vertices
        )    

    del edges_to_be_considered_for_the_cell, 
    cells_created_so_far,child_edges_considered,
    child_A_last_vertex_used,
    child_B_last_vertex_used,
    child_A_last_vertex_added,
    child_B_last_vertex_added,
    A_list_of_vertices_used,
    B_list_of_vertices_used,
    child_unused_edges
 
    return all_possible_children
            


                
def cell_creation(
        first_edge_of_the_cell,
        child_A_last_vertex_added,
        child_B_last_vertex_added,
        child_A_last_vertex_used,
        child_B_last_vertex_used,
        A_list_of_vertices_used,
        B_list_of_vertices_used,
        edges_to_be_considered_for_the_cell,
        cells_created_so_far,
        child_unused_edges,
        child_edges_considered,
        graph_vertices
    ):

    '''
        Returns all possible children for this parent
        We still need to add more attributes to the child before we create it
    '''
    all_possible_children = []
    '''
        This function creates the second edge and hence the cell
        Once we have a tentative  cell, 
        1. We create equivalence classes
        2. We check no fold condition
        3. We update edge set of middle graph
        4. We find girth of middle graph, top graph and bottom graph
    '''

    assert(child_A_last_vertex_used <= child_A_last_vertex_added)
    assert(child_B_last_vertex_used <= child_B_last_vertex_added)
    
    if(child_B_last_vertex_used == child_B_last_vertex_added) and (child_B_last_vertex_used != graph_vertices['n']-1):
        vertex_b_to_be_added = child_B_last_vertex_added + 1
        B_list_of_vertices_used.append(vertex_b_to_be_added)
        child_B_last_vertex_added = vertex_b_to_be_added
        for v in A_list_of_vertices_used:
            edges_to_be_considered_for_the_cell.append([v, vertex_b_to_be_added])
    
    if(child_A_last_vertex_added == child_A_last_vertex_used):
        if(child_A_last_vertex_used < graph_vertices['m1'] -1) or (graph_vertices['m1']-1 < child_A_last_vertex_used and child_A_last_vertex_used < graph_vertices['m']-1):
            vertex_a_to_be_added = child_A_last_vertex_added + 1
            A_list_of_vertices_used.append(vertex_a_to_be_added)
            child_A_last_vertex_added = vertex_a_to_be_added
            for v in B_list_of_vertices_used:
                edges_to_be_considered_for_the_cell.append([vertex_a_to_be_added, v])
        
    assert(len(edges_to_be_considered_for_the_cell) > 0)
    
    for edge in edges_to_be_considered_for_the_cell:
        
        if(first_edge_of_the_cell[0] != edge[0]) and (first_edge_of_the_cell[1] != edge[1]):
            second_edge_of_the_cell = edge
            cell = [first_edge_of_the_cell, second_edge_of_the_cell]
            child_edges_considered_copy = deepcopy(child_edges_considered)
            child_edges_considered_copy.append(second_edge_of_the_cell)
            child_unused_edges_copy = deepcopy(child_unused_edges)
            child_unused_edges_copy.remove(second_edge_of_the_cell)
            child_cells_created_so_far =  deepcopy(cells_created_so_far)
            child_cells_created_so_far.append(cell)
            child_edges_to_be_considered_for_the_cell = deepcopy(edges_to_be_considered_for_the_cell)
            child_edges_to_be_considered_for_the_cell.remove(edge)
            assert(first_edge_of_the_cell not in child_edges_to_be_considered_for_the_cell) 
            assert(second_edge_of_the_cell not in child_edges_to_be_considered_for_the_cell)
            
            child_A_last_vertex_used_update = max(child_A_last_vertex_used, second_edge_of_the_cell[0])
            child_B_last_vertex_used_update = max(child_B_last_vertex_used, second_edge_of_the_cell[1])

            #horizontal_edges_a = parent_node.horizontal_edges_a + [[cell[0][0], cell[1][0]]]
            #horizontal_edges_b = parent_node.horizontal_edges_b + [[cell[0][1], cell[1][1]]]
            child_node = {
                'cells_created_so_far': child_cells_created_so_far,
                'edges_to_be_considered_for_the_cell': child_edges_to_be_considered_for_the_cell,
                'edges_considered': child_edges_considered_copy,
                'A_last_vertex_used': child_A_last_vertex_used_update,
                'B_last_vertex_used': child_B_last_vertex_used_update,
                'A_last_vertex_added': child_A_last_vertex_added,
                'B_last_vertex_added': child_B_last_vertex_added,
                'A_list_of_vertices_used': A_list_of_vertices_used,
                'B_list_of_vertices_used': B_list_of_vertices_used,
                'unused_edges': child_unused_edges_copy,
                'new_cell':cell
                #'horizontal_edges_a':horizontal_edges_a,
                #'horizontal_edges_b':horizontal_edges_b
            }
            all_possible_children.append([cell, child_node])
            
    return all_possible_children        
