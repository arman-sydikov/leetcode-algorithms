from typing import List
import math

class Solution:
    def findMedianSortedArrays(self, top: List[int], bottom: List[int]) -> float:
        if len(top) > len(bottom):
            top, bottom = bottom, top
        
        left = 0
        right = len(top)
        answer = 0
        while left <= right:
            
            # Calculate top and bottom middle index
            topIndex = (left+right)//2
            bottomIndex = (len(top)+len(bottom)+1)//2 - topIndex

            # Set top left and right
            topLeft, topRight = -math.inf, math.inf
            if topIndex > 0:
                topLeft = top[topIndex-1]
            if topIndex < len(top):
                topRight = top[topIndex]

            # Set bottom left and right
            bottomLeft, bottomRight = -math.inf, math.inf
            if bottomIndex > 0:
                bottomLeft = bottom[bottomIndex-1]
            if bottomIndex < len(bottom):
                bottomRight = bottom[bottomIndex]
            
            # Binary search
            if bottomLeft > topRight:
                left = topIndex+1
                continue
            if topLeft > bottomRight:
                right = topIndex-1
                continue

            # Found solution
            if (len(top)+len(bottom))%2 == 0:
                answer = (max(topLeft, bottomLeft) + min(topRight, bottomRight)) / 2
            else:
                answer = max(topLeft, bottomLeft)
            break
        return answer


top = [5,6]
bottom = [1,2,3,4,7]
solution = Solution()
print(solution.findMedianSortedArrays(top, bottom))