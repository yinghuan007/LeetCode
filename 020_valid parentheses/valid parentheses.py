class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        newList = []
        para = ["[]","{}","()"]
        for i in range(0,len(s)):
            newList.append(s[i])
            if len(newList)>=2 and (newList[-2] + newList[-1] in para):
                newList.pop()
                newList.pop()
        return len(newList)==0
