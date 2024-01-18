

import heapq 
class Solution:
    def overlap(self, a, b):
        print( f'Checking overlap for : {a} and {b} ')
        a_start = a[0]
        a_end = a[1]
        b_start = b[0]
        b_end = b[1]
        overlapping = False 
        if a_end > b_start: 
            overlapping = True 
        if not overlapping:
            return None 
        else:
            return [ a_start, max(a_end, b_end) ]

    def merge(self, intervals):
        heapq.heapify(intervals)
        merged = [ heapq.heappop(intervals) ] 
        while( intervals ):
            interval = heapq.heappop(intervals)
            if self.overlap( merged[-1], interval):
                merged[-1] = self.overlap( merged[-1], interval)
            else:
                merged.append( interval )
        return merged
    
if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    sol = Solution()
    print( sol.merge( intervals ) ) 
    