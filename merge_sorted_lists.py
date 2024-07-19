class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2): #This solution is for two arrays
        final = []
        p1 = 0
        p2 = 0
        while(p1 < max(len(list1),len(list2)) or p2 < max(len(list1),len(list2))):
            if(p1 == len(list1)):
                final = final + list2[p2:len(list2)]
                break
            if(p2 == len(list2)):
                final = final + list1[p1:len(list1)]
                break
            else:
                if(list1[p1] < list2[p2]):
                    final.append(list1[p1])
                    p1 = p1 + 1

                elif(list1[p1] > list2[p2]):
                    final.append(list2[p2])
                    p2 = p2 + 1

                else:
                    final.append(list1[p1])
                    p1 = p1 + 1
                    final.append(list2[p2])
                    p2 = p2 + 1

        return final

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next               
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
        if list1 or list2:
            if list1:
                cur.next = list1
            else:
                cur.next = list2
        return head.next
                
                


a = Solution()
print(a.mergeTwoLists([1,2,3,4],[2,3]))
