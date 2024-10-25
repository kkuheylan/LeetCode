class Solution(object):
    def asteroidCollision(self, asteroids):
        negative = []
        positive = []

        for i in asteroids:
            if i < 0:
                while positive and positive[-1] < abs(i):
                    positive.pop()
                if positive and positive[-1] == abs(i):
                    positive.pop()
                elif not positive:
                    negative.append(i)
            else:
                positive.append(i)

        return negative + positive
    