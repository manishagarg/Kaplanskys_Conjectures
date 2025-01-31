# Copyright (c) [2024] [Manisha Garg]
# Custom License: See LICENSE file in the project root for the full license terms.


import tree_class as treeInstance
from anytree import RenderTree

#This is where we can parallelize


size_list = [[4, 4], [4, 5], [4, 6], [5, 5], [4, 7], [5, 6], [4, 8], [5, 7], [4, 9], [6, 6], [4, 10], [5, 8], [6, 7], [4, 11], [5, 9], [4, 12], [6, 8], [7, 7], [5, 10], [4, 13], [6, 9], [5, 11], [4, 14], [7, 8], [4, 15], [5, 12], [6, 10], [7, 9], [4, 16], [8, 8], [5, 13], [6, 11], [4, 17], [5, 14], [7, 10], [4, 18], [6, 12], [8, 9], [5, 15], [4, 19], [7, 11], [6, 13], [4, 20], [5, 16], [8, 10], [9, 9], [4, 21], [6, 14], [7, 12], [5, 17], [4, 22], [8, 11], [5, 18], [6, 15], [9, 10], [7, 13], [4, 23], [5, 19], [4, 24], [6, 16], [8, 12], [7, 14], [9, 11], [4, 25], [5, 20], [10, 10], [6, 17], [8, 13], [5, 21], [7, 15], [6, 18], [9, 12], [5, 22], [10, 11], [7, 16], [8, 14], [6, 19], [5, 23], [9, 13], [7, 17], [5, 24], [6, 20], [8, 15], [10, 12], [11, 11], [5, 25], [6, 21], [7, 18], [9, 14], [8, 16], [10, 13], [6, 22], [11, 12], [7, 19], [9, 15], [8, 17], [6, 23], [7, 20], [10, 14], [11, 13], [6, 24], [8, 18], [9, 16], [12, 12], [7, 21], [6, 25], [10, 15], [8, 19], [9, 17], [7, 22], [11, 14], [12, 13], [8, 20], [10, 16], [7, 23], [9, 18], [11, 15], [7, 24], [8, 21], [12, 14], [13, 13], [10, 17], [9, 19], [7, 25], [8, 22], [11, 16], [9, 20], [10, 18], [12, 15], [13, 14], [8, 23], [11, 17], [9, 21], [10, 19], [8, 24], [12, 16], [13, 15], [14, 14], [9, 22], [11, 18], [8, 25], [10, 20], [12, 17], [9, 23], [13, 16], [11, 19], [10, 21], [14, 15], [9, 24], [12, 18], [10, 22], [11, 20], [13, 17], [14, 16], [9, 25], [15, 15], [12, 19], [10, 23], [11, 21], [13, 18], [14, 17], [10, 24], [12, 20], [15, 16], [11, 22], [13, 19], [10, 25], [12, 21], [14, 18], [11, 23], [15, 17], [16, 16], [13, 20], [11, 24], [12, 22], [14, 19], [15, 18], [16, 17], [13, 21], [11, 25], [12, 23], [14, 20], [15, 19], [13, 22], [12, 24], [16, 18], [17, 17], [14, 21], [13, 23], [12, 25], [15, 20], [16, 19], [17, 18], [14, 22], [13, 24], [15, 21], [16, 20], [14, 23], [17, 19], [18, 18], [13, 25], [15, 22], [14, 24], [16, 21], [17, 20], [18, 19], [15, 23], [14, 25], [16, 22], [17, 21], [15, 24], [18, 20], [19, 19], [16, 23], [17, 22], [15, 25], [18, 21], [19, 20], [16, 24], [17, 23], [18, 22], [19, 21], [16, 25], [20, 20], [17, 24], [18, 23], [19, 22], [20, 21], [17, 25], [18, 24], [19, 23], [20, 22], [21, 21], [18, 25], [19, 24], [20, 23], [21, 22], [19, 25], [20, 24], [21, 23], [22, 22], [20, 25], [21, 24], [22, 23], [21, 25], [22, 24], [23, 23], [22, 25], [23, 24], [23, 25], [24, 24], [24, 25], [25, 25]]

