# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.Merge the two lists into one sorted list.
# The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Example 1: Input: list1 = [1, 2, 4], list2 = [1, 3, 4]  Output: [1, 1, 2, 3, 4, 4]
# Example 2: Input: list1 = [], list2 = [] Output: []
# Example 3: Input: list1 = [], list2 = [0]  Output: [0]
class ListNode:
    def __init__(self, val=0, next=None):  # class constructor
        self.val = val
        self.next = next


def list_to_linkedlist(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next
def mergeTwoLists(head1,head2):
    # base case
    if not head1:
        return head2
    if not head2:
        return head1
    
    #recursive case
    if head1.val < head2.val:
        head1.next = mergeTwoLists(head1.next , head2)
        return head1
    else:
        head2.next = mergeTwoLists(head1 , head2.next)
        return head2
    

def display(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

list1 = list_to_linkedlist([1,3,5])
list2 = list_to_linkedlist([1,2,6])

display(mergeTwoLists(list1,list2))

    
    
    