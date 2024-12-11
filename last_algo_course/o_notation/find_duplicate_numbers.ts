function findDuplicate(nums: number[]): number {
    let dictionary = {};
    for (let num of nums) {
        if (num in dictionary) {
            return num;
        } else {
            dictionary[num] = 1;
        }
    }
    return -1;
};

// Create tests
function testFindDuplicate() {
    const input = [1, 3, 4, 2, 2];
    const expected = 2;
    const result = findDuplicate(input);
    console.log(result === expected ? "Passed" : "Failed");
}

testFindDuplicate();