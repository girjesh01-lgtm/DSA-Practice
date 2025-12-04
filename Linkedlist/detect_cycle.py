class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_cycle(head):
    slow = fast = head

    # Step 1: Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        print(f"slow = {slow.val}, fast = {fast.val}")

        if slow == fast:
            break
    else:
        return None  # No cycle

    # Step 2: Find start of cycle
    slow = head
    print("\nafter detecting the cycle\n")
    print(f"slow = {slow.val}, fast = {fast.val}")
    while slow != fast:
        slow = slow.next
        fast = fast.next
        print(f"slow = {slow.val}, fast = {fast.val}")
    return slow  # Start of the cycle node


# Creating the nodes
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)



# Linking the nodes
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n4

cycle_start = detect_cycle(n1)
print(cycle_start.val if cycle_start else "No Cycle")