import heapq

class Solution:
    # Solution 1 | minHeap | Runtime: 49.95% & Memory: 82.34% | NeetCode
    def findMaximizedCapital(self, k, w, profits, capital):

        maxProfit = [] # include the affordable projects only
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)

        for i in range(k):
            
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -1 * p)
            if not maxProfit:
                break
            w += -1 * heapq.heappop(maxProfit)

        return w
        
test = Solution()
print(test.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]) == 4)
print(test.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]) == 6)