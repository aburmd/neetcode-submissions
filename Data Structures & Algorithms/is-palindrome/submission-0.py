class Solution:
    def alphaNum(self,c):
        return (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
        l,r=0,len(s)-1
        s=s.lower()
        while l<r:
            if not self.alphaNum(s[l]) and not self.alphaNum(s[r]):
                l+=1
                r-=1
                continue
            elif not self.alphaNum(s[l]):
                l+=1
                continue
            elif not self.alphaNum(s[r]):
                r-=1
                continue
            else:
                if s[l]!=s[r]:
                    return False
                else:
                    l+=1
                    r-=1
        return True

        