package iteration

func Repeat(s string) string {
	ans := ""
	for i := 0; i < 5; i++ {
		ans += s
	}
	return ans
}
