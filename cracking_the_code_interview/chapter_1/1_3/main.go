package main

import "fmt"

type TestString struct {
	value      string
	trueLength int
}

func Urlify(s TestString) string {
	nspaces := 0
	for i := 0; i < s.trueLength; i++ {
		if s.value[i] == ' ' {
			nspaces++
		}
	}
	if nspaces == 0 {
		return s.value
	}
	bytestr := []byte(s.value)
	index := s.trueLength + nspaces*2
	for i := s.trueLength - 1; i >= 0; i-- {
		if bytestr[i] == ' ' {
			bytestr[index-3] = '0'
			bytestr[index-2] = '2'
			bytestr[index-1] = '%'
			index -= 3
		} else {
			bytestr[index-1] = bytestr[i]
			index--
		}

	}
	return string(bytestr)
}

func main() {
	testStrings := []TestString{
		{"Hey dude  ", 8},
		{"Mr John Smith    ", 13},
		{"What a wonderful day      ", 20},
		{"heydude", 7},
	}
	for _, testString := range testStrings {
		fmt.Printf("Urlify(%v) = %s\n", testString, Urlify(testString))
	}
}
