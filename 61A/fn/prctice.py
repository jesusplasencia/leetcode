#
def welcome():
    print('Go');
    return 'hello';
#

#
def cal():
    print('Bears');
    return 'world';
#

#
def digit(n, k):
    strNbr = str(n);
    lenStr = len(strNbr);
    if (lenStr - 1 < k): return 0;
    return int(strNbr[lenStr - 1 - k]);
#

#
def middle(a, b, c):
    sumTmp = a + b + c;
    maxTmp = max(a, b, c);
    minTmp = min(a, b, c);
    return sumTmp - (maxTmp + minTmp);
#

print(middle(30, 5, 40));