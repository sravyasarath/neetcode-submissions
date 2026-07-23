class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleanstr= "".join(txt.lower() for txt in s if txt.isalnum())
        #print(cleanstr)
        left=0
        right=len(cleanstr)-1
        while(left<right):
            if cleanstr[left]!=cleanstr[right]:
                return False
            left+=1
            right-=1
        return True        
        