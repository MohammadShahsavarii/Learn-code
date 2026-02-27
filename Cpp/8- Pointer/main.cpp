#include <iostream>

using namespace std;

/*
A pointer is a variable that contains an address.


                            name_of_variable
           address: y       /                  \        x : address
                     \____pn_____           ____n______/
                     |    x     |   ====>  |    44     |
                      -----------           -----------
                         int*                   int
                             \
                               type


## &name_of_variable ----> display address of variable

## The type of the pointer is type of the cell it points to.

## pointer can point to anything that has an address.

*/


int main()
{
    int n = 44;

    cout << "n = " << n << endl;
    cout << "&n = " << &n << endl << endl;

    //-------------------------------

    int* pn = &n;

    cout << "pn = " << pn << endl;
    cout << "&pn = " << &pn << endl;

    cout << "*pn = " << *pn << endl << endl;    // َAccessing the value of a variable

    /*
    point to pointer:

                z                    y                    x  <-- address
     ___ppn____/          ___pn____/          _____n____/
    |    y    |   ===>   |   x    |   ===>   |    44   |
     ----------           ---------           ---------
        int**               int*                 int    <--- type

*/

    int** ppn = &pn;

    cout << "ppn = " << ppn << endl;        // == address of ppn
    cout << "&ppn = " << &ppn << endl;

    cout << "*ppn= " << *ppn << endl;       // == pn == address of n
    cout << "**ppn = " << **ppn << endl;

    char* p = strchr(s, 'C');

}
