class Listnode:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next
class Solution:
    def mergetwolist(self,list1,list2):
        dummy=Listnode(0)
        current=dummy
        while list1 and list2:
            if list1.value<list2.value:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        if list1:
            current.next=list1
        if list2:
            current.next=list2
        return dummy.next
list1 = Listnode(1)
list1.next = Listnode(3)
list1.next.next = Listnode(5)

# Create second list
list2 = Listnode(2)
list2.next = Listnode(4)
list2.next.next = Listnode(6)

obj = Solution()

result = obj.mergetwolist(list1, list2)

while result:
    print(result.value, end=" ")
    result = result.next

