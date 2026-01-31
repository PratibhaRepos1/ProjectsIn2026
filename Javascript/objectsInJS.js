/* Objects In Javascript
An object is a collection of key-value pairs used to store related data and functionality.
key -> properties
Values -> any data type (string, number, array, functions, object)
Objects are reference data types in Javascript
*/
//create a object
// 1. Object Literal (most common)
const car = {
    brand: 'BMW',
    speed: 200
}

//2. Using new Object()
const obj = new Object();
obj.name = "JS";

//3. Using Constructor Function (older but important)
function Person(name,age) {
    this.name = name;
    this.age = age;
}
const p1 = new Person("A", 23);

//Accessing Object Properties
car.brand;
//Bracket Notation
car['speed'];

const user = {
    name: 'Pratibha',
    age: 31,
    isDeveloper: true
};

//Adding, updating & Deleteing Properties
user.city = "Bangkok" // add
user.age = 41; //update

delete user.isDeveloper; // delete


//Objects are Reference Types (Very Important)
const a = {value: 10};
const b = a;

b.value = 20; //since both a & b point to the same memory location 
/* output will
    a:  { value: 20 }
    b:  { value: 20 }
*/ 
console.log('a: ', a);
console.log('b: ', b);

/* Interview Q:
Why objects behave differently from primitives?
👉 Because objects are stored by reference.
*/
// Object Methods (functions inside Objects)

const user1 = {
    name: 'Pratibha',
    greet() {
        return `Hello ${this.name}`;
    }
}

console.log(user1.greet());

// Looping through the Objects: for...in, Object.keys(), Object.values(), Object.entries()

for(let key in user) {
    console.log('key:', key, 'value:', user[key])
}

console.log('-----------------*******************-----------------------');
console.log(Object.keys(user));
console.log(Object.values(user));
console.log(Object.entries(user));

// Object Destructuring (must know)

const student = {name:"John", age:23}
const {name, age} = student;

//rename while destructuring
const {name: studentName} = student;

console.log(student)

//Shallow copy VS Deep Copy (interview Favorite)
const copy = {...student};

const deepCopy = JSON.parse(JSON.stringify(user));
console.log(deepCopy);