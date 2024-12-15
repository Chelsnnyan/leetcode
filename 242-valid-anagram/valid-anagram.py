class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        di = {}
        for i in s:
            if i not in di:
                di[i] = 1
            else:
                di[i]+=1
        for j in t:
            if j not in d:
                d[j] = 1
            else:
                d[j]+=1
        return d==di
