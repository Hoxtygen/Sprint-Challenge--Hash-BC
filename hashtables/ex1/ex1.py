#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    result = None
    for j in range(length):
        key = weights[j]
        hash_table_insert(ht, key, j)
        element= limit - key
        res = hash_table_retrieve(ht, element)
        if res:
            if length == 2:
                res = 0
            result = (j, res)
    return result


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
