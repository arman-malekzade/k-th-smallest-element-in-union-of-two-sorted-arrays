__author__ = 'Arman Malekzade'
arr1 = [1, 2, 5, 6, 8, 29, 212, 213]
arr2 = [3, 4, 6, 7, 10, 11]


def index_k_of_union(k, l1, l2):
    if len(l1) == 0:
        return l2[k]
    if len(l2) == 0:
        return l1[k]
    divide_index = (k-1) / 2
    if k == 0:
        return min(l1[0], l2[0])
    if divide_index >= len(l1):
        return index_k_of_union(k-divide_index-1, l1, l2[divide_index+1:])
    if divide_index >= len(l2) or l1[divide_index] <= l2[divide_index]:
        return index_k_of_union(k-divide_index-1, l1[divide_index+1:], l2)
    else:
        return index_k_of_union(k-divide_index-1, l1, l2[divide_index+1:])


class Union:
    def __init__(self, list1, list2):
        self.l1 = list1
        self.l2 = list2

    def __getitem__(self, key):
        if key <= len(self.l1) + len(self.l2):
            return index_k_of_union(key-1, self.l1, self.l2)
        else:
            raise IndexError('Out of range')


U = Union(arr1, arr2)
print U[9]

