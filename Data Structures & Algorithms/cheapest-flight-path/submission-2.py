class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')]*n# kepps track of price to get to destination from starting point
        prices[src] = 0 
        for _ in range(k+1):# number of flights
            curr_prices = prices.copy()
            for s,d,p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < curr_prices[d]:
                    curr_prices[d] = prices[s] + p 
            prices = curr_prices
        return prices[dst] if prices[dst] != float('inf') else -1

        