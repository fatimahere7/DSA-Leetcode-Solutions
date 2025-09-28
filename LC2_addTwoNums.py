# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.You may assume the two numbers
# do not contain any leading zero, except the number 0 itself.
# Example 1:
# Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
# Output: [7, 0, 8]
# Explanation: 342 + 465 = 807.


class ListNode:
    def __init__(self , val = 0 , next = None):   #class constructor
        self.val = val
        self.next = next

def list_to_linkedlist(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next        

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next 
    return result  

def solution(l1 ,l2):
    carry = 0
    dummy = ListNode(0)
    current = dummy
    
    while l1 != None or l2 != None or carry !=0:
        sum = carry
        if l1 != None:
            sum += l1.val
            l1= l1.next
        if l2 != None:
            sum += l2.val
            l2 = l2.next 
        carry = sum//10  # to avoid float value we use this //
        current.next = ListNode(sum%10)  
        current = current.next     
    
    return dummy.next
    
def display(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

def reverse_linkedlist(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev    


l1 = list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
l2 = list_to_linkedlist([9, 9, 9, 9])
  
display(l1)
display(l2)
res = solution(l1,l2)
display(solution(l1,l2))
print(linkedlist_to_list(res))
display(reverse_linkedlist(res))