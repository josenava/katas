package main

import "fmt"

func zeroFillRow(m *[][]int, row int) {
	for i := 0; i < len((*m)[0]); i++ {
		(*m)[row][i] = 0
	}
}

func zeroFillColumn(m *[][]int, col int) {
	for j := 0; j < len((*m)); j++ {
		(*m)[j][col] = 0
	}
}

func zeroMatrix(m *[][]int) {
	rowHasZero := false
	columnHasZero := false

	for j := 0; j < len((*m)[0]); j++ {
		if (*m)[0][j] == 0 {
			rowHasZero = true
			break
		}
	}
	for i := 0; i < len((*m)); i++ {
		if (*m)[i][0] == 0 {
			columnHasZero = true
			break
		}
	}

	for i := 1; i < len((*m)); i++ {
		for j := 1; j < len((*m)[0]); j++ {
			if (*m)[i][j] == 0 {
				(*m)[i][0] = 0
				(*m)[0][j] = 0
			}
		}
	}

	for i := 1; i < len((*m)); i++ {
		if (*m)[i][0] == 0 {
			zeroFillRow(m, i)
		}
	}

	for j := 1; j < len((*m)[0]); j++ {
		if (*m)[0][j] == 0 {
			zeroFillColumn(m, j)
		}
	}

	if rowHasZero {
		zeroFillRow(m, 0)
	}

	if columnHasZero {
		zeroFillColumn(m, 0)
	}
}

func main() {
	testMatrix := [][]int{
		{2, 4, 9, 1},
		{3, 7, 0, 1},
		{0, 8, 2, 1},
	}

	fmt.Printf("zeroMatrix(%v) = \n", testMatrix)
	zeroMatrix(&testMatrix)
	fmt.Printf("= %v", testMatrix)
}
