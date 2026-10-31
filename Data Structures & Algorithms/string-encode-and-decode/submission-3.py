class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            length = len(word)          # "cat" なら 3
            result += str(length) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0  # 今から読む位置

        while i < len(s):
            # 文字数と本文の境目にある "#" を探す
            j = s.index("#", i)

            # i から "#" の手前までが文字数
            length = int(s[i:j])

            # 本文は "#" の次から始まる
            start = j + 1

            # start から length 文字を取り出す
            word = s[start:start + length]
            result.append(word)

            # 次の文字数が書いてある位置に進む
            i = start + length

        return result
