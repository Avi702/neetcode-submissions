class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            alive = True
            while alive and stack and stack[-1] > 0 and i < 0:
                j = stack[-1]
                if j == abs(i):
                    stack.pop()
                    alive = False
                elif j < abs(i):
                    stack.pop()
                else:
                    alive = False
            if alive:
                stack.append(i)
        return stack