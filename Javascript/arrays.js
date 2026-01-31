/* Arrays In Javascript 
An array is an ordered collection of elements, stored by index (starting from 0).
Arrays are objects, can store mixed data types
*/

//2. How to Create Arrays
const arr = [10,20,30,40,50];
const mixed = [1, "JS", true, {name:"A"}, null];
const nums = [1,2,3, 4, 5, 6, 7,2];

const arr1 = new Array(4) // creating a empty array with length 4, Tip: avoid in interview

//3. Accessing & Updating Elements
console.log(nums[0]); //access
nums[1] = 5; //update
console.log(nums);
nums.length; // length

//4. Important Array Methods (Must-Know)
/*
| Method      | Description       |
| ----------- | ----------------- |
| `push()`    | Add at end        |
| `pop()`     | Remove from end   |
| `unshift()` | Add at start      |
| `shift()`   | Remove from start |

*/
nums.push(10) // Add at the end
console.log(nums)
nums.pop() //remove from end
console.log(nums)
nums.unshift(20) // add at the start
console.log(nums)
nums.shift() // remove from start
console.log(nums)

// 5. Iteration Methods (Very Important)
//forEach() (no return)
nums.forEach(n => console.log(n))

//map() (returns new array)

const doubled = nums.map(n => n * 2);
console.log(doubled);

//filter() return new array
const even = nums.filter(n => n % 2 === 0);
console.log(even);

// 6. Search & Check Methods

console.log(nums.includes(2));
console.log(nums.indexOf(2))
console.log('*******')
console.log(nums.find(n => n > 2));
console.log(nums.some(n => n > 2));
console.log(nums.every(n => n > 2));

// slice() vs splice() (Classic Interview Q)
/*  slice(start, end)   // non-mutating
    splice(start, count) // mutating
*/
console.log(arr.slice(1,3)); // non-mutating
console.log(arr)
console.log(arr.splice(1,2)); //mutating
console.log(arr);

//9. Array Destructuring

const [a,b] = [10,20];

const [, second] = [1,2,3];

// spread operator
const newArr = [...nums, 3,4];

//copy operator
const copyMe = [...nums]
console.log('----------Sorting array ---------');
const sortME = [10,3,5,2,9].sort((a,b) => a - b);
console.log(sortME)