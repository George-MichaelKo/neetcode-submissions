class Solution:
    def romanToInt(self, s: str) -> int:
        hashD = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        prev = 0
        total = 0 
        for char in s:
            total +=  hashD[char]
            if prev < hashD[char]:
                total -= 2 * prev
            prev = hashD[char]
        return total

        