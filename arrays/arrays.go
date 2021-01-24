package arrays

func Sum(numbers []int) int {
	sum := 0
	for _, num := range numbers {
		sum += num
	}
	return sum
}

func SumAll(arrays ...[]int) []int {
	sums := []int{}
	for _, array := range arrays {
		sums = append(sums, Sum(array))
	}
	return sums
}

func SumAllTails(arrays ...[]int) []int {
	tails := []int{}
	for _, array := range arrays {
		tail := 0
		if len(array) > 0 {
			tail = Sum(array[1:])
		}
		tails = append(tails, tail)
	}
	return tails
}
