package main

import (
	"testing"
)

func Test(t *testing.T) {

	tests := []struct {
		name     string
		nums1    []int
		nums2    []int
		expected float64
	}{
		{name: "Example1", nums1: []int{1, 3}, nums2: []int{2}, expected: 2.0},
		{name: "Example2", nums1: []int{1, 2}, nums2: []int{3, 4}, expected: 2.5},
		{name: "Example3", nums1: []int{0, 0}, nums2: []int{0, 0}, expected: 0.0},
		{name: "Example4", nums1: []int{}, nums2: []int{1}, expected: 1.0},
		{name: "Example5", nums1: []int{2}, nums2: []int{}, expected: 2.0},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := findMedianSortedArrays(test.nums1, test.nums2)
			if got != test.expected {
				t.Errorf("got %.2f want %.2f", got, test.expected)
			}
		})
	}
}
