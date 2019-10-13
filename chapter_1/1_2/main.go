package main

import (
	"fmt"
	"sort"
	"strings"
)

type StringPairs struct {
	A, B string
}

func SortString(w string) string {
	s := strings.Split(w, "")
	sort.Strings(s)
	return strings.Join(s, "")
}

func IsPermutation(a, b string) bool {
	if len(a) != len(b) {
		return false
	}

	return SortString(a) == SortString(b)
}

func main() {
	testStrings := []StringPairs{
		{"aabc", "cccaahg"},
		{"abbbaa", "aaabbb"},
		{"bbbaa", "caada"},
		{"ababa", "bbaaa"},
		{"12345", "21435"},
	}
	for _, testString := range testStrings {
		fmt.Printf("IsPermutation(%s, %s) = %t\n", testString.A, testString.B, IsPermutation(testString.A, testString.B))
	}
}
