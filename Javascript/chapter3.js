// data manipulation
let exampleSentence = 'this is a string';

let stringLength = exampleSentence.length;

console.log('Value at the end of the string = ', exampleSentence[stringLength - 1]);

let combinedString = 'hello world ' + ' ' + 'my name is james';

console.log(typeof(combinedString))

console.log(combinedString.indexOf('a'));

// split()
console.log(exampleSentence.split(' '));

//include
console.log(exampleSentence.includes('a'))

//replaceAll() & replace() method difference

// slice()

//regex : string matching or regular expression

// array and lists
// crud - create read update delete
let simple_array = ['james', 'is', 'cool'];
simple_array[1] = 'hello'
console.log(simple_array[1]);

//pop push shift unshift

simple_array.push('new_word')
console.log(simple_array)
simple_array.pop()
console.log(simple_array)

let check = simple_array.includes('james');
console.log(check)

let check1 = simple_array.join(' ');
console.log(check1);
let check2 = simple_array.reverse();
console.log(check2);

let check3 = simple_array.sort();
console.log(check3);

simple_array = [[1,2], [3,4]]
for(let i =0; i < simple_array.length; i++) {
    let subArray = simple_array[i];
    for(let j=0; j < subArray.length; j++) {
        console.log(i,j, simple_array[i][j])
    }
}

// how to delete or filter out values
let numbers = [1,2,3,4,5];
let start_num = numbers.slice(0,2);
let end_num = numbers.slice(3);

let newFliteredArray = start_num.concat(end_num);

console.log(newFliteredArray)

//objects in javascript
const bio = {
    name:'james',
    age: 29,
    hobbies: ['gym', 'coding', 'reading'],
    friends: {
        'john': {
            decscription: 'good at maths'
        }
    }
}

console.log(bio);

let name = bio['name'];
console.log(name);

let chk_key = 'name';
bio[chk_key] = 'henry'
console.log(bio.friends);

// object.entries

console.log('joke' in bio)

function helloWorld() {
    let sentence = 'hello world';
    console.log(sentence)
}

//clouser

function counter() {
    let count = 0

    return function() {
        count++
        console.log(count)
    }
}

let increment = counter()

increment()
increment()

module.exports = {
    helloWorld
}

// error handling techniques
const brokenObject = {
    word: 'nice'
}
function problemBlock() {
    try {
        console.log('Attempted the try block')
        const sub_object = brokenObject.hello.world

        console.log(sub_object)

    } catch (err) {
        console.log(err.message)
    }
   
}
//problemBlock()


function throwError() {
    try{
        throw new Error('Custom Error Message')
    } catch(err) {
        console.log(err.message)
    }
    
}
throwError()
console.log('code continue to excute')