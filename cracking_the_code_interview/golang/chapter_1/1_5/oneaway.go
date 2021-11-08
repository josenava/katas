package main

import (
	"fmt"
	"math"
)

type StringTuple struct {
	input, output string
}

func isOneAway(output, input string) bool {
	if math.Abs(float64(len(output)-len(input))) > 1 {
		return false
	}

	maxDiff := 1
	totalDiff := 0

	var minLenByteStr, maxLenByteStr []byte
	var minLength int

	if len(output) < len(input) {
		minLenByteStr = []byte(output)
		minLength = len(output)
		maxLenByteStr = []byte(input)
	} else {
		minLenByteStr = []byte(input)
		minLength = len(input)
		maxLenByteStr = []byte(output)
	}
	for i := 0; i < minLength; i++ {
		if maxLenByteStr[i] != minLenByteStr[i] && i < len(maxLenByteStr)-1 && maxLenByteStr[i+1] != minLenByteStr[i] {
			totalDiff++
		}
	}
	return totalDiff <= maxDiff
}

func main() {
	testStrings := []StringTuple{
		{"TestString", "Test"},
		{"Heydude", "Heydud"},
		{"eydude", "Heydude"},
		{"pale", "ple"},
		{"what", "whal"},
		{"nole", "hole"},
		{"aabbb", "aabbbc"},
		{"lolo", "whaa"},
	}
	for _, testString := range testStrings {
		fmt.Printf("isOneAway(%s, %s) = %t\n", testString.output, testString.input, isOneAway(testString.output, testString.input))
	}

}
