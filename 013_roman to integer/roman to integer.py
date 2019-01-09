class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        for i in range(0,len(s)-1):
            ch = s[i]
            chNext = s[i+1]
            if dict[ch]<dict[chNext]:
                ans -= dict[ch]
            else:
                ans += dict[ch]
        ans += dict[s[-1]]
        return ans