all_cell_type =  [[0, 4, 4], [0, 4, 5], [0, 4, 6], [5, 0, 5], [0, 4, 7], [0, 5, 6], [0, 4, 8], [5, 0, 7], [0, 4, 9], [0, 6, 6], [0, 4, 10], [0, 5, 8], [0, 6, 7], [0, 4, 11], [5, 0, 9], [0, 4, 12], [0, 6, 8], [7, 0, 7], [0, 5, 10], [0, 4, 13], [0, 6, 9], [5, 0, 11], [0, 4, 14], [0, 7, 8], [0, 4, 15], [0, 5, 12], [0, 6, 10], [7, 0, 9], [0, 4, 16], [0, 8, 8], [5, 0, 13], [0, 6, 11], [0, 4, 17], [0, 5, 14], [0, 7, 10], [0, 4, 18], [0, 6, 12], [0, 8, 9], [5, 0, 15], [0, 4, 19], [7, 0, 11], [0, 6, 13], [0, 4, 20], [0, 5, 16], [0, 8, 10], [9, 0, 9], [0, 4, 21], [0, 6, 14], [0, 7, 12], [5, 0, 17], [0, 4, 22], [0, 8, 11], [0, 5, 18], [0, 6, 15], [0, 9, 10], [7, 0, 13], [0, 4, 23], [5, 0, 19], [0, 4, 24], [0, 6, 16], [0, 8, 12], [0, 7, 14], [9, 0, 11], [0, 4, 25], [0, 5, 20], [0, 10, 10], [0, 6, 17], [0, 8, 13], [5, 0, 21], [7, 0, 15], [0, 6, 18], [0, 9, 12], [0, 5, 22], [0, 10, 11], [0, 7, 16], [0, 8, 14], [0, 6, 19], [5, 0, 23], [9, 0, 13], [7, 0, 17], [0, 5, 24], [0, 6, 20], [0, 8, 15], [0, 10, 12], [11, 0, 11], [5, 0, 25], [0, 6, 21], [0, 7, 18], [0, 9, 14], [0, 8, 16], [0, 10, 13], [0, 6, 22], [0, 11, 12], [7, 0, 19], [9, 0, 15], [0, 8, 17], [0, 6, 23], [0, 7, 20], [0, 10, 14], [11, 0, 13], [0, 6, 24], [0, 8, 18], [0, 9, 16], [0, 12, 12], [7, 0, 21], [0, 6, 25], [0, 10, 15], [0, 8, 19], [9, 0, 17], [0, 7, 22], [0, 11, 14], [0, 12, 13], [0, 8, 20], [0, 10, 16], [7, 0, 23], [0, 9, 18], [11, 0, 15], [0, 7, 24], [0, 8, 21], [0, 12, 14], [13, 0, 13], [0, 10, 17], [9, 0, 19], [7, 0, 25], [0, 8, 22], [0, 11, 16], [0, 9, 20], [0, 10, 18], [0, 12, 15], [0, 13, 14], [0, 8, 23], [11, 0, 17], [9, 0, 21], [0, 10, 19], [0, 8, 24], [0, 12, 16], [13, 0, 15], [0, 14, 14], [0, 9, 22], [0, 11, 18], [0, 8, 25], [0, 10, 20], [0, 12, 17], [9, 0, 23], [0, 13, 16], [11, 0, 19], [0, 10, 21], [0, 14, 15], [0, 9, 24], [0, 12, 18], [0, 10, 22], [0, 11, 20], [13, 0, 17], [0, 14, 16], [9, 0, 25], [15, 0, 15], [0, 12, 19], [0, 10, 23], [11, 0, 21], [0, 13, 18], [0, 14, 17], [0, 10, 24], [0, 12, 20], [0, 15, 16], [0, 11, 22], [13, 0, 19], [0, 10, 25], [0, 12, 21], [0, 14, 18], [11, 0, 23], [15, 0, 17], [0, 16, 16], [0, 13, 20], [0, 11, 24], [0, 12, 22], [0, 14, 19], [0, 15, 18], [0, 16, 17], [13, 0, 21], [11, 0, 25], [0, 12, 23], [0, 14, 20], [15, 0, 19], [0, 13, 22], [0, 12, 24], [0, 16, 18], [17, 0, 17], [0, 14, 21], [13, 0, 23], [0, 12, 25], [0, 15, 20], [0, 16, 19], [0, 17, 18], [0, 14, 22], [0, 13, 24], [15, 0, 21], [0, 16, 20], [0, 14, 23], [17, 0, 19], [0, 18, 18], [13, 0, 25], [0, 15, 22], [0, 14, 24], [0, 16, 21], [0, 17, 20], [0, 18, 19], [15, 0, 23], [0, 14, 25], [0, 16, 22], [17, 0, 21], [0, 15, 24], [0, 18, 20], [19, 0, 19], [0, 16, 23], [0, 17, 22], [15, 0, 25], [0, 18, 21], [0, 19, 20], [0, 16, 24], [17, 0, 23], [0, 18, 22], [19, 0, 21], [0, 16, 25], [0, 20, 20], [0, 17, 24], [0, 18, 23], [0, 19, 22], [0, 20, 21], [17, 0, 25], [0, 18, 24], [19, 0, 23], [0, 20, 22], [21, 0, 21], [0, 18, 25], [0, 19, 24], [0, 20, 23], [0, 21, 22], [19, 0, 25], [0, 20, 24], [21, 0, 23], [0, 22, 22], [0, 20, 25], [0, 21, 24], [0, 22, 23], [21, 0, 25], [0, 22, 24], [23, 0, 23], [0, 22, 25], [0, 23, 24], [23, 0, 25], [0, 24, 24], [0, 24, 25], [25, 0, 25]]


