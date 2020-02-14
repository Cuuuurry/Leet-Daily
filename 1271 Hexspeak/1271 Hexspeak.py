class Solution:
    def toHexspeak(self, num: str) -> str:
        num = int(num)
        finalString = ""
        hexDict = {0: "O", 1: "I", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        while num > 0:
            res = num % 16
            quotient = num // 16
            if 1 < res < 10:
                return "ERROR"
            finalString = hexDict[res] + finalString
            num = quotient

        return finalString
