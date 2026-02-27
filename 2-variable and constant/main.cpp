#include <iostream>

using namespace std;

int main()
{
    /* DEFINE VARIABLES */
    int m;  //define variable
    m = 10; //value variable
    int n = 20; //define and value variable
    cout << "m = " << m << " , " << "n = " << n << endl;

    m++;                           // increase value of variable
    cout << "m = " << m << endl;


    int d, f;                       // recive value of variables from user
    cout << "enter two integer number: ";
    cin >> d >> f;
    cout << "d = " << d << " , " << "f = " << f << endl;

    int s, t;
    cout << "s = " << s << " , " << "t = " << t << endl;


    /* DEFINE CONSTANT */

    const int z = 5, x= 6;                // for constant can not define and value separate
    cout << "z = " << z << " , " << "x = " << x << endl;
    /*z++;      CAN NOT CHANGE VALUE OF CONSTANT
    cout << "z= " << z;
    */
    return 0;
}
