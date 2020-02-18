class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, date = date.split("-")
        daysDict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
                    8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        year = int(year)
        month = int(month)
        date = int(date)
        if not year % 4:
            daysDict[2] = 29
        if not year % 100:
            daysDict[2] = 28
        if not year % 400:
            daysDict[2] = 29

        print(year, month, date)
        pastDate = 0
        for i in range(1, month):
            pastDate += daysDict[i]
        pastDate += date
        return pastDate