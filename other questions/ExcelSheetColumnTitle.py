""" 
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"

Constraints:
    1 <= columnNumber <= 231 - 1
 """


""" 
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
      myDist = {i: chr(64 + i) for i in range(1, 27)}
      if int(columnNumber) < 0:
        return "NULL"
      else:    
        count = 0
        returnList = []
        while columnNumber > 26:
            columnNumber-=26
            count +=1
        if count > 0 :
            for i in range(1,count,1):
                returnList.append("A")
        else :
            returnList.append(chr(columnNumber))
            return str(returnList)  
               """    

        
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            # 1-based indexing ko 0-based banane ke liye -1 kiya
            columnNumber -= 1
            
            # 26 se divide karke remainder nikala (yeh hume current letter dega)
            remainder = columnNumber % 26
            
            # Remainder ko letter mein convert karke list mein dala (0 -> A, 1 -> B...)
            result.append(chr(65 + remainder))
            
            # Agle letter ke liye number ko chota kiya
            columnNumber //= 26
            
        # Kyunki humne peeche se letters nikale hain, isliye reverse karke jod denge
        return "".join(reversed(result))



# only for test dont read
columnNumber = 28
sol = Solution()
print(sol.convertToTitle(columnNumber))