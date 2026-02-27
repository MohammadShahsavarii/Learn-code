#include <iostream>

using namespace std;
/*                                                          (name of Array)numbers _____________________
Array element has same type, and have index                                        | 2 | 8 | 4 | 18 | 3|
                                                                                   ---------------------
Dimension:                                                                  index    0   1   2   3    4
    1. One-Dimensional Arrays: number[3]
    2. Multi-Dimensional Arrays:  a[1][3]

define and initialize:
    by programmer:
        initialize undirect:    type name[numbers of element];
                                name[index] = value;
                                name[index] = value;

        intialize direct;       type name[numbers of element] = { value, value, ...}

    by user:
        use for loop.

*/
int main()
{
    // I. ONE-DIMENSIONAL ARRAYS:
    // define array
    int number[5];      // type name[number of element];

    // initialize element by programmer
    // 1.
    number[0] = 4;
    number[1] = 6;
    number[2] = 4;
    number[3] = 5;
    number[4] = 3;

    cout << number[3] << endl;
    for (int i = 0 ; i < 5 ; i++){
        cout << "number: " << number[i] << endl << endl;
    }

    // 2.
        //a.
    int numbers_2[5] = { 1 ,2 , 3 , 4 , 5 };
    for (int i = 0 ; i < 5 ; i++){
        cout << "numbers_2: " << numbers_2[i] << endl;
    }
        //b.
    /*int numbers_3[3] = { 1 ,2 , 3 , 4 , 5 };
    for (int i = 0 ; i < 3 ; i++){                          ERROR
        cout << "numbers_3: " << numbers_3[i] << endl;
    }*/
        //c.
    int numbers_4[7] = { 1 ,2 , 3 , 4 , 5 };
    for (int i = 0 ; i < 7 ; i++){
        cout << "numbers_4: " << numbers_4[i] << endl;
    }
        //d.
    int numbers_5[] = {11, 12, 13, 14, 15};
    for (int i = 0; i < 7; i++){                           // The last two index values are garbage.
       // cout << "numbers_5: " << numbers_5[i] << endl;
    }



    //-----------------------------------------------------------
    int num[5];

    // initialize element by cin (user)
    cout << "Enter 5 numbers: ";
    for ( int i = 0; i < 5; i++){
        cin >> num[i];
    }
    for(int i = 0; i < 5; i++){
        cout << num[i] << endl;
    }


    //  II. MULTI-DIMENSIONAL ARRAYS:

    // define
    int a[2][3];
    // 1 2 3    --> row1 index[0]
    // 4 5 6    --> row2 index[1]
    a[0][0] = 1;
    a[0][1] = 2;
    a[0][2] = 3;

    a[1][0] = 4;
    a[1][1] = 5;
    a[1][2] = 6;

    for(int i = 0; i < 2; i++){       // number of rows
        for(int j = 0; j < 3; j++)  // number of cloumns
            cout << a[i][j] << " ";
        cout << endl;       //برای چاپ زیر همدیگر
    }
    //-----------------------------------------------
    int b[2][3] = {
                    { 11 , 12 , 13},
                    { 14 , 15 , 16}
                  };
    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 3; j++)
            cout << b[i][j] << " ";
        cout << endl;
    }


    //--------------------------------------------------

    int c[2][3];
    cout << "Enter 6 numbers for c: ";
    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 3; j++)
            cin >> c[i][j];
    }
    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 3; j++)
            cout << c[i][j] << " ";
        cout << endl;
    }
}
