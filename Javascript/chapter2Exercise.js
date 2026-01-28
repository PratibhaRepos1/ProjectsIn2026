// 1. Define a variable called name and set it equal to a string that contains your name. Then, demonstrate how you would change its value to your full name.

let name = 'Pratibha';
name = 'Pratibha Jadhav'

// 2. How would you compare two variables, a and b, to check equality?
let a = 10;
let b = '10';

console.log(a === b);

// 3. Write an if...else statement in JavaScript that checks if a number stored in a variable age is greater than 18. If true, it should log "Adult" to the console; otherwise, it should log "Minor".

let age = 20;
if(age > 18) {
    console.log('Adult');
} else {
    console.log('Minor')
}

// 4. Create a for loop that iterates from 0 to 10, but only prints even numbers to the console.

for(let i = 0; i<10; i++) {
    if(i%2 === 0)  {
        console.log('i:', i);
    }
}

// 5. Given an array numbers, write a while loop that continues to sum the numbers until the sum is greater than 100, then exits the loop.

let numbers = [10,2, 3, 44,50,60,];
let i = 0;
let length = numbers.length
while(i < length) {
    sum = numbers[i] + numbers[i+1];
    if(sum > 100) {
        break;
    }
    console.log('sum is ', sum);
    i++;
}
// 6. Define a function named calculateArea that takes two parameters, width and height, and returns the area of a rectangle. // width * height

function calculateArea(width,height) {
    return width * height;
}
console.log(calculateArea(5,3));