/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  let numbers = [];
  while (s > 0) {
    let digit = s % 10;
    numbers.push(digit);
    s = Math.floor(s / 10);
  }
  return calculateRomanString(numbers);
};

var calculateRomanString = (numbers) => {
  let romanString = '';
  var dict = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
  };

  for (let i = numbers.length ; i > 0; i--) {
    let digit = numbers[i - 1];
    let counter = i;
    //Scenario when digit is 9, 90, 900
    let myNumber = digit*(10**(counter - 1));
    if (myNumber == 9*(10**(counter - 1))) {
        romanString += dict[10**(counter-1)] + dict[10**(counter)];
    }
    else if (myNumber >= 5*(10**(counter - 1)) && myNumber < 9*(10**(counter-1))) {
        let repetitiveQty = (myNumber - 5*(10**(counter - 1)))/(10**(counter-1));
        romanString += dict[5*(10**(counter-1))] + (dict[1*(10**(counter-1))]).repeat(repetitiveQty);
    }
    else if (myNumber == 4*(10**(counter - 1))) {
        romanString += dict[10**(counter-1)] + dict[5*(10**(counter - 1))];
    }
    else {
        romanString += dict[10**(counter-1)].repeat(digit);
    }
  }

  return romanString;
};

console.log(romanToInt(400));
