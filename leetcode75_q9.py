"""
1. ek nayi list banauga .sorted() ka use karke

2. ek tuple banauga jisme koi bhi element repeat nahi hota!

3. touple se value leke list.count() ka use karke pata karuga ki ye kitni baar aaya h

4. .push ka use karke ek empyt list me aab dehre dehre mamala upload hoga set ka ek element push fir count ka ans jo aaya usko str() me badal k push

5. aager count ke return ki len <= 0 to khuch nahi hoga , len == 1 to direct push , aager len >=2 to hum 10% karke ans nikal ke push karege
"""


class Solution:
    def compress(self, chars) -> int:
        unique_numbers = list(dict.fromkeys(chars))
        totalADD = len(unique_numbers)
        for __unique_numbers in range(0, len(unique_numbers)):
            if len((str(chars.count(unique_numbers[__unique_numbers])))) > 1 :
             totalADD += len((str(chars.count(unique_numbers[__unique_numbers]))))
            else :
               continue 
        return totalADD


SolutionObj = Solution()
# chars = ["a", "a", "b", "b", "c", "c", "c"]
chars = ["a"]
print(SolutionObj.compress(chars))
