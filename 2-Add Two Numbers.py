# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            temp = ListNode()
            current = temp

            carry = 0
            while l1 or l2 or carry:
                total = 0
                total += l1.val if l1 else 0
                total += l2.val if l2 else 0
                total +=carry

                carry = total // 10
                num = total % 10

                current.next = ListNode(num)
                current = current.next

                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None


            return temp.next





s = Solution()

def buildln(l):
    head = None
    ret = []
    for i in l:
        node = ListNode(i)
        node.next = head
        head = node
    return head
l1 = [2,4,3]
l2 = [5,6,4]
li1 = buildln(l1[::-1])
li2 = buildln(l2[::-1])


def getlnval(l):
    current = l
    while current is not None:
        print(current.val)
        current = current.next
retval = s.addTwoNumbers(li1, li2)

getlnval(retval)
