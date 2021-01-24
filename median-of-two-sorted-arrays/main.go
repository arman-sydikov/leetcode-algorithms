package main

import "math"

// 4. Median of Two Sorted Arrays
// https://leetcode.com/problems/median-of-two-sorted-arrays
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	if len(nums1) > len(nums2) {
		return findMedianSortedArrays(nums2, nums1)
	}
	left := 0
	right := len(nums1)
	middle := (len(nums1) + len(nums2) + 1) / 2
	var answer float64
	for left <= right {
		middle1 := left + (right-left)/2
		middle2 := middle - middle1

		max1, min1 := math.MinInt32, math.MaxInt32
		if middle1 > 0 {
			max1 = nums1[middle1-1]
		}
		if middle1 < len(nums1) {
			min1 = nums1[middle1]
		}
		max2, min2 := math.MinInt32, math.MaxInt32
		if middle2 > 0 {
			max2 = nums2[middle2-1]
		}
		if middle2 < len(nums2) {
			min2 = nums2[middle2]
		}

		if max1 > min2 {
			right = middle1 - 1
			continue
		}
		if max2 > min1 {
			left = middle1 + 1
			continue
		}

		if (len(nums1)+len(nums2))%2 == 0 {
			answer = float64(max(max1, max2)+min(min1, min2)) / 2
		} else {
			answer = float64(max(max1, max2))
		}
		break
	}
	return answer
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}
