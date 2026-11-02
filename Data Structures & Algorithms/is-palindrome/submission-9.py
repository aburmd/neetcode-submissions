class Solution:
    def alphanum(self,c):
        return ord('a')<=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9')
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        s=s.lower()
        while l<r:
            if not self.alphanum(s[l]) and not self.alphanum(s[r]):
                l+=1
                r-=1
                continue
            elif not self.alphanum(s[l]):
                l+=1
                continue
            elif not self.alphanum(s[r]):
                r-=1
                continue
            else:
                if s[l]!=s[r]:
                    return False
                else:
                    l+=1
                    r-=1
        return True

        