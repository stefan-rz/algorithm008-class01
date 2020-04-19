class Solution:
    def firstUniqChar(self, s: str) -> str:
        # dic 是一个有序字典
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v: return k
        return ' '