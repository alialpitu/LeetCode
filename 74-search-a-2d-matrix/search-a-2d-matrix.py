class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = len(matrix[0])-1
        Mh = 0

        U = 0
        D =len(matrix)-1
        v = 0

        while U <= D:
            Mv = U + ((D-U)//2)
            if matrix[Mv][-1] < target:
                U = Mv + 1
            elif matrix[Mv][0] > target:
                D = Mv - 1
            else:
                break

        while L <= R:
            Mh = L + ((R-L)//2)
            if matrix[Mv][Mh] < target:
                L = Mh+1
            elif matrix[Mv][Mh] > target:
                R = Mh-1
            else:
                return True
        return False
        