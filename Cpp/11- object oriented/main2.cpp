#include <iostream>

#include <iomanip>  // include for use of setfill and setw

using namespace std;

// information hiding


/*
use:
setfill(): Sets the fill character for output operations from left.
setw(): Sets the width of the next input/output field.
*/

class date{
    private:
        int year;
        int month;
        int day;

        // private member function
        // Adjust the date and print it in the format YYYY/MM/DD
        void adjust_date_and_print_date(){ //1365/3/12  => 1365/03/12
            cout << "date: " << year << "/" << setfill('0') << setw(2) << month << "/" << setfill('0') << setw(2) << day << endl;
        }
    
    
    public:
        // constructor
        date(int y, int m, int d){
            year = y;
            month = m;
            day = d;
        }

        void print_date() {
            adjust_date_and_print_date();
        }
};

int main()
{
    date date1(1365, 6, 12);
    date1.print_date();
}
