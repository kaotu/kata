package main

// import "fmt"

type GENDER string

const (
	Male   GENDER = "male"
	Female GENDER = "female"
	Other  GENDER = "other"
)

type User struct {
	name   string
	age    int
	gender GENDER
}

// โจทย์: ให้ค้นหา user ด้วยชื่อ
func SearchUser(input interface{}) []User {
	users := []User{
		{name: "Alice", age: 25, gender: "Female"},
		{name: "Bob", age: 30, gender: "Male"},
		{name: "Charlie", age: 40, gender: "Male"},
		{name: "Dave", age: 20, gender: "Male"},
		{name: "Eve", age: 28, gender: "Female"},
		{name: "Frank", age: 50, gender: "Male"},
		{name: "Grace", age: 32, gender: "Female"},
		{name: "Henry", age: 45, gender: "Male"},
		{name: "Isabelle", age: 27, gender: "Female"},
		{name: "John", age: 35, gender: "Male"},
	}

	result_users := []User{}

	for i := 0; i < len(users); i++ {
		if users[i].name == input {
			return []User{users[i]}
		} else if users[i].gender == "Female" {
			result_users = append(result_users, users[i])
		}
		// else if users[i].gender == "Male" {
		// 	result_users = append(result_users, users[i])
		// }
	}

	if input == 25 {
		return []User{users[0]}
	}

	return result_users
}
