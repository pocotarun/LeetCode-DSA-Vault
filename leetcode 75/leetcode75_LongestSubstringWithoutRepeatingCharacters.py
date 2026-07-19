"""Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letarr: list = []
        s = str(s)

        return 0


# only for test :) dont read >>>
letstr: str = "qwertyuiop"
letstr2: str = "qwertyuioppoiuytrewq"
sol = Solution()
print(sol.lengthOfLongestSubstring(letstr))




""" 
लॉजिक हिंट (Sliding Window Approach):
1. एक "window" इमेजिन करो जो स्ट्रिंग के ऊपर स्लाइड करती है। हम इस विंडो को दो pointers से ट्रैक करेंगे: `left` और `right`, दोनों 0 इंडेक्स से शुरू होंगे।
2. हमें याद रखना होगा कि हमारी विंडो में अभी कौन-कौन से characters हैं ताकि डुप्लीकेट्स (duplicates) न आएं। इसके लिए Python का `set` सबसे बेस्ट है।
3. अब `right` पॉइंटर को एक-एक करके आगे बढ़ाओ:
   - अगर s[right] वाला कैरेक्टर हमारे `set` में नहीं है:
     बहुत बढ़िया! इसे `set` में डाल दो। हमारी विंडो अभी वैलिड है। अपनी "maximum length" वाले वेरिएबल को अपडेट कर लो अगर अभी की विंडो का साइज़ (right - left + 1) पहले से बड़ा है।
   - अगर s[right] वाला कैरेक्टर पहले से हमारे `set` में है:
     यहाँ एक डुप्लीकेट आ गया! अब हमें अपनी विंडो को लेफ्ट साइड से छोटा करना होगा। s[left] वाले कैरेक्टर को `set` से हटाओ और `left` पॉइंटर को 1 कदम आगे बढ़ाओ। यह तब तक करते रहो जब तक वो डुप्लीकेट कैरेक्टर विंडो से बाहर न निकल जाए।
4. जैसे ही डुप्लीकेट हट जाए, तुम s[right] वाले कैरेक्टर को आराम से `set` में डाल सकते हो और `right` पॉइंटर को आगे बढ़ाना जारी रख सकते हो।
5. यह प्रोसेस तब तक रिपीट करो जब तक `right` पॉइंटर स्ट्रिंग के अंत तक न पहुँच जाए।
"""