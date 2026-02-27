#include <iostream>
#include <math.h>
using namespace std;

/*
Functions in C++ :
    1. library functions:
            use include library, like: #include <math.h>
                    sqrt()          Square root (ro: Rădăcină pătrată)
                    abs()           Absolute value(ro:Modul)
                    pow(a, b)       Power(ro: Putere)

    2. Define function by USER:
            I. define and call befoe main() function and call in main_function:
                    a. no has returnn value:
                            void function_name(){

                            }

                    b. has value return
                            value_type_return function_name(){

                            }

                    c. send parametr to main
                            I.
                                value_type_return function_name(parameter1, parameter2){
                                    statement;
                                }
                            II. call by value:
                                void function_name(type_value parameter1, type_value parameter2){
                                    statement;
                                }
                            III.call by reference:
                                void function_name(type_value &parameter1, type_value &parameter2){
                                    statement;
                                }
                    d. Recursive function:

            II. define function after mani, and declare that before main:

*/

//2.II. declare function after main
//-----------------------------------------------------
int factorial_2(int num);  // == int factorial_2(int);



// 2.I.a. define
//------------------------------------------------------
void show_message() {
    cout << "Hello world..." << endl;
}



//2.I.b. define
//-------------------------------------------------------
int calculate_sum()
{
    int first = 10;
    int second = 15;

    int sum = first + second;
    return sum;
}

//2.I.c.I send parameter to main
//-------------------------------------------------------
int calculate_sum_2(int first, int second)
{
    int sum = first + second;
    return sum;
}

int calculate_sum_3(int first = 3, int second = 5)  // has default value
{
    int sum = first + second;
    return sum;
}


//2.I.c.II. call by value
//-------------------------------------------------------
void increment(int x, int y)    // call by value
{
    x++;        //this operats did not work in main
    y++;        //function, because is local and different name
    //cout << "Inside increment: x = " << x << ", y = " << y << endl;
}


//2.I.c.III. call by reference
//-------------------------------------------------------
void increment_2(int &x, int &y)    // call by reference
{
    x++;        //this operats did not work in main
    y++;        //function, because is local and different name
    //cout << "Inside increment: x = " << x << ", y = " << y << endl;
}


//2.I.d. recursive function
//------------------------------------------------------
int factorial(int number)
{
    if(number == 1) return 1;
    return number * factorial(number - 1);
}



int main()
{
    //1. library function
    cout << "sqrt(25) = " << sqrt(25) << endl;
    cout << "abs(-15) = " << abs(-15) << endl;
    cout << "pow(2,3) = " << pow(2, 3) << endl;

    //2.I.a. call function
    //--------------------------------------------
    show_message();


    //2.I.b. call function
    //--------------------------------------------
    cout << "sum = " << calculate_sum() << endl;


    //2.I.c. call function
    //--------------------------------------------
    cout << "sum(10, 20) = " << calculate_sum_2(10, 20) << endl;        //calculate_sum_2(argument_1, argument_2)

    cout << "sum(12, 14) = " << calculate_sum_3(12, 14) << endl;
    cout << "sum = " << calculate_sum_3() << endl;                // calculate by default value


    //2.I.c.II. call by value
    //--------------------------------------------
    int a = 3;
    int b = 6;
    cout << "Before increment: a = " << a << ", b = " << b << endl;

    increment(a,b);
    cout << "After call increment(by value): a = " << a << ", b = " << b << endl;
    cout<<endl;

    //2.I.c.III. call by reference
    //---------------------------------------------
    int m = 3;
    int n = 6;
    cout << "Before increment: m = " << m << ", n = " << n << endl;

    increment_2(m, n);
    cout << "After call increment(by reference): m = " << m << ", n = " << n << endl;


    //2.I.d. call recursive
    //----------------------------------------------
    cout << "factorial(5) = " << factorial(5) << endl;


    //2.II.ccall function after main
    //----------------------------------------------
    cout << "factorial_2(4) = " << factorial_2(4) << endl;

    return 0;
}


//2.II. function after main
//--------------------------------------------------
int factorial_2(int num)
{
    if(num == 1) return 1;
    return num * factorial(num - 1);
}
