#include <iostream>

using namespace std;
/*
Data type:
 Integer:                                               Floating point:
    integer(short, int, long)                               float
    Boolean (bool) => true, false                           double
    Character (char) => a-z,0-9,.,{},[],...
    numerical (enum)


Assignment Operators:
m += 5  --->  m = m + 5
m -= 5  --->  m = m - 5
m *= 5  --->  m = m * 5
m /= 5  --->  m = m / 5
m %= 5  --->  m = m % 5


Increment and Decrement Operators:
    For one variable:                                        For more than one variable:
        ++m  --->  m = m + 1 (Pre-increase)                     n = ++m;  ---> first increase m, then initialize n
        m++  --->  m = m + 1 (Post-increase)                    n = m++   ---> first initialize n, then increase m

        --m  --->  m = m - 1 (Pre-decrease)
        m--  --->  m = m - 1 (Post-decrease)
*/
int main()
{
    int m , n;
    m = 20;
    n = ++m;
    cout << "n = ++m " << ", "<< "m = "<< m << ", " << "n= " << n << endl;

    m = 20;
    n = m++;
    cout << "n = m++ " << ", " << "m = "<< m << ", " << "n= " << n << endl;
    return 0;
}
