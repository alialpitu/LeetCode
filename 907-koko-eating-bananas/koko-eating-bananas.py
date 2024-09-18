class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
            L = 1
            R = max(piles)
            piles = sorted(piles)

            while L <= R:
                k = 0
                m = (L + R) // 2
                for i in piles:
                    k += math.ceil(i/m)
                if k > h:
                    L = m + 1
                elif k <= h:
                    R = m - 1

            return(L)  