// const funnyNumber = (array) => { // 4 operators
//     for(let i = 0; i < array.length; i++) {
//         if(i===3) return array[i];
//     }
// };

const funnyNumber = (array) => { // 1 operations
     return array[3];
};

const nums = [420, 96, 12, 69, 77];

console.time("funnyNumber");
console.log(funnyNumber(nums));
console.timeEnd("funnyNumber");