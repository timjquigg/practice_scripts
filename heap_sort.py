class MaxHeap:
    """This class creates a Max Heap data structure. Used for heap sorting."""

    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    # Helper Methods

    def parent_index(self, index):
        return index // 2

    def left_child_index(self, index):
        return index * 2

    def right_child_index(self, index):
        return index * 2 + 1

    def child_present(self, index):
        return self.left_child_index(index) <= self.count

    def get_larger_child(self, index):
        left_index = self.left_child_index(index)
        right_index = self.right_child_index(index)
        if self.heap_list[left_index] > self.heap_list[right_index]:
            return left_index
        else:
            return right_index

    # End of Helper Methods

    def add(self, element):
        """Add an element to the heap_list

        Args:
            element (_type_): The element to add
        """
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def retrieve_max(self):
        """Removes maximum value from the heap_list and reheapifies
        list.

        Returns:
            _type_: The maximum value
        """
        if self.count == 0:
            return None
        max_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        self.heapify_down()
        return max_value

    def heapify_up(self):
        """Restores the heap properties to the list after a new item is
        added."""
        index = self.count
        while self.parent_index(index) > 0:
            child = self.heap_list[index]
            parent = self.heap_list[self.parent_index(index)]
            if child > parent:
                self.heap_list[index] = parent
                self.heap_list[self.parent_index(index)] = child
            index = self.parent_index(index)

    def heapify_down(self):
        """Restores the heap properties to the list after the root is
        removed."""
        index = 1
        while self.child_present(index):
            larger_child_index = self.get_larger_child(index)
            child = self.heap_list[larger_child_index]
            parent = self.heap_list[index]
            if child > parent:
                self.heap_list[larger_child_index] = parent
                self.heap_list[index] = child
            index = larger_child_index


def heap_sort(list):
    """The algorithm to take an unsorted list and sort return a list
    sorted in ascending order.

    Args:
        list (list): An unsorted list to be sorted by the heap sort
        algorithm.

    Returns:
        sort (list): The sorted list.
    """
    sort = []
    max_heap = MaxHeap()
    for index in list:
        max_heap.add(index)
    while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        sort.insert(0, max_value)
    return sort
