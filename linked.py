class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            if l1:
                x = l1.val
            else:
                x = 0

            if l2:
                y = l2.val
            else:
                y = 0

            total = x + y + carry

            carry = total // 10

            current.next = ListNode(total % 10)

            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
    
# Create Linked List 1: 2 -> 4 -> 3
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Create Linked List 2: 5 -> 6 -> 4
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Create Solution object
obj = Solution()

# Call function
result = obj.addTwoNumbers(l1, l2)

# Print Linked List
print("Result Linked List:")

while result:
    print(result.val, end=" ")
    result = result.next