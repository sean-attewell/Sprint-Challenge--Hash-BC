#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    """
    YOUR CODE HERE
    """

    index = 0

    for item in weights:
        target = limit - item
        key_already_in_table = hash_table_retrieve(ht, item)
        # need first or condition because 0 isn't considered true
        if (key_already_in_table == 0 or key_already_in_table) and (limit - item == target):
            return(index, key_already_in_table)
        hash_table_insert(ht, item, index)
        index += 1    

    # index = 0

    for item in weights:
        target = limit - item
        print('target', target)
        # hash_table_remove(ht, item)
        target_index = hash_table_retrieve(ht, target)
        # hash_table_insert(ht, item, index)
        # index += 1 
        print('target_index', target_index)

        if target_index != None:
            item_index = hash_table_retrieve(ht, item)
            print('item_index', item_index)

            if item_index > target_index:
                print('(item_index, target_index)', (item_index, target_index))
                return (item_index, target_index)
            else:
                print('(target_index, item_index)', (target_index, item_index))
                return (target_index, item_index)


    return None

# get_indices_of_item_weights([4, 4], 2, 8)

def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
