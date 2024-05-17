# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = []

        while list1 and list2:
            if list1.val < list2.val:
                merged.append(list1.val)
                list1 = list1.next
            else:
                merged.append(list2.val)
                list2 = list2.next
        while list1:
            merged.append(list1.val)
            list1 = list1.next
        while list2:
            merged.append(list2.val)
            list2 = list2.next

        dummy = ListNode()
        curr = dummy
        for val in merged:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next            


        

        