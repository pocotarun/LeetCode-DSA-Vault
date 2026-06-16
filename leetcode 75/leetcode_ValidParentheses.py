"""Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false
"""
""" 
class Solution:
    def isValid(self, s: str):
        slist= list(s)
        if(len(s) % 2 != 0):
            return False
        else:
            # # phase1
            # if(slist.count("(") != slist.count(")")) or (slist.count("[") or slist.count("]")) or (slist.count("{") != slist.count("}")):
            #     return False
            
            # i use 2 pointer approach
            for i in range(0,len(slist)//2, 2):
                if slist[i] in ["{","[","("]:
                    return True 



            # if(slist.count("("))    
            




        return True  

 """

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        box = []
        partner = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char in ['(', '[', '{']:
                box.append(char)
            else:
                if not box:
                    return False
                last_opened = box.pop()
                if last_opened != partner[char]:
                    return False
        return len(box) == 0


# >>>>>>>>>>>>>>>> TEST PHASE DONT READ
s: str = "([)]"
s2: str = "([])"
s3: str = "(]"
s4: str = "()[]{}"
s5: str = "()"
sol = Solution()
print(sol.isValid(s),sol.isValid(s2),sol.isValid(s3),sol.isValid(s4),sol.isValid(s5))

