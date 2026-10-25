class Solution:
    def alpnum(self, c:str):
        return (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        if len(s)<=0:
            return True
        while left<=right:
            if not self.alpnum(s[left].lower()):
                left+=1
                continue
            if not self.alpnum(s[right].lower()):
                right-=1
                continue
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
            
        