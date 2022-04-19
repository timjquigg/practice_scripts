import random

def bubblesort(list):
    """This is a basic implementation of the bubble sort algorithm

    Args:
        list (list): This is the list that you would like to sort

    Returns:
        list: The sorted list
    """
    for item in list:
        for i in range(len(list) - 1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list

#For testing
test_list = []
for i in range(10):
    test_list.append(random.randint(0,100))

print(test_list)
print(bubblesort(test_list))