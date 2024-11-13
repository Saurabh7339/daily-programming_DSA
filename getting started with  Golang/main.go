package main

import (
	"fmt"
	"sort"
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
	fmt.Println("hola")
	var ages [3]int = [3]int{1, 2, 3}
	fmt.Println(ages)

	names := "hey there"
	println(strings.ContainsAny(names, "hey"))
	new_slice := strings.Split(names, " ")
	fmt.Println(new_slice)

	my_new_slice := []string{"zebra", "there"}
	slice := []int{12, 2}

	sort.Strings(my_new_slice)
	fmt.Println((my_new_slice))
	fmt.Println(sort.SearchStrings(my_new_slice, "xx"))
	age := 23
	fmt.Println(age)

	x := 0
	for x <= 5 {
		fmt.Println(x)
		x++
	}
	for i := 0; i < len(my_new_slice); i++ {
		fmt.Println(my_new_slice[i])
	}

	for index, value := range my_new_slice {
		fmt.Printf("the value is %v", value)
		my_new_slice[index] = "its working"
		fmt.Println(value)
	}
	fmt.Println(my_new_slice)
	value := 70
	if value == 40 {
		fmt.Println("this is true")
	} else if value == 50 {
		fmt.Println("not 40 but", value)
	} else {
		fmt.Println("age is something else")
	}
	for _, value := range my_new_slice {
		fmt.Println(value)
	}
	name := goFunction([]string{"dante"})
	println(name)
	println(upperSplit("hey there this is a test"))

	menu := map[string]float64{
		"soup": 12.21312,
		"hey":  12312.22,
	}
	fmt.Println(menu["soup"])
	menu["soup"] = 12.1
	fmt.Println(menu)

	var my_new_array = []int{}
	for i := 0; i <= 5; i++ {
		my_new_array = append(my_new_array, i)
	}
	fmt.Println(my_new_array)

	check_value_map(menu)
	fmt.Println(menu)

	test_slice(slice)

	var my_map map[int]string = map[int]string{1: "hey there"}
	println(my_map)

	my_string := "()[{}]"
	println(balanced_brackets(my_string))

	// var _name string
	// var _age int
	// fmt.Scan(&_name, &_age)
	// fmt.Println(_name, _age)
	var e = Employee{
		Name:   "dante",
		Number: 1,
		Hired:  time.Now(),
	}
	fmt.Printf("%+[1]v\n", e)
}
