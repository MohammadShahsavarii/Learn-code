#include <iostream>

using namespace std;

/*
class name {
    private:
        property

    public:
        //the functions who need to call or access
};

// define object in main function

# constructor: have same name of class
              has no any type of return
              it is automatic recall
*/


/* first way

class date {
    private:
        int year;
        int month;
        int day;

    public:
        // define function to have access to details in private
        void set_date( int y, int m, int d){
            year = y;
            month = m;
            day = d;
        }

        void print_date(){
            cout << "date: " << year << "/" << month << "/" << day << endl;
        }
};
*/


// second way(use constractor)

class date{
    private:
        int year;
        int month;
        int day;

    public:
        //define constructor
        date(int y, int m, int d){
            year = y;
            month = m;
            day = d;
        }

        void print_date(){
            cout << "date: " << year << "/" << month << "/" << day << endl;
        }
};

int main()
{
    /* //first way
    // define object: name_of_class name_for_object
    date date1;

    //access to detail in class
    date1.set_date(1365, 3, 12);
    date1.print_date();
    */

    // second way(constructor)
    // define and initialize object
    date date1(1365, 3, 12);
    date1.print_date();
}
