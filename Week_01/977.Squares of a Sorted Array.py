class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ## Method 1: beat 39.27%
        # n = len(A) - 1
        # i, j = 0, n
        # cur = j
        # res = [0 for i in range(n + 1)]

        # while A[i] <= 0 and A[j] > 0:
        #     if (A[i] ** 2 >= A[j] ** 2):
        #         res[cur] = A[i] ** 2
        #         cur -= 1
        #         i += 1
        #     else:
        #         res[cur] = A[j] ** 2
        #         cur -= 1
        #         j -= 1

        # while i <= j and A[i] <= 0:
        #     res[cur] = A[i] ** 2
        #     cur -= 1
        #     i += 1

        # while i <= j and A[j] > 0:
        #     res[cur] = A[j] ** 2
        #     cur -= 1
        #     j -= 1

        # return res

        ##Method 2: no difference 
        # i, j = 0, 0
        # res = []
        # N = len(A)
        # while j < N and A[j] < 0:
        #     j += 1
        # i = j - 1
        
        # while i >= 0 and j < N:
        #     if A[i] ** 2 > A[j] ** 2:
        #         res.append(A[j] ** 2)
        #         j += 1
        #     else:
        #         res.append(A[i] ** 2)
        #         i -= 1
        # while i >= 0:
        #     res.append(A[i]**2)
        #     i -= 1
        # while j < N:
        #     res.append(A[j]**2)
        #     j += 1
        # return res
        
        # Method 3: 
        #https://leetcode.com/problems/squares-of-a-sorted-array/discuss/578910/Python%3A-O(N)-Solution
        m =[abs(s) for s in A]
        m.sort()
        l =[w*w for w in m ]
        return l