class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        L = 0; R = len(people) - 1
        count = 0
        while L <= R:
            if people[R] + people[L] <= limit:
                L+=1
            R-=1
            count+=1
        return count
            