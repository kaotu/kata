const twoSum = require("./index");

test("should twoSum() to be defined.", () => {
  expect(typeof twoSum).toEqual("function");
});

test("should return [0,1] if input [2,7,11,15] and target = 9", () => {
  const actual = twoSum([2, 7, 11, 15], 9);
  const expected = [0, 1];
  expect(actual).toEqual(expected);
});

test("should return [1,3] if input [0,1,2,3] and target = 4", () => {
  const actual = twoSum([0, 1, 2, 3], 4);
  const expected = [1, 3];
  expect(actual).toEqual(expected);
});

test("should return [0,3] if input [12,3,4,9] and target = 21", () => {});
