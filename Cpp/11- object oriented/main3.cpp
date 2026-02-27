#include <iostream>

using namespace std;

// private member functions

/*
every object that define from class, has its own copy of all member of class.

sometimes we have no object, or it is not in access, and need to access the members, we can use static members.

*/

/*
in static:
            because has not object, do not use constructor
can do static properties and also functions

initialize static members is:
                         out of the class and 
                         out of main function
*/




class date{
    private:
        static int year;
        static int month;
        static int day;


    public:
        static void print_date() {
            cout << "date: " << year << "/" << month << "/"  << day << endl;
        }

};

// initialize static properties
    // access from class date to element year
int date::year = 1375;
int date::month = 6;
int date::day = 12;


int main()
{
    date::print_date();
}
