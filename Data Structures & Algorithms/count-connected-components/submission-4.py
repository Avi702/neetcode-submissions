class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1]*n
        def find(n1):
            if n1 != par[n1]:
                par[n1] = find(par[n1])
            return par[n1]
        
        def union(n1,n2):
            root1 = find(n1)
            root2 = find(n2)
            if root1 == root2:
                return 0

            if rank[root1] > rank[root2]:
                rank[root1] += rank[root2]
                par[root2] = root1
            else:
                rank[root2] += rank[root1]
                par[root1] = root2
            return 1
        count = n
        for n1, n2 in edges:
            count -= union(n1,n2)
        return count


            

