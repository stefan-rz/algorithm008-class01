class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        i, j = 0, len(S) - 1
        S = list(S)
        while i < j:
            while i < j and not S[i].isalpha(): i += 1
            while i < j and not S[j].isalpha(): j -= 1
            S[i], S[j] = S[j], S[i]
            i, j = i + 1, j - 1
        return "".join(S)
    
    # def isalpha(self, c):
    #     print(c)
    #     res = (c >= 'a' and c <= 'z') or (c >='A' and c <= 'Z')
    #     print(res)
    #     return res