class Solution:
    def __init__(self):
        self.dct={1:1,2:2}
    def climbStairs(self, n: int) -> int:
        if n==1:
            return self.dct[1]
        if n==2:
            return self.dct[2]
        if n not in self.dct:
            self.dct[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.dct[n]


        