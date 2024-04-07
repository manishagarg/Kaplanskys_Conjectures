# Copyright (c) [2024] [Manisha Garg]
# Custom License: See LICENSE file in the project root for the full license terms.

from copy import deepcopy
''' Need  to pass 
        parent pattern matrix for A and B, P_A and P_B
        parent vertex lists of patterns for A and B, v_A and v_B
        edge we are adding
        equivalence class we are adding an edge to
        equivalence class we are merging
        equivalence class we are removing
'''

import numpy

list_of_deleted_classes = []

# FOUR actions

def add_class( 
    edge, 
    label_of_class_to_be_added,
    m,
    n,
    graph
    ):
    '''
        Args: 
        pattern_vertex_list_a: Array It is an array of the form [[0, [], []],[1, [], []]] 
        edge_a/b = the horizontal edge we are adding to a(b) graph
        index = index of the equivalence class , that is, label of the ec
        We add two vertices to the middle graph corresponding to this label

        Return:
        1. middle_graph_edges: Array 
        It might be possible that it is empty. It is not a problem.
        2. child_vertex_list: Array
        We update in_class and out_class of in_vertex and out_vertex of graph A and B
    '''
    label_in = m + n + 2*(label_of_class_to_be_added)
    label_out = m + n + 2*(label_of_class_to_be_added) + 1
    if graph == 'A':
        x = edge[0]
        y = edge[1]
        
    elif graph == 'B':
        x = m + edge[0]
        y = m + edge[1]
    else:
        raise ValueError("The value of graph should be either A or B")

    middle_graph_edges = [(x, label_out), (y, label_in)]
   
    return [middle_graph_edges]


def add_edge_to_equiv_class( 
    edge, 
    label_of_class,
    m,
    n,
    graph):

    label_in = m + n + 2*(label_of_class)
    label_out = m + n + 2*(label_of_class) + 1
    if graph == 'A':
        x = edge[0]
        y = edge[1]
        
    elif graph == 'B':
        x = m + edge[0]
        y = m + edge[1]
    else:
        raise ValueError("The value of graph should be either A or B")

    middle_graph_edges = [(x, label_out), (y, label_in)]

    return [middle_graph_edges]


def merge_without_inversion( 
    label_to_be_kept, 
    label_to_be_merged,
    m,
    n
):
    
    middle_graph_edges = []
    middle_graph_edges.append([m+n+ 2*label_to_be_kept, m+n+ 2*label_to_be_merged])
    middle_graph_edges.append([m+n+ 2*label_to_be_kept+1, m+n+ 2*label_to_be_merged+1])

    return [middle_graph_edges]




def merge_inversion( 
    label_to_be_kept, 
    label_to_be_merged,
    m,
    n
):
    '''
    Args:
        label_to_be_merged: label of the class we invert and then merge it into the other class
    '''

    middle_graph_edges = []
    middle_graph_edges.append([m+n+ 2*label_to_be_kept, m+n+ 2*label_to_be_merged + 1])
    middle_graph_edges.append([m+n+ 2*label_to_be_kept+1, m+n+ 2*label_to_be_merged])

    return [middle_graph_edges]

