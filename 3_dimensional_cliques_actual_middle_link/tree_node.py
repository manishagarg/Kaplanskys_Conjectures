# Copyright (c) [2024] [Manisha Garg]
# Custom License: See LICENSE file in the project root for the full license terms.


from copy import deepcopy
from anytree import NodeMixin, RenderTree, Node
import datetime, math, numpy

class NodeClass(NodeMixin):
    def __init__(
        self,
        middle_graph_edges = [],
        cells_created_so_far = [],
        edges_to_be_considered_for_the_cell = [],
        edges_considered = [],
        A_last_vertex_used = 0,
        B_last_vertex_used = 0,
        A_last_vertex_added = 0,
        B_last_vertex_added = 0,
        A_list_of_vertices_used = [],
        B_list_of_vertices_used = [],
        unused_edges = [],
        P0_BE1_TE2_EER3_PBAA4_CoAA5_PBAB6_CoAB7_PBBB8_CoBB9 = [],
        edges = None,
        cells = [],
        equiv_classes = {'of_a':[], 'of_b': []}, 
        vertices_a_pattern=[], 
        vertices_b_pattern=[], 
        equivalence_class_list = [],
        shortest_len_a_matrix = numpy.array([]),
        shortest_len_b_matrix = numpy.array([]),
        shortest_len_middle_matrix = numpy.array([]), 
        cycle_len_list_middle_graph = numpy.array([]),
        cycle_len_list_a = numpy.array([]),
        cycle_len_list_b =numpy.array([]),
        horizontal_edges_a = [],
        horizontal_edges_b = [],
        node_ancestors = [],
        node_position = 0,
        progress_contribution = 1,
        girth_a = math.inf,
        girth_b = math.inf,
        girth_middle = math.inf,
        new_cell = [],
        equiv_classes_indices = [],
        action =[],
        total_girth = [],
        parents=[],
        parent_height = 0                 
    ):
        #Adequacy related information
        self.cells_created_so_far =  cells_created_so_far
        self.edges_to_be_considered_for_the_cell = edges_to_be_considered_for_the_cell
        self.edges_considered = edges_considered
        self.A_last_vertex_used = A_last_vertex_used
        self.B_last_vertex_used = B_last_vertex_used
        self.A_list_of_vertices_used = A_list_of_vertices_used
        self.B_list_of_vertices_used  = B_list_of_vertices_used
        self.A_last_vertex_added = A_last_vertex_added
        self.B_last_vertex_added = B_last_vertex_added
        self.P0_BE1_TE2_EER3_PBAA4_CoAA5_PBAB6_CoAB7_PBBB8_CoBB9 = P0_BE1_TE2_EER3_PBAA4_CoAA5_PBAB6_CoAB7_PBBB8_CoBB9
        self.unused_edges = unused_edges
        self.horizontal_edges_a = horizontal_edges_a
        self.horizontal_edges_b = horizontal_edges_b
        self.new_cell = new_cell
       # History/State/Progress related information
        self.node_ancestors = node_ancestors
        self.edges = edges
        self.cells = cells
        self.progress_contribution = progress_contribution
        self.node_position = node_position
        #Equivalence classes related information
        self.equivalence_classes = equiv_classes
        self.vertices_a_pattern = vertices_a_pattern
        self.vertices_b_pattern = vertices_b_pattern
        self.equivalence_class_list = equivalence_class_list
        self.equiv_classes_indices = equiv_classes_indices
        # Girth related information
        self.action = action
        self.middle_graph_edges = middle_graph_edges
        self.shortest_len_a_matrix = shortest_len_a_matrix
        self.shortest_len_b_matrix = shortest_len_b_matrix
        self.shortest_len_middle_matrix = shortest_len_middle_matrix
        self.cycle_len_list_middle_graph = cycle_len_list_middle_graph
        self.cycle_len_list_a = cycle_len_list_a
        self.cycle_len_list_b = cycle_len_list_b
        self.girth_a = girth_a
        self.girth_b = girth_b
        self.girth_middle = girth_middle
        self.total_girth=total_girth
        # to be checked
        self.file_name_partitions = "manisha.txt"
        #self.fake = numpy.random.rand(1000,1000)
        self.parents = parents
        self.parent_height = parent_height
