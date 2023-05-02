package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestInput3ShouldBeReturnFizz(t *testing.T) {
	assert := assert.New(t)

	expected := FizzBuzz(3)
	actual := "Fizz"

	assert.Equal(expected, actual)
}

func TestInput5ShouldReturnBuzz(t *testing.T) {
	assert := assert.New(t)

	expected := FizzBuzz(5)
	actual := "Buzz"

	assert.Equal(expected, actual)
}

func TestInput1ShouldBeReturn1(t *testing.T) {
	assert := assert.New(t)

	expected := FizzBuzz(1)
	actual := 1

	assert.Equal(expected, actual)
}

func TestInput10ShouldBeReturnBuzz(t *testing.T) {
	assert := assert.New(t)

	expected := FizzBuzz(10)
	actual := "Buzz"

	assert.Equal(expected, actual)
}

func TestInput15ShouldBeReturnFizzBuzz(t *testing.T) {
	assert := assert.New(t)

	expected := FizzBuzz(15)
	actual := "FizzBuzz"

	assert.Equal(expected, actual)
}

func TestInput9ShouldBeReturnFizz(t *testing.T) {
	assert := assert.New(t)

	expected := FizzBuzz(9)
	actual := "Fizz"

	assert.Equal(expected, actual)
}
