// O(n) time complexity
function sum_char_codes (n: string): number {
    let sum = 0;

    for (let i = 0; i < n.length; i++) {
        sum += n.charCodeAt(i);
    }

    for (let i = 0; i < n.length; i++) {
        sum += n.charCodeAt(i);
    }

    return sum;
}

// O(n) time complexity
function sum_char_code_until_char_69 (n: string): number {
    let sum = 0;

    for (let i = 0; i < n.length; i++) {
        const charCode = n.charCodeAt(i);
        if (charCode === 69) return sum;
        sum += n.charCodeAt(i);
    }

    return sum;
}

// O(n²) time complexity
function sum_char_codes_all_combinations (n: string): number {
    let sum = 0;

    for (let i = 0; i < n.length; i++) {
        for (let j = 0; j < n.length; j++) {
            sum += n.charCodeAt(i) + n.charCodeAt(j);
        }
    }

    return sum;
}

// O(n3) time complexity
function sum_char_codes_all_combinations_3 (n: string): number {
    let sum = 0;

    for (let i = 0; i < n.length; i++) {
        for (let j = 0; j < n.length; j++) {
            for (let k = 0; k < n.length; k++) {
                sum += n.charCodeAt(i) + n.charCodeAt(j) + n.charCodeAt(k);
            }
        }
    }

    return sum;
}