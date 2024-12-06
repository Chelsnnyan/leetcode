class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        n = []
        

        for x in range(len(intervals)):
            s = newInterval[0]
            e = newInterval[1]
            if e<intervals[x][0]:
                n.append(newInterval)
                return n + intervals[x:]
            elif s>intervals[x][1]:
                n.append(intervals[x])
            else:
                newInterval = [min(s, intervals[x][0]), max(e, intervals[x][1])]
        n.append(newInterval) 
        return n