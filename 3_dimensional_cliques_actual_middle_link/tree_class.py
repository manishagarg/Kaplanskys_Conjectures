# Copyright (c) [2024] [Manisha Garg]
# Custom License: See LICENSE file in the project root for the full license terms.


import numpy, math, datetime
from anytree import NodeMixin, RenderTree, Node
from copy import deepcopy
import createChildren
import equivalence
import girth_all_graphs
import tree_node as nodeInstance
import psutil, sys
import clique


class MainTree:
   
    def __init__(self, m, n, conditions_to_be_checked, cell_type):
        
        self.tree = []
        self.cell_type = cell_type
        self.m = m
        self.n = n
        self.m1 = 0
        self.m2 = self.m
        self.valid_partitions = []
        self.conditions_to_be_checked = conditions_to_be_checked
        self.no_of_iterations = 0
        self.no_of_valid_partitions = 0
        self.tree_last_node = None
        self.girth_table =  numpy.zeros((max(self.m, self.n),min((self.m *(self.m - 1)), (self.n *(self.n - 1)))))
        self.total_progress = 0 #not being used right now
        self.no_of_children = 0
        self.graph_vertices = {}
        self.girth_check = True
        self.equivalence_check = True
        self.fold_check = True
        self.file_name_partitions='test.txt'
        self.file_name_all_conditions='test.txt'
        self.file_name_girth_4='test.txt'
        self.file_name_girth_table='test.txt'
        self.file_name_log_file='test.txt'
        self.table_data_file = 'test.txt'
        self.height = 0
        # variables inorder to release memory
        self.valid_girth = True
        self.valid_orientation = True
        self.all_possible_children = []
        self.child_node = None
        self.girth_A_data = []
        self.begin_time = 0
        self.last_height_increase_time = None
        pass
    
    def memory_usage_psutil(self):
    # return the memory usage in MB
    
        process = psutil.Process()
        mem = process.memory_info()[0] / float(2 ** 20)
        print(str(mem) + (' MB'))
        return mem
    
    def createTree(
        self,
        checks,
        file_name_partitions, 
        file_name_all_conditions,
        file_name_log_file,
        file_name_raw_table_data,
        folder_name
        ): 
        
        #print('At the start') 
        #self.memory_usage_psutil()
        # File names
        self.file_name_partitions = file_name_partitions
        self.file_name_all_conditions = file_name_all_conditions
        self.file_name_log_file = file_name_log_file
        self.table_data_file = file_name_raw_table_data
        self.m1 = self.cell_type[0]
        self.m2 = self.cell_type[1]
        ### condition check
        if 0 not in checks:
            self.girth_check = False
        
        self.graph_vertices = {
            'm1':self.m1,
            'm2': self.m2,
            'm': self.m,
            'n': self.n
        }
        vertices_a_pattern = []
        vertices_b_pattern = []
        
        # logging:
        log_file = open(file_name_log_file, "a")
        #print("Code began for the size: ", self.m, "x", self.n, file=log_file)
        print("Code began for the size: ", self.m, "x", self.n, file=log_file)

        begin_time = datetime.datetime.now()
        self.begin_time = begin_time
        self.last_height_increase_time = begin_time
        print("Begin Time: ", begin_time, file=log_file)
        log_file.close()

        
        
        
        # For now 1 is always in the condition
        if 1 in self.conditions_to_be_checked: #Check if pattern is present
            # creating vertex patterns
            for i in range(self.m): vertices_a_pattern.append([i,[],[]])
            for i in range(self.n): vertices_b_pattern.append([i, [],[]])
            # Girth data
            shortest_len_a_matrix = numpy.matrix(numpy.ones((self.m,self.m)) * numpy.inf)
            numpy.fill_diagonal(shortest_len_a_matrix, 0)
            shortest_len_b_matrix = numpy.matrix(numpy.ones((self.n,self.n)) * numpy.inf)
            numpy.fill_diagonal(shortest_len_b_matrix, 0)
            

        unused_edges = []
        for i in range(self.m):
            for j in range(self.n):
                unused_edges.append([i,j])
        '''
            We check if we have odd partition or even
        '''    
        
        
        
        #checking if mn is even or odd
        if((self.m * self.n)%2 == 0):
            unused_edges.remove([0,0])
            unused_edges.remove([1,1])
            vertices_a_pattern[0][2].append(0)
            vertices_a_pattern[1][1].append(0)
            vertices_b_pattern[0][2].append(0)
            vertices_b_pattern[1][1].append(0)

            slm_middle_order = self.m +self.n + 2
            shortest_len_middle_matrix = numpy.matrix(numpy.ones((slm_middle_order,slm_middle_order)) * numpy.inf) # since we have
            numpy.fill_diagonal(shortest_len_middle_matrix, 0) 
            # first ec labeled as 0 to begin with
            # initialization of shorlest len matrix of middle graph
            # the edges are (a_0, color1_in, b_0), (a_1, color1_out, b_1)
            # (a_0, color1_out)=0.5, (color1_out, b_0) = 0.5, (a_0, b_0)=1
            # (a_1, color1_in)=0.5, (color1_in, b_1) = 0.5, (a_1, b_1)=1
            
            # Indices to update -
            # Corresponding to a_i, we have index i
            # Corresponding to b_j, we have index self.m + j
            # For color_i, in, we have self.m +self.n+2(i) if in
            # For color_i, out, we have self.m +self.n+2(i)+1 if out
            
            # The list L of edges we have so far:
            # L = [(a_1, 0in),(a_0, 0_out),(b_1, 0in),(b_0, 0out)]
            # Indices = [(1,8), (0,9), (5,8), (4, 9)] to be labeled 1/2
            # (1, self.m +self.n), (0, self.m +self.n+1), (self.m+1, self.m +self.n), (self.m, self.m +self.n+1)

            shortest_len_middle_matrix[0, self.m + self.n+1] = 0.5
            shortest_len_middle_matrix[1, self.m + self.n] = 0.5
            shortest_len_middle_matrix[self.m, self.m + self.n+1] = 0.5
            shortest_len_middle_matrix[self.m+1, self.m + self.n] = 0.5
            shortest_len_middle_matrix[0, self.m] = 1
            shortest_len_middle_matrix[1, self.m + 1] = 1
            
            # Updating the symmetric entries
            shortest_len_middle_matrix[self.m + self.n+1, 0] = 0.5
            shortest_len_middle_matrix[self.m + self.n, 1] = 0.5
            shortest_len_middle_matrix[self.m + self.n+1, self.m] = 0.5
            shortest_len_middle_matrix[self.m + self.n, self.m+1] = 0.5
            shortest_len_middle_matrix[self.m, 0] = 1
            shortest_len_middle_matrix[self.m + 1, 1] = 1
            

            shortest_len_a_matrix[0,1] = 1 
            shortest_len_a_matrix[1,0] = 1
            shortest_len_b_matrix[0,1] = 1 
            shortest_len_b_matrix[1,0] = 1
            
            
            
        
            self.tree_last_node = nodeInstance.NodeClass(
                cells_created_so_far = [[[0,0], [1,1]]],
                edges_to_be_considered_for_the_cell = [[0,1], [1,0]],
                edges_considered = [[0,0], [1,1]],
                A_last_vertex_used = 1,
                B_last_vertex_used = 1,
                A_last_vertex_added = 1,
                B_last_vertex_added = 1,
                A_list_of_vertices_used = [0,1],
                B_list_of_vertices_used = [0,1],
                unused_edges=unused_edges,
                edges = [[0,0], [1,1]], #sample [(0,0), (2,3), (5,6)]; max # = mn
                cells = [[[0,0], [1,1]]],
                middle_graph_edges = [],
                P0_BE1_TE2_EER3_PBAA4_CoAA5_PBAB6_CoAB7_PBBB8_CoBB9=[],
                equiv_classes = {'of_a':[[[0], [[0,1]]]], 'of_b': [[[0], [[0,1]]]]},
                new_cell = [], 
                vertices_a_pattern = vertices_a_pattern,
                vertices_b_pattern = vertices_b_pattern,
                equivalence_class_list = [0],
                shortest_len_a_matrix= shortest_len_a_matrix,
                shortest_len_b_matrix = shortest_len_b_matrix,
                shortest_len_middle_matrix = shortest_len_middle_matrix,
                cycle_len_list_a = numpy.array(numpy.ones(self.m) * numpy.inf),
                cycle_len_list_b = numpy.array(numpy.ones(self.n) * numpy.inf),
                cycle_len_list_middle_graph = numpy.array(numpy.ones(self.m + self.n + 2) * numpy.inf),
                horizontal_edges_a = [[0,1]],
                horizontal_edges_b = [[0,1]],
                node_ancestors = [],
                node_position = 0,
                progress_contribution = 1,
                girth_a = math.inf,
                girth_b = math.inf,
                girth_middle = math.inf,
                equiv_classes_indices = [0],
                parents=[],
                parent_height = 0
                )
            
        
        else:
            
            slm_middle_order = self.m +self.n
            shortest_len_middle_matrix = numpy.matrix(numpy.ones((slm_middle_order,slm_middle_order)) * numpy.inf) # since we have
            numpy.fill_diagonal(shortest_len_middle_matrix, 0) 
            
            unused_edges.remove([0,0])
            self.tree_last_node = nodeInstance.NodeClass(
                cells_created_so_far = [[[0,0]]],
                edges_to_be_considered_for_the_cell = [],
                edges_considered = [[0,0]],
                A_last_vertex_used = 0,
                B_last_vertex_used = 0,
                A_last_vertex_added = 0,
                B_last_vertex_added = 0,
                A_list_of_vertices_used = [0],
                B_list_of_vertices_used = [0],
                unused_edges=unused_edges,
                edges = [[0,0]], #sample [(0,0), (2,3), (5,6)]; max # = mn
                cells = [[[0,0]]],
                middle_graph_edges = [],
                P0_BE1_TE2_EER3_PBAA4_CoAA5_PBAB6_CoAB7_PBBB8_CoBB9 = [],
                equiv_classes = {'of_a':[], 'of_b': []},
                new_cell = [],
                vertices_a_pattern = vertices_a_pattern,
                vertices_b_pattern = vertices_b_pattern,
                equivalence_class_list = [],
                shortest_len_a_matrix = shortest_len_a_matrix,
                shortest_len_b_matrix = shortest_len_b_matrix,
                shortest_len_middle_matrix =  shortest_len_middle_matrix,
                cycle_len_list_a = numpy.array(numpy.ones(self.m) * numpy.inf),
                cycle_len_list_b = numpy.array(numpy.ones(self.n) * numpy.inf),
                cycle_len_list_middle_graph = numpy.array(numpy.ones(self.m + self.n) * numpy.inf),
                horizontal_edges_a = [],
                horizontal_edges_b = [],
                node_ancestors = [],
                node_position = 0,
                progress_contribution = 1,
                girth_a = math.inf,
                girth_b = math.inf,
                girth_middle = math.inf,
                equiv_classes_indices = [],
                parents=[],
                parent_height = 0
                )
            
        

        '''
        Printing files
        '''
        text_file_valid_partitions = open(file_name_partitions, "a")
        print("The size of graphs is ", self.m, "x", self.n, file=text_file_valid_partitions)
        text_file_valid_partitions.close()
        
        
        #Girth condition is present
        self.exploreTree(
            self.tree_last_node
        )
        
        

        log_file = open(file_name_log_file, "a")
        print("The program ended for ", self.m, "x", self.n, file=log_file)
        print("Number of valid partitions found are: ", self.no_of_valid_partitions, file=log_file)
        end_time = datetime.datetime.now()
        delta_time = end_time-begin_time
        print("End time: ", end_time, file=log_file)
        print("The program ran for the duration: ", end_time-begin_time, file=log_file)
        print("-----------------------------------------------------------", file=log_file)
        log_file.close()
        # Output folder
        # Create the folder if it doesn't exist
        
        import os
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        file_path_table_data = os.path.join(folder_name, self.table_data_file)
        table_data_file = open(file_path_table_data, "a")
        print("{'m':", self.m, ",'n':",self.n, ",'time_taken':'" ,str(delta_time), "','height_tree':", self.height, ",'no_of_valid_partitions':", self.no_of_valid_partitions," },",file=table_data_file)
        table_data_file.close()
        return [self.valid_partitions]
    
    def mianOperations(self, parent_node, each_child):
        
        self.valid_girth = True
        self.valid_orientation = True
        self.clique_condition_satisfied = True
        self.child_node = nodeInstance.NodeClass(
            cells_created_so_far = each_child[1]['cells_created_so_far'],
            edges_to_be_considered_for_the_cell = each_child[1]['edges_to_be_considered_for_the_cell'],
            edges_considered = each_child[1]['edges_considered'],
            A_last_vertex_used = each_child[1]['A_last_vertex_used'],
            B_last_vertex_used = each_child[1]['B_last_vertex_used'],
            A_last_vertex_added = each_child[1]['A_last_vertex_added'],
            B_last_vertex_added = each_child[1]['B_last_vertex_added'],
            A_list_of_vertices_used = each_child[1]['A_list_of_vertices_used'],
            B_list_of_vertices_used = each_child[1]['B_list_of_vertices_used'],
            unused_edges = each_child[1]['unused_edges'],
            new_cell = each_child[1]['new_cell']
        )
        if self.equivalence_check:
            equivalence_class_data = equivalence.createEquivalenceClasses(
            each_child, 
            parent_node,
            True,
            self.m,
            self.n
            )
            self.valid_orientation = equivalence_class_data[0]
            child_node_parent_height = deepcopy(parent_node.parent_height)
            if self.valid_orientation:
                each_child[1]['middle_graph_edges'] = equivalence_class_data[5]
                #update child node
                self.child_node.equivalence_classes = equivalence_class_data[1]
                self.child_node.equivalence_class_list= equivalence_class_data[2]
                self.child_node.equiv_classes_indices= equivalence_class_data[2]
                self.child_node.action = equivalence_class_data[6]
                self.girth_data_for_A_B = equivalence_class_data[7]
                self.child_node.horizontal_edges_a=equivalence_class_data[8]
                self.child_node.horizontal_edges_b=equivalence_class_data[9]
                self.child_node.parent_height = child_node_parent_height+1

        
        if self.girth_check and self.valid_orientation and self.equivalence_check:
            # middle graph edges will be created only due to equivalence classes
            #initialize girth_a, girth_b and girth_middle
            girth_middle=0
            girth_a = 0
            girth_b = 0

            assert(self.valid_orientation == True)
            assert(self.valid_girth == True)

            # girth_Middle graph
            self.girth_middle_link_data = girth_all_graphs.girth(
                number_of_vertices = len(parent_node.cycle_len_list_middle_graph),
                edges_added=each_child[1]['middle_graph_edges'],
                shortest_len_mat=parent_node.shortest_len_middle_matrix,
                cycle_len_list=parent_node.cycle_len_list_middle_graph,
                action=self.child_node.action
            )
            girth_middle = numpy.amin(self.girth_middle_link_data[1])
            self.child_node.shortest_len_middle_matrix =self.girth_middle_link_data[0]
            self.child_node.cycle_len_list_middle_graph =self.girth_middle_link_data[1]
            self.child_node.girth_middle=girth_middle

            # girth_A
            if(len(self.girth_data_for_A_B['edge_added_in_A']) != 0):
                self.girth_A_data = girth_all_graphs.girth(
                    number_of_vertices=self.m,
                    edges_added=[self.girth_data_for_A_B['edge_added_in_A']],
                    shortest_len_mat=parent_node.shortest_len_a_matrix,
                    cycle_len_list=parent_node.cycle_len_list_a,
                    action=[]
                )
                self.child_node.shortest_len_a_matrix =self.girth_A_data[0]
                self.child_node.cycle_len_list_a =self.girth_A_data[1]
                
            else:
                self.child_node.shortest_len_a_matrix = parent_node.shortest_len_a_matrix
                self.child_node.cycle_len_list_a = parent_node.cycle_len_list_a
            girth_a = numpy.amin(self.child_node.cycle_len_list_a)
            self.child_node.girth_a=girth_a
            assert(girth_a != 2)

            # girth_B
            if(len(self.girth_data_for_A_B['edge_added_in_B']) != 0):
                self.girth_B_data = girth_all_graphs.girth(
                    number_of_vertices=self.n,
                    edges_added=[self.girth_data_for_A_B['edge_added_in_B']],
                    shortest_len_mat=parent_node.shortest_len_b_matrix,
                    cycle_len_list=parent_node.cycle_len_list_b,
                    action=[]
                )
                
                self.child_node.shortest_len_b_matrix =self.girth_B_data[0]
                self.child_node.cycle_len_list_b =self.girth_B_data[1]
                
            else:
                self.child_node.shortest_len_b_matrix = parent_node.shortest_len_b_matrix
                self.child_node.cycle_len_list_b = parent_node.cycle_len_list_b
            
            girth_b = numpy.amin(self.child_node.cycle_len_list_b)
            self.child_node.girth_b=girth_b

            # girth condition
            p = min(girth_a, girth_b)
            q = girth_middle

            if (p>=4 and q>=3):
                self.valid_girth = True
            else:
                self.valid_girth = False

            self.child_node.total_girth = [girth_a, girth_middle, girth_b] if self.equivalence_check and self.valid_orientation else [girth_a, girth_b]

        if self.valid_orientation and self.valid_girth:
            
            self.clique_condition_satisfied = clique.has_no_four_cliques(self.child_node.horizontal_edges_a) and clique.has_no_four_cliques(self.child_node.horizontal_edges_b)
            assert self.child_node.parent_height == len(self.child_node.cells_created_so_far)-1
            if (not self.clique_condition_satisfied):
                print('here')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

            if (self.child_node.parent_height > self.height):
                self.height = self.child_node.parent_height
                # logging:
                log_file = open(self.file_name_log_file, "a")
                print("Height of the tree is: ", self.height, file=log_file)
                current_time = datetime.datetime.now()
                time_elapsed = current_time - self.last_height_increase_time
                print("Time elapsed from last height increase ", time_elapsed, file=log_file)
                self.last_height_increase_time = current_time
                log_file.close()

        return

    
    def exploreTree(
            self,
            parent_node
        ):
        #print("Explore Tree Starts", sys.getsizeof(self))
        self.valid_girth = True
        self.valid_orientation = True
        
        #print('Explore Tree')
        #print('Height of the tree', self.height)
        #self.memory_usage_psutil()

        '''
            1. Create potential children using adequacy condition
               call possible_cells = adequacy_condition()
            2. Create equivalence classes
            3. Girth condition
        '''
        
        if (len(parent_node.cells_created_so_far) < ((self.m)*(self.n)/2)): #Stopping criteria
            
            #print("Explore Tree: inside the first if", sys.getsizeof(self))
            assert(len(parent_node.unused_edges) > 0)
            assert(len(parent_node.edges_considered) < self.m * self.n)
            
            self.no_of_children = self.no_of_children + 1
            
            self.all_possible_children = createChildren.adequacy_condition(
                parent_node,
                self.graph_vertices
            )
            #print("Explore Tree: after storing all possible children", sys.getsizeof(self))
            for each_child in self.all_possible_children: # = [A ,B,C, D], [A1, A2] [A11,  A12, A13]
                self.mianOperations(parent_node, each_child)
                if self.valid_orientation and self.valid_girth and self.clique_condition_satisfied:
                    
                    #print("size of child node: ", sys.getsizeof(self.child_node))   
                    self.exploreTree(
                        self.child_node
                    )
        
        else:
            '''
                We have a valid partition and we cannot create
                any further children
            '''
            self.no_of_valid_partitions +=1
            self.no_of_children = self.no_of_children+1
            if(self.no_of_valid_partitions <=50):
                self.print_data(self.file_name_partitions, parent_node)
        return

    def print_data(
        self,
        file_name,
        parent_node
        ): 

        log_file = open(self.file_name_log_file, "a")
        print("Found a valid partition with height", self.height, file=log_file)
        log_file.close()
        file_name = open(file_name, "a")

        print('**************************************************************************************', file=file_name)
        print('partition_number = ', self.no_of_valid_partitions, file = file_name)
        print('partition = ', parent_node.cells_created_so_far, file = file_name)
        
        print('A_no_of_vertices(m) = ', self.m, file = file_name)
        print('B_no_of_vertices(n) = ', self.n, file = file_name)

        print('A_number_of_horizontal_edges = ', len(parent_node.horizontal_edges_a), file = file_name)
        print('A_equivalence_classes = ', parent_node.equivalence_classes, file = file_name)
        print('A_horizontal_edges = ', parent_node.horizontal_edges_a, file = file_name)
        #expected_vertices = int( reduce(mul, (Fraction(self.m-i, i+1) for i in range(2)), 1) )
        #print("A_Relative_no_of_edges = ",len(parent_node.horizontal_edges_a), "/", expected_vertices, "=", (len(parent_node.horizontal_edges_a))/expected_vertices, file = file_name)
        
        print('B_number_of_horizontal_edges = ', len(parent_node.horizontal_edges_b), file = file_name)
        print('B_equivalence_classes = ', parent_node.equivalence_classes, file = file_name)
        print('B_horizontal_edges= ', parent_node.horizontal_edges_b, file = file_name)
        #expected_vertices = int( reduce(mul, (Fraction(self.n-i, i+1) for i in range(2)), 1) )
        #print("B_Relative_no_of_edges = ",len(parent_node.horizontal_edges_b), "/", expected_vertices, "=",(len(parent_node.horizontal_edges_b))/expected_vertices, file = file_name)
        
        
        #print('girth_table = ', girth_table, file=file_name)
        print('total_girth = ',parent_node.total_girth, file = file_name)
        g = (min(parent_node.total_girth[0], parent_node.total_girth[2]),\
             parent_node.total_girth[1])\
            if len(parent_node.total_girth)>2 \
            else None
        print('Girth (p,q) = ', g, file = file_name)

        return


