# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        # 今見ているノードがある間、繰り返す
        while current is not None:
            # つながりを変える前に、元の次のノードを覚えておく
            next_node = current.next

            # 今のノードの行き先を逆順につなぎ直した部分の先頭に変える
            current.next = prev

            # 今のノードを、つなぎ直した部分の新しい先頭にする
            prev = current

            # 覚えておいた元の次のノードに移り、次の処理に進む
            current = next_node

        return prev
        