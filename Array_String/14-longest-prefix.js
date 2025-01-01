/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
    if (strs.length == 0) return "";
    let prefix = strs[0];
    for (let word of strs) {
        while(word.indexOf(prefix) !== 0) {
            //Remove last word from my chosen prefix
            prefix = prefix.slice(0, -1);
            if (prefix == "") return "";
        }
    }
    return prefix;
};

let strs = ['flower', 'flow', 'flight'];
console.log(strs[1].indexOf('flow'));