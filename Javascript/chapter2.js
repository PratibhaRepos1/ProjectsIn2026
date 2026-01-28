console.log('hello world');
console.log(10 + 6);

//var, let, const
const sentence = 'I am better every day.'; // this is string
let numberOfEggs = 3; // this is number
numberOfEggs = 8;

console.log(sentence);
console.log(numberOfEggs);

let totalGroceries = numberOfEggs;
console.log(totalGroceries);

true && false // these are booleans

let friends = {
    james: 'is super cool',
    lucy: 'isn\'t a so cool'
} // object

console.log(friends);

//array
let exampleArray = [1,2,3,4,90,100]; // JS is 0th index system
//console.log(exampleArray);

//functions in javascript
function sumNumbers(value, secondValue) {
    if(value == secondValue) {
        console.log(value === secondValue);
    }
    console.log('sum of two values: ', value + secondValue);
}

let anotherSumNumbers = sumNumbers;

sumNumbers('3',3);
anotherSumNumbers(10,20);

// operators in Javascripts =, +, -, *, /, %, ==, ===, !=. !===
// logical operators && AND || OR !

let condition1 = true;
let condition2 = false;
//console.log(condition1 && condition2)
//console.log(!condition1)

// typeof function
//control flow

// if else block
if(condition1 && condition2) {
    console.log('You did it!');
} else if(condition1 || condition2) {
    console.log('one condition of the two was true')
}
else {
    console.log('the value was false so here we are');
}

// while loop
let i = 0;
let length = exampleArray.length;

// while(i < length) {
//     console.log('i:', i)
//     i++;
// }

for(let j=10; j<30; j++ ) {
    if(j%2 === 0) {
        continue
    }
    console.log('j:',j)
}

// continue and break keywords in javascript

function addStrings(string1='default1', string2='default1') {
    if(!string1 || !string2) {
        console.log('you are missing inputs')
        return
    }
    console.log(string1 + ' ' + string2);
}

addStrings('hello')