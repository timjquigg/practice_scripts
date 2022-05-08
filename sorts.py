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
    # This will loop over each item until it goes through a full loop
    # without having to change anything, at which point the list is
    # sorted.
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sorted = False
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
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    else:
        result += right
    return result


def quick_sort(lst, start, end):
    """This is an implimentation of the quick sort algorithm. It picks
    a middle point of the list at random to act as a pivot. It then
    divides the list into those items that are less than the value of
    the pivot and those items that are greater than the value of the
    pivot. It then recursively runs the same check on each half. This
    function alters the input list.

    Args:
        lst (list): The input list to be sorted.
        start (int): Where in the list to start.
        end (end): Where in the list to end.
    """
    if start >= end:
        return
    pivot_index = random.randrange(start, end + 1)
    pivot_value = lst[pivot_index]
    less_than_pointer = start
    lst[end], lst[pivot_index] = lst[pivot_index], lst[end]
    for i in range(start, end):
        if lst[i] < pivot_value:
            lst[i], lst[less_than_pointer] = lst[less_than_pointer], lst[i]
            less_than_pointer += 1
    lst[end], lst[less_than_pointer] = lst[less_than_pointer], lst[end]
    quick_sort(lst, start, less_than_pointer - 1)
    quick_sort(lst, less_than_pointer + 1, end)


# For testing
merge_test_list = []
bubble_test_list = []
quick_test_list = []
for i in range(10):
    merge_test_list.append(random.randint(0, 100))
    bubble_test_list.append(random.randint(0, 100))
    quick_test_list.append(random.randint(0, 100))


print("Original list for merge sort:\n", merge_test_list)
print("Sorted list from merge sort:\n", merge_sort(merge_test_list))
print("Original list for bubble sort:\n", bubble_test_list)
print("Sorted list from bubble sort:\n", bubblesort(bubble_test_list))
print("Original list for quick sort:\n", quick_test_list)
quick_sort(quick_test_list, 0, len(quick_test_list) - 1)
print("Sorted list from quick sort:\n", quick_test_list)
