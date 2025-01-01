/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
  s = s.trim();
  let arrayString = s.split(" ");
  return arrayString[arrayString.length - 1].length;
};

let s = "   fly me   to   the moon  "
console.log(lengthOfLastWord(s));