folder_name = 'output_clique_actual_full_search_4_3'
file_name_raw_table_data = 'raw_table_data_clique_4_3.txt'
        
conditions_to_be_checked=[0,1,2,3]
'''
Conditions:
    1 = girth condition
    2 = adequacy condition
    3 = equivalence classes
'''


def initiate(
    m, 
    n, 
    cell_type,
    conditions_to_be_checked, 
    file_name_partitions,
    file_name_all_conditions,
    file_name_log_file,
    file_name_raw_table_data
    ):

    valid_partitions = []

    '''
        0 : Unoriented
        1 : Pattern
        2 : No Fold
        3 : Girth
    '''

    file_names = {
        'file_name_partitions': file_name_partitions,
        'file_name_all_conditions': file_name_all_conditions,
        'file_name_log_file':file_name_log_file,
        'file_name_raw_table_file': file_name_raw_table_data

    }
    tree = treeInstance.MainTree( 
        m, 
        n, 
        conditions_to_be_checked,
        cell_type
    )

    tree.createTree(
        conditions_to_be_checked,
        file_name_partitions, 
        file_name_all_conditions,
        file_name_log_file,
        file_name_raw_table_data,
        folder_name)
    
    return valid_partitions


def listOfSizes (size_list, conditions_to_be_checked, all_cell_type): 

    str_conditions = ''.join(map(str,conditions_to_be_checked)) 
    for index,size_tuple in enumerate(size_list):
        cell_type = all_cell_type[index]
        m = size_tuple[0]
        n = size_tuple[1]
        mn = m*n
        str_mn = str(mn) + '_'+str(m)+'by'+str(n)+'_'
        #file_name_cond = str_mn + 'conditions'+ str_conditions + '.txt'
        file_name_partitions = str_mn + 'partitions'+ '.txt'
        file_name_all_conditions = '!!' + str_mn + 'cond0123' + '.txt'
        file_name_log_file = str_mn + '_log.txt'
        file_name_raw_table_data = 'raw_table_data_clique_4_3.txt'
        #file_name_state = str_mn + '_state.txt'
        
        valid_partitions = initiate( 
            m, 
            n, 
            cell_type,
            conditions_to_be_checked,
            file_name_partitions,
            file_name_all_conditions,
            file_name_log_file,
            file_name_raw_table_data
            ) 
        #print("The code has run")


listOfSizes(
    size_list = size_list, 
    conditions_to_be_checked = conditions_to_be_checked,
    all_cell_type = all_cell_type
    )


