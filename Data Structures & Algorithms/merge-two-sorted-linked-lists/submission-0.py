# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # 仮の先頭
        tail = dummy        # 答えの最後尾

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1       # 小さいほうをつなぐ
                list1 = list1.next      # list1を次へ進める
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next# 答えの最後尾を進める

        # 片方が空になったら、もう片方の残りをつなぐ
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next  # 仮の先頭を除いて返す
