package main

import (
	"fmt"
	"strconv"
	"unicode"
)

type testCase struct {
	input, expected string
}

func compressString(s string) string {
	var compressed []byte
	original := []byte(s)

	previousChar := byte(unicode.ToLower(rune(original[0])))
	var charCount int64 = 0
	for _, c := range original {
		currentChar := byte(unicode.ToLower(rune(c)))
		if currentChar != previousChar {
			compressed = append(compressed, previousChar)
			compressed = strconv.AppendInt(compressed, charCount, 10)
			charCount = 0
		}
		charCount++
		previousChar = currentChar
	}

	compressed = append(compressed, previousChar)
	compressed = strconv.AppendInt(compressed, charCount, 10)

	if len(compressed) >= len(original) {
		return s
	}

	return string(compressed)
}

func main() {
	testCases := []testCase{
		{"aabbbcccddd", "a2b3c3d3"},
		{"aaAaaA", "a6"},
		{"eeeUUUabce", "eeeUUUabce"},
		{"aabcccccaaa", "a2b1c5a3"},
	}
	for _, testCase := range testCases {
		result := compressString(testCase.input)
		fmt.Printf("compressString(%s) = %s, is_ok=%t\n", testCase.input, result, testCase.expected == result)
	}

}
