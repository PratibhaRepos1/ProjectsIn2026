//Google questions: from given an array tell me first recurring character or number
//Given an array = [2,5,1,2,3,5,1,2,4]
// It should return 2

//Given an array = [2,1,1,2,3,5,1,2,4];
// It should return 1

// Given an array = [2,3,4,5];
// It should return undefined

function firstRecurringCharacter(input) {
    for(let i = 0; i < input.length; i++) {
        for(let j = i + 1; j < input.length; j++) {
            if(input[i] === input[j]) {
                return input[i]
            }

        }
    return undefined;
    }
} // O(n^2) since here we use two for loop so not efficients : so this First Character Recurring problem can be solved by using Hashtable

// using hashtable
function firstRecurringCharacter2(input){
    let map = {}
    for(let i = 0; i < input.length; i++) {
            
        if(map[input[i]] !== undefined) {
            return input[i]
        } else {
            map[input[i]] = i
        }
        console.log(map)
    }

    return undefined;

} // O (n) downside : increase space complexity but since we are using just 1 for loop we increase time complexity

console.log(firstRecurringCharacter([2,5,5,2,3,5,1,2,4]))
