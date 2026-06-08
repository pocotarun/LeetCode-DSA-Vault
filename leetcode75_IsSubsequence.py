class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index: int = 0  
        
        # 1. Loop ko len(s) tak chalaya taaki aakhri character bhi check ho
        for i in range(0, len(s)):
            
            # 2. .find() ka result ek variable mein save kar liya
            found_index = t.find(s[i], index)
            
            if found_index != -1: 
                # Agar character mil gaya, to agla search uske aage se shuru hoga
                index = found_index + 1
            else:
                # Agar ek bhi character nahi mila, to yahin se False return kar do
                return False
                
        # 3. Jab poora loop bina ruke khatam ho jaye, iska matlab saare characters mil gaye!
        return True  

# Test karne ke liye
s: str = "abc"
t: str = "ahbgdc"
solu = Solution()
print(solu.isSubsequence(s, t))  # Output: True