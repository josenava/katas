package main

import "fmt"

func IsUnique(s string) bool {
	// O(n^2) version to achieve a more optimal one, we need to sort the string first
	if len(s) == 1 {
		return true
	}
	n := 0
	for n < len(s) {
		i := n + 1
		for i < len(s) {
			if s[n] == s[i] {
				return false
			}
			i += 1
		}
		n += 1
	}
	return true
}

func main() {
	testStrings := []string{"aabc", "cccaahg", "heydude", "abc", "b"}
	for _, testString := range testStrings {
		fmt.Printf("isUnique(%s) = %t\n", testString, IsUnique(testString))
	}
}
