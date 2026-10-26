class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen={')':'(','}':'{',']':'['}
        stack=[]
        l,r=0,len(s)-1
        for c in s:
            if stack and c in closeToOpen and stack[-1]==closeToOpen[c]:
                stack.pop()
                continue
            stack.append(c)
        if not stack:
            return True
        return False
            
        