from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        def sortKey(interval):
            return interval[0]
        intervals = sorted(intervals, key=sortKey)
        roomDict = {}
        numRoom = 0
        popList = []
        for i, interval in enumerate(intervals):
            tmpStart = interval[0]
            roomDict[i] = interval[1]
            for roomKey in roomDict:
                if roomDict[roomKey] <= interval[0]:
                    popList.append(roomKey)
            while popList:
                roomKey = popList.pop()
                roomDict.pop(roomKey)
            tmpRoom = len(roomDict)
            numRoom = max(numRoom, tmpRoom)
        return numRoom

if __name__ == "__main__":
    s = Solution()
    testCases = []
    testCases.append([])
    tmp = [[2,4],[3,7]]
    testCases.append(tmp)
    tmp = [7,10],[2,4]
    testCases.append(tmp)
    for testCase in testCases:
        print(s.minMeetingRooms(testCase))
