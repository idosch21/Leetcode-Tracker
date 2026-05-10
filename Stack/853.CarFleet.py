class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        size = len(position)
        posNspeed = [[pos,speed] for pos,speed in zip(position,speed)]

        stack = []

        for pos,speed in sorted(posNspeed)[::-1]:
            stack.append((target -pos) /speed)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
