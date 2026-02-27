#include <iostream>

using namespace std;

/*

while(condition)                                وقتی تعداد دفعات تکرار مشخص نیست
    statement;

//---------------------------


do statement while (condition);                  وقتی تعداد دفعات تکرار مشخص نیست


//----------------------------


for(initialization ; condition ; updte)             وقتی که تعداد دفعات تکرار مشخص هست
    statement;

HOW for LOOP WORKS:
    1- initialize
    2- check condition
    3- run statement
    4- evaluation update
    5- repeat steps 2 to 4

*/

int main()
{
    int number = 1;
    while (number <= 10){
        cout << "Hello" << endl;
        number++;
    }
    cout << "The End" << endl << endl;


    //----------------------------------


    int nums = 1;
    do {
        cout << "H0ll0" << endl;
        nums++;
    }while(nums <= 11);
    cout << "The End" << endl << endl;


     //----------------------------------


     for (int i = 1 ; i <= 10 ; i++){
        cout << "salam" << endl;
     }
     cout << "The End" << endl << endl;


     //------------------------------------


     for ( int i = 10 ; i > 0 ; i--){
        cout << "LOOP" << endl;
     }
     cout << "The End" << endl << endl;


     //------------------------------------


     for ( int i = 1 ; i <= 10 ; i++){

        if(i == 5) break;

        cout << i << endl;
     }
     cout << "The End" << endl << endl;


     //------------------------------------


     for ( int i = 1 ; i <= 10 ; i++){

        if(i == 5) continue;        // nu return number 5

        cout << i << endl;
     }
     cout << "The End" << endl << endl;


}
