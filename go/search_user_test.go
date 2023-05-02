package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSearchHenryShouldBeReturnDataOfHenry(t *testing.T) {
	assert := assert.New(t)

	expected := SearchUser("Henry")
	actual := []User{
		{name: "Henry", age: 45, gender: "Male"},
	}

	assert.Equal(actual, expected)
}

func TestSearchAgeIs25ShouldBeReturnDataOfAlice(t *testing.T) {
	assert := assert.New(t)

	expected := SearchUser(25)
	actual := []User{
		{name: "Alice", age: 25, gender: "Female"},
	}

	assert.Equal(actual, expected)
}

func TestSearchNameIsabelleShouldReturnDataOfIsabelle(t *testing.T) {
	assert := assert.New(t)

	expected := SearchUser("Isabelle")
	actual := []User{
		{name: "Isabelle", age: 27, gender: "Female"},
	}

	assert.Equal(actual, expected)
}

func TestSearchGenderIsFemaleShouldBeReturnArrayInvolveFemale(t *testing.T) {
	assert := assert.New(t)

	expected := SearchUser("Female")
	actual := []User{
		{name: "Alice", age: 25, gender: "Female"},
		{name: "Eve", age: 28, gender: "Female"},
		{name: "Grace", age: 32, gender: "Female"},
		{name: "Isabelle", age: 27, gender: "Female"},
	}

	assert.Equal(actual, expected)
}

// func TestSearchGenderIsMaleShouldBeReturnArrayInvolveFemale(t *testing.T) {
// 	assert := assert.New(t)

// 	expected := SearchUser("Male")
// 	actual := []User{
// 		{name: "Bob", age: 30, gender: "Male"},
// 		{name: "Charlie", age: 40, gender: "Male"},
// 		{name: "Dave", age: 20, gender: "Male"},
// 		{name: "Frank", age: 50, gender: "Male"},
// 		{name: "Henry", age: 45, gender: "Male"},
// 		{name: "John", age: 35, gender: "Male"},
// 	}

// 	assert.Equal(actual, expected)
// }
