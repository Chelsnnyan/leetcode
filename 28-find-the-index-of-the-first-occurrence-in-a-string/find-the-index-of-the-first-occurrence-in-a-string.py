class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ln = len(needle)
        first = needle[0]
        for i in range(len(haystack)):
            if haystack[i] == first:
                if haystack[i:i+ln] == needle:
                    return i
        return -1



    


