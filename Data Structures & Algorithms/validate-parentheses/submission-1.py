class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in pairs: # 閉じ括弧のとき
                # for s="]"
                if len(stack) == 0:
                    return False
                
                last = stack.pop() # 最後の開きカッコ
                expected = pairs[c]

                if expected != last:
                    return False

            else: # 開き括弧のとき
                stack.append(c)

        return len(stack) == 0

        