# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        node = []
        curr = head

        while curr:
            node.append(curr)
            curr = curr.next
    

        l, r = 0, len(node) - 1

        while l < r:
            node[l].next = node[r]
            l += 1
            if l >= r:
                break
            node[r].next = node[l]
            r -= 1

        node[l].next = None






        # slow, fast = head, head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        

        # curr = slow.next
        # prev = slow.next = None

        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        
        # first, second = head, prev

        # while second:
        #     tmp1, tmp2 = first.next, second.next
        #     first.next = second
        #     second.next = tmp1
        #     first, second = tmp1, tmp2

   


       



        
        


        