class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] # store the asteroids as they come, until collision scenario

        # when does a collision happen - postive meets negative
        for aster in asteroids:
            is_alive = True
            if stack and stack[-1] > 0 and aster < 0:
                # we have a left moving asteriod which could lead to collision
                while stack and (abs(stack[-1]) < abs(aster)) and stack[-1] > 0: 
                    # arriving asteroid is greater - 
                    stack.pop()
                if stack and (abs(stack[-1]) > abs(aster)) and stack[-1] > 0:
                    # arriving asteroid is smaller, gets destroyed
                    is_alive = False
                    pass
                if stack and (abs(stack[-1]) == abs(aster)) and stack[-1] > 0:
                    # both gets destroyed
                    stack.pop() # loop for the next element
                    is_alive = False
            
            if is_alive:
                stack.append(aster)

        return stack