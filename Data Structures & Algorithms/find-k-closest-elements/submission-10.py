class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = float('inf')
        window = 0
        start_i = 0
        L = 0
        R = 0
        while R < len(arr):
            window += abs(arr[R]-x)
            if R - L + 1 == k:
                if res > window:
                    res = window
                    start_i = L
                window -= abs(arr[L]-x)
                L += 1
            R+=1
        return arr[start_i:start_i+k]



            
        
        

            