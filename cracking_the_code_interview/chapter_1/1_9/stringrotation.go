package main

import (
	"fmt"
	"strings"
)

type testCase struct {
	a, b     string
	expected bool
}

func isRotation(s1, s2 string) bool {
	if len(s1) != len(s2) || len(s1) == 0 {
		return false
	}

	substring := s1 + s1
	return strings.Contains(substring, s2)
}

func main() {
	testCases := []testCase{
		{"erbottlewat", "waterbottle", true},
		{"eyheh", "lololo", false},
	}

	for _, testCase := range testCases {
		result := isRotation(testCase.a, testCase.b)
		fmt.Printf("isRotation(%s, %s) = %t, test_ok=%t\n", testCase.a, testCase.b, result, testCase.expected == result)
	}
}
