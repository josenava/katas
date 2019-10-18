package main

import (
	"fmt"
	"sort"
	"strings"
)

func sortString(w string) string {
	s := strings.Split(w, "")
	sort.Strings(s)
	return strings.Join(s, "")
}

func cleanStr(s string) string {
	// removes whitespaces and sorts the string. A better implementation should
	// remove all non alphanumeric chars
	str := strings.Replace(s, " ", "", -1)
	return sortString(strings.ToLower(str))
}

func isPalindromePermutation(s string) bool {
	str := cleanStr(s)
	maxOdd := 0
	if len(str)%2 == 1 {
		// there should be an odd char count
		maxOdd = 1
	}

	bytestr := []byte(str)
	oddCount := 0
	charCount := 0
	currentChar := bytestr[0]
	for _, c := range bytestr {
		if currentChar != c {
			if charCount%2 == 1 {
				oddCount++
			}
			charCount = 0
		}
		charCount++
		currentChar = c
	}

	return oddCount <= maxOdd
}

func main() {
	testStrings := []string{
		"Tact Coa",
		"This is not a palindrome permutation",
		"Not a permutation either",
		"Wble aas I ree W sai lEba", // Able was I ere I saw Elba
		"Odvev Ned or eren",         // Never odd or even
	}
	for _, testString := range testStrings {
		fmt.Printf("isPalindromePermutation(%s) = %t\n", testString, isPalindromePermutation(testString))
	}

}
