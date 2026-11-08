class Solution:
    def isValid(self, s: str) -> bool:
        pairs ={
            "(":")",
            "{":"}",
            "[":"]"
        }

        stack = []

        for c in s:
            if c in pairs:
                # 対応すると閉じ括弧を追加
                stack.append(pairs[c])
            else:
                # 対応する閉じ括弧がない場合
                if not stack:
                    return False
                
                # 一番上の閉じ括弧と一致するか確認
                if stack.pop() != c:
                    return False
        
        return len(stack) == 0
