function mySqrt(x: number): number {
    
    if (x == 0) return 0;

    let lo = 0;
    let hi = x;

    while (lo < hi) {
        const m = Math.floor(lo + (hi - lo) / 2);
        const sqr = m * m;
        if (sqr === x) {
            return m;
        } else if (sqr > x) {
            hi = m;
        } else {
            lo = m + 1;
        }
    }

    return lo - 1;

};