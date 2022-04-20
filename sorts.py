import random

def bubblesort(lst):
    """This is a basic implementation of the bubble sort algorithm. It
    checks each item in the list against its adjacent item if the lower
    of the two items is placed in front. It repeats starting at the
    beginning of the list until it has gone through the list N times.
    This function does alter the input list and returns it sorted. 

    Args:
        lst (list): This is the list that you would like to sort.

    Returns:
        lst: The original list, now sorted.
    """
    for item in lst:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

def merge_sort(lst):
    """This is an implimentation of the merge sort algorithm. It splits
    the original list in half recursively until it is split into single
    element lists. It then calls the merge helper function to
    reassemble the lists in order. This function does not alter the
    input list.

    Args:
        lst (list): This is the list that will be sorted
    """
    # If the input list is a single item, return it.
    if len(lst) <= 1:
        return lst
    # If the input list is longer than one item, split it in half
    # recursively.
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)

def merge(left, right):
    """This is a helper function for the merge_sort function. It takes
    the split lists and combines them in order, returning a new sorted
    list.

    Args:
        left (list): The left half of the list from merge_sort.
        right (list): The right half of the list from merge_sort.
    
    Returns:
        result (list): A new list that is a sorted copy of the list
        that was input into the merge_sort function.
    """
    result = []
    while (left and right):
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    else:
        result += right
    return result

#For testing
test_list = []
for i in range(10):
    test_list.append(random.randint(0,100))

print(test_list)
print(merge_sort(test_list))
print(test_list)
print(bubblesort(test_list))
print(test_list)