# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_array_using_linked_list(arr):
    head = None

    # Step 1: Build linked list by inserting at head
    for value in arr:
        new_node = Node(value)
        new_node.next = head
        head = new_node

    # Step 2: Convert linked list back to array
    reversed_arr = []
    current = head
    while current:
        reversed_arr.append(current.data)
        current = current.next

    return reversed_arr


# Example
arr = [1, 2, 3, 4, 5]
print(reverse_array_using_linked_list(arr))
# Output: [5, 4, 3, 2, 1]
