/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
    let index = 1;
    let current = strs[0].substring(0, index);
    if (strs.length === 1) return strs[0]
    if (current === '') return "";
    while(current != null) {
        if (index > strs[0].length) {
            return strs[0].substring(0, index - 1);
        }
        let mapFilterWords = strs.filter((item) => item.substring(0, index) === current);
        if (mapFilterWords.length === 0) {
            if (index > 0) {
                return strs[0].substring(0, index - 1);
            }
            return "";
        }
        else if (mapFilterWords.length === strs.length) {
            index++;
            current = strs[0].substring(0, index);
        }
        else {
            return strs[0].substring(0, index - 1);
        }
    }
}

let strs = ["flower","flower","flower","flower"]
console.log(longestCommonPrefix(strs));