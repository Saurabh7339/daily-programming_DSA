package main

import (
	"fmt"
	// "sort"
	"strings"
	"time"
)

type Employee struct {
	Name   string
	Number int
	Boss   *Employee
	Hired  time.Time
}

func balanced_brackets(s string) bool {

	stack := []rune{}
	brackets_map := map[rune]rune{')': '{', '}': '(', ']': '['}
	///
	for _, value := range s {

		for key, key_value := range brackets_map {
			if key_value == value {
				stack = append(stack, value)
			}
			if key == value {
				println(key)
				if len(stack) == 0 {
					return false
				}
				top := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				if top != brackets_map[key] {
					return false
				}
			}
		}
	}
	println(stack)
	if len(stack) != 0 {
		return false
	} else {
		return true
	}

}

func goFunction(n []string) string {
	fmt.Println("hey there", n)
	return "dante is boss"
}
func upperSplit(n string) (string, string) {
	upper_str := strings.ToUpper(n)
	fmt.Println(upper_str)
	str_list := strings.Split(upper_str, " ")
	return str_list[0], str_list[1]
}

func check_value_map(v map[string]float64) {
	v["soup"] = 1.1
}

func test_slice(arr []int) {
	for index, value := range arr {
		println(index, value)
	}
}

func main() {
	var total_prices []int = []int{7, 1, 5, 3, 6, 4}
	profit := maxProfit(total_prices)
	fmt.Println(profit)

	nums := []int{1, 2, 3, 4, 5, 6, 7}
	k := 3
	fmt.Println(rotated(nums, k))
}
