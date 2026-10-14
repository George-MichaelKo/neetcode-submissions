class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = list()
        hashMap = {2:['a','b', 'c'],3:['d','e', 'f'],4:['g','h', 'i'],5:['j','k', 'l'],6:['m','n', 'o'],7:['p','q', 'r', 's'],8:['t','u', 'v'],9:['w','x', 'y','z']}
        n = len(digits)
        if n == 0:
            return []
        def backtrack(i, combination):
            if len(combination) == n:
                result.append("".join(combination))
                return 

            for char in hashMap[int(digits[i])]:
                combination.append(char)
                backtrack(i+1, combination)   
                combination.pop()
        
        backtrack(0,[])
        return result

        