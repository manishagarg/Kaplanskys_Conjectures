# Copyright (c) [2024] [Manisha Garg]
# Custom License: See LICENSE file in the project root for the full license terms.

from copy import deepcopy
import middle_graph_edges
import numpy

def noFoldOriented(equiv_class):
    no_fold = True
    f=[]
    g=[]
    for pair in equiv_class:
        f.append(pair[0])
        g.append(pair[1])
    if((len(set(f)) < len(f)) or (len(set(g)) < len(g))): no_fold = False
    return no_fold 

# We can update list of equivalence classes here in these functions itself
def mergeWithoutInversion(
    classes, 
    index_a, 
    index_b
    ):
    class_list = deepcopy(classes)
    merged_class = class_list[index_a][1]+class_list[index_b][1]
    no_fold = noFoldOriented(merged_class)
    class_list[index_a][1] = merged_class
    class_list.remove(class_list[index_b])
    return [class_list, no_fold]


def mergeWithInversion(
        classes, 
        inversion_class_index, 
        uninverted_class_index
    ):
    
    index = 0
    class_list = deepcopy(classes)
    class_to_be_removed_label = class_list[inversion_class_index][0][0]
    class_to_be_kept_label = class_list[uninverted_class_index][0][0]
    
    for (edge) in class_list[inversion_class_index][1]:
        class_list[inversion_class_index][1][index] = [edge[1], edge[0]]
        index = index+1
    
    merged_class = class_list[inversion_class_index][1] + class_list[uninverted_class_index][1]
    no_fold = noFoldOriented(merged_class)
    class_list[uninverted_class_index][1] = merged_class
    class_list.remove(class_list[inversion_class_index])
    return [class_list, no_fold]

def createEquivalenceClasses(
    child,
    parent_node,
    fold_check,
    m,
    n
    ):
    
    child_vertices_b_pattern = []
    child_vertices_a_pattern = []
    
    #Initializing
    action = ['nothingHappened']
    all_middle_graph_edges = []
    compatible_orientation = True
    no_fold = True
    new_cell = deepcopy(child[1]['new_cell'])
    girth_data_for_A_B = {
                "edge_added_in_A": [],
                "edge_added_in_B": []  
            }
    
    # Initializing parent_data
    equiv_classes_indices_child = deepcopy(parent_node.equiv_classes_indices)
    
    # Writing horizontal edges from vertical edges
    horizontal_a_edge = [new_cell[0][0], new_cell[1][0]]
    horizontal_a_edge_inverted =  [new_cell[1][0], new_cell[0][0]]
    horizontal_b_edge= [new_cell[0][1], new_cell[1][1]]
    horizontal_b_edge_inverted= [new_cell[1][1], new_cell[0][1]]
    
    parent_class_a = deepcopy(parent_node.equivalence_classes['of_a']) 
    parent_class_b = deepcopy(parent_node.equivalence_classes['of_b']) 
    equiv_class_child = {
        'of_a': [],
        'of_b': []
    }

    # parent_equiv_classes contains Equivalence classes for A and equivalence classes for B
    edge_a_present = False   
    edge_b_present = False
    edge_a_present_inverted = False
    edge_b_present_inverted = False
    # Index recording of horizontal edges in A and B. Is an edge or its inverted version present already in A or B?
    child_horizontal_a_edges = deepcopy(parent_node.horizontal_edges_a)
    child_horizontal_b_edges = deepcopy(parent_node.horizontal_edges_b)
    
    for (index,equiv_class) in enumerate(parent_class_a):
        if(horizontal_a_edge in equiv_class[1]):
            #record index
            edge_a_index = index
            edge_a_present = True
            label_of_class_for_a = parent_class_a[edge_a_index][0][0]
            #assert(horizontal_a_edge in child_horizontal_a_edges)
        elif(horizontal_a_edge_inverted in equiv_class[1]):
            edge_a_index = index
            edge_a_present_inverted = True
            label_of_class_for_a = parent_class_a[edge_a_index][0][0]
            #assert(horizontal_a_edge_inverted in child_horizontal_a_edges)
    
    for (index,equiv_class) in enumerate(parent_class_b):    
        if(horizontal_b_edge in equiv_class[1]):
            #record index
            edge_b_index = index
            edge_b_present = True
            label_of_class_for_b = parent_class_b[edge_b_index][0][0]
            #assert(horizontal_b_edge in child_horizontal_b_edges)
        elif(horizontal_b_edge_inverted in equiv_class[1]):
            edge_b_index = index
            edge_b_present_inverted = True
            label_of_class_for_b = parent_class_b[edge_b_index][0][0]
            #assert(horizontal_b_edge_inverted in child_horizontal_b_edges)

    if(edge_a_present):
        #child_horizontal_a_edges = child_horizontal_a_edges+[horizontal_a_edge] 
        if(edge_b_present):
            if(edge_a_index != edge_b_index):
                ''' 
                    ACTION: we merge without inversion
                '''

                action = ['mergeWithoutInversion']
                # ec data
                equiv_class_data_a = mergeWithoutInversion(
                    classes = parent_class_a, 
                    index_a = edge_a_index, # keep a
                    index_b = edge_b_index  # remove b
                )
                equiv_class_child['of_a'] = equiv_class_data_a[0]
                equiv_class_data_b = mergeWithoutInversion(
                    parent_class_b, 
                    edge_a_index, 
                    edge_b_index
                )
                equiv_class_child['of_b'] = equiv_class_data_b[0]
                # fold and label updation
                no_fold = equiv_class_data_a[1] and equiv_class_data_b[1]
                equiv_classes_indices_child.remove(label_of_class_for_b)
                # middle graph edges
                middle_graph_data_a = middle_graph_edges.merge_without_inversion(
                    label_to_be_kept = label_of_class_for_a,
                    label_to_be_merged = label_of_class_for_b,
                    m = m,
                    n = n
                )

                middle_graph_data_b = middle_graph_edges.merge_without_inversion(
                    label_to_be_kept = label_of_class_for_a,
                    label_to_be_merged = label_of_class_for_b,
                    m = m,
                    n = n
                )

                # because we need only the edges in middle graph merged
                # those edges will be the same in case of A and B
                # We have set distance between classes to be zero
                all_middle_graph_edges = middle_graph_data_a[0] 
                
            else:
                '''
                    we dont need to do anything
                '''
                action = ['nothingHappened']
                equiv_class_child = parent_node.equivalence_classes                
                all_middle_graph_edges = []

        elif(edge_b_present_inverted): # binverse present
            
            if(edge_a_index != edge_b_index):
                ''' 
                    ACTION: we merge with inversion
                '''
                action = ['mergeWithInversion']
                label_kept = label_of_class_for_a
                label_removed  = label_of_class_for_b
                child_horizontal_b_edges = child_horizontal_b_edges+[horizontal_b_edge]
            
                equiv_class_data_a = mergeWithInversion(
                    classes = parent_class_a, 
                    inversion_class_index = edge_b_index, # removing
                    uninverted_class_index = edge_a_index # keeping   
                )
                equiv_class_child['of_a'] = equiv_class_data_a[0]
                equiv_class_data_b = mergeWithInversion(
                    parent_class_b, 
                    edge_b_index, 
                    edge_a_index
                )
                equiv_class_child['of_b'] = equiv_class_data_b[0]
                # fold and label updation
                no_fold = equiv_class_data_a[1] and equiv_class_data_b[1]
                equiv_classes_indices_child.remove(label_removed)
                assert label_kept in equiv_classes_indices_child
                #middle link data
                middle_graph_data_a = middle_graph_edges.merge_inversion(
                        label_to_be_kept = label_kept, 
                        label_to_be_merged= label_removed,
                        m = m,
                        n = n)
                
                middle_graph_data_b = middle_graph_edges.merge_inversion(
                    label_to_be_kept = label_kept,
                    label_to_be_merged = label_removed,
                    m=m,
                    n= n
                )
                assert middle_graph_data_a[0]==middle_graph_data_b[0] # We could just remove middle graph calling for one of the functions
                # because we need only the edges in middle graph merged
                # those edges will be the same in case of A and B
                all_middle_graph_edges = middle_graph_data_a[0] 
                
            else:
                compatible_orientation = False    
        else: 
            '''
            ACTION: Add an edge to an EC in B graph
            # a is present but b or b inverse are not present
            # update the indexed class with b
            # We dont add any new class
            # We dont change anything in graph A, so no pattern or fold is introduced
            # We need to check b still
            '''
            action = ['addEdge']
            label = label_of_class_for_a
            child_horizontal_b_edges = child_horizontal_b_edges+[horizontal_b_edge] 

            parent_class_b[edge_a_index][1].append(horizontal_b_edge)
            equiv_class_child['of_a'] = parent_class_a
            equiv_class_child['of_b'] = parent_class_b
            # No-fold check
            no_fold = noFoldOriented(parent_class_b[edge_a_index][1]) if(fold_check) else True
            
            # need to check middle graph edges as well
            # no middle_graph edges are added due to A
            # Middle graph edges are added only in B
            equiv_classes_indices_child = equiv_classes_indices_child
            middle_graph_data_b = middle_graph_edges.add_edge_to_equiv_class(
                edge=horizontal_b_edge,
                label_of_class=label,
                m=m,
                n=n,
                graph="B"
            )

            all_middle_graph_edges = middle_graph_data_b[0]
            girth_data_for_A_B = {
                "edge_added_in_A": [],
                "edge_added_in_B": horizontal_b_edge  
            } 

                    
    elif(edge_a_present_inverted): # a inverse present
        if(edge_b_present):
            #child_horizontal_a_edges.remove(horizontal_a_edge_inverted)
            child_horizontal_a_edges = child_horizontal_a_edges+[horizontal_a_edge] 
                
            if(edge_a_index != edge_b_index):
                '''
                 ACTION: We merge with inversion
                '''
                action = ['mergeWithInversion']
                label_kept = label_of_class_for_b
                label_removed = label_of_class_for_a
                
                
                equiv_class_data_a = mergeWithInversion(
                    parent_class_a, 
                    edge_a_index, #removing
                    edge_b_index #keeping
                    )
                equiv_class_child['of_a'] = equiv_class_data_a[0]
                equiv_class_data_b = mergeWithInversion(
                    parent_class_b,
                    edge_a_index, 
                    edge_b_index
                    )
                equiv_class_child['of_b'] = equiv_class_data_b[0]
                no_fold = equiv_class_data_a[1] and equiv_class_data_b[1]
                
                equiv_classes_indices_child.remove(label_removed)
                assert(label_kept in equiv_classes_indices_child)
                #middle link data
                
                middle_graph_data_a = middle_graph_edges.merge_inversion( 
                        label_to_be_kept = label_kept, 
                        label_to_be_merged= label_removed,
                        m = m,
                        n = n
                        )
                
                middle_graph_data_b = middle_graph_edges.merge_inversion(
                    label_to_be_kept = label_kept,
                    label_to_be_merged = label_removed,
                    m = m,
                    n = n
                )
                all_middle_graph_edges = middle_graph_data_a[0] # because we need only the edges in middle graph merged
                # those edges will be the same in case of A and B

            else:
                compatible_orientation = False        
            
        elif(edge_b_present_inverted): # both inverses are present
            if(edge_a_index != edge_b_index):
                '''    
                 ACTION: we merge simply without inversion since both are inverted
                '''
                action = ['mergeWithoutInversion']
                equiv_class_data_a = mergeWithoutInversion(
                    parent_class_a, 
                    edge_a_index, 
                    edge_b_index
                    )
                equiv_class_child['of_a'] = equiv_class_data_a[0]
                equiv_class_data_b = mergeWithoutInversion(
                    parent_class_b, 
                    edge_a_index, 
                    edge_b_index
                    )
                equiv_class_child['of_b'] = equiv_class_data_b[0]
                no_fold = equiv_class_data_a[1] and equiv_class_data_b[1]
                equiv_classes_indices_child.remove(label_of_class_for_b)
                # middle graph edges
                middle_graph_data_a = middle_graph_edges.merge_without_inversion(
                    label_to_be_kept = label_of_class_for_a,
                    label_to_be_merged = label_of_class_for_b,
                    m = m,
                    n = n
                )
                middle_graph_data_b = middle_graph_edges.merge_without_inversion(
                    label_to_be_kept = label_of_class_for_a,
                    label_to_be_merged = label_of_class_for_b,
                    m = m,
                    n = n
                )
                all_middle_graph_edges = middle_graph_data_a[0] # because we need only the edges in middle graph merged
                # those edges will be the same in case of A and B
            else:
                '''
                    we dont need to do anything
                '''
                action = ['nothingHappened']
                equiv_class_child = parent_node.equivalence_classes
                all_middle_graph_edges = []                

        else:
            ''' 
             ACTION: Add b edge inverted to an EC 
             only a inverted is present
             we update the indexed class with b inverted
             Fold is not introduced for a but we need to check b for fold condition
            '''
            action = ['addEdge']
            label = label_of_class_for_a
            child_horizontal_b_edges = child_horizontal_b_edges+[horizontal_b_edge_inverted] 
           
            equiv_class_child['of_a'] = parent_class_a
            parent_class_b[edge_a_index][1].append(horizontal_b_edge_inverted)
            equiv_class_child['of_b'] = parent_class_b
            no_fold = noFoldOriented(parent_class_b[edge_a_index][1]) if(fold_check) else True
            
            # vertices_a remain same for A
            # equiv_list remains the same
            equiv_classes_indices_child = equiv_classes_indices_child
            # We just need to update the graph B with inverted edge b
            middle_graph_data_b = middle_graph_edges.add_edge_to_equiv_class(
                edge=horizontal_b_edge_inverted,
                label_of_class=label,
                m=m,
                n=n,
                graph="B"
            )
            
            all_middle_graph_edges = middle_graph_data_b[0]
            girth_data_for_A_B = {
                "edge_added_in_A": [],
                "edge_added_in_B": horizontal_b_edge_inverted  
            }

    elif(edge_b_present): 
        '''
        # a or a inverted are not present, only b is present
        # we add the a edge and b remains as it is
        # We dont introduce fold due to b since we are not merging or adding any edge to classes in b
        # But we need to check for fold condition due to a

        # ACTION (DONE): We add a edge to an existing EC
        '''
        action = ['addEdge']
        label = label_of_class_for_b
        child_horizontal_a_edges = child_horizontal_a_edges+[horizontal_a_edge] 
 
        parent_class_a[edge_b_index][1].append(horizontal_a_edge)
        equiv_class_child['of_a'] = parent_class_a
        equiv_class_child['of_b'] = parent_class_b
        no_fold = noFoldOriented(parent_class_a[edge_b_index][1]) if(fold_check) else True
        '''
            # check pattern here for adding an edge to a class
            # pattern_matrix_b  and vertices_b remain same for B
            # equiv_list remains the same
            # We just need to update the graph A
        '''
        equiv_classes_indices_child = equiv_classes_indices_child
        middle_graph_data_a = middle_graph_edges.add_edge_to_equiv_class(
            edge = horizontal_a_edge,
            label_of_class = label,
            m=m,
            n=n,
            graph="A"
        )       
        all_middle_graph_edges = middle_graph_data_a[0]
        girth_data_for_A_B = {
            "edge_added_in_A": horizontal_a_edge,
            "edge_added_in_B": []  
            }
        
    elif(edge_b_present_inverted): 
        '''
        # a or a inverted are not present, only b inverted is present
        # ACTION (DONE): we add the a edge by inverting
        '''
        action = ['addEdge']
        label = label_of_class_for_b
        child_horizontal_a_edges = child_horizontal_a_edges+[horizontal_a_edge_inverted] 

        parent_class_a[edge_b_index][1].append(horizontal_a_edge_inverted) 
        equiv_class_child['of_a'] = parent_class_a
        equiv_class_child['of_b'] = parent_class_b
        no_fold = noFoldOriented(parent_class_a[edge_b_index][1]) if(fold_check) else True
        
        equiv_classes_indices_child = equiv_classes_indices_child
        
        middle_graph_data_a = middle_graph_edges.add_edge_to_equiv_class(
            edge = horizontal_a_edge_inverted,
            label_of_class = label,
            m=m,
            n=n,
            graph="A"
        )
        all_middle_graph_edges = middle_graph_data_a[0]
        girth_data_for_A_B = {
            "edge_added_in_A": horizontal_a_edge_inverted,
            "edge_added_in_B": []  
            }
        
    else: # neither a nor b is present
        # ACTION: We create a new EC
        # No fold can be introduced here
        action = ['addClass']
        label_a = parent_class_a[-1][0][0]+1 if(len(parent_class_a)>0) else 0
        label_b = parent_class_b[-1][0][0]+1 if(len(parent_class_b)>0) else 0
        assert(label_a == label_b)
        child_horizontal_a_edges = child_horizontal_a_edges+[horizontal_a_edge]
        child_horizontal_b_edges = child_horizontal_b_edges+[horizontal_b_edge]
        
        parent_class_a.append([[label_a],[horizontal_a_edge]])
        parent_class_b.append([[label_b],[horizontal_b_edge]])
        equiv_class_child['of_a'] = parent_class_a
        equiv_class_child['of_b'] = parent_class_b
        
        equiv_classes_indices_child.append(label_a) #update equivalence_class_list
        middle_graph_data_a = middle_graph_edges.add_class(
            horizontal_a_edge, 
            label_a,
            m=m,
            n=n,
            graph = "A"
            )
        middle_graph_data_b = middle_graph_edges.add_class(
            horizontal_b_edge, 
            label_b,
            m=m,
            n=n,
            graph = "B"
            )
        all_middle_graph_edges = middle_graph_data_a[0] + middle_graph_data_b[0]
        girth_data_for_A_B = {
            "edge_added_in_A": horizontal_a_edge,
            "edge_added_in_B": horizontal_b_edge  
        }


    return [
        compatible_orientation and no_fold,
        equiv_class_child, 
        equiv_classes_indices_child, # Not needed in reality but jjust kept for checking and asserting
        child_vertices_a_pattern, 
        child_vertices_b_pattern,
        all_middle_graph_edges,
        action,
        girth_data_for_A_B,
        child_horizontal_a_edges,
        child_horizontal_b_edges
    ]
    
