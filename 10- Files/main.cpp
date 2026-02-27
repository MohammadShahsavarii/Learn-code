#include <iostream>

#include <fstream>

using namespace std;

/*
include fstream
and in some IDE
include string

ofstream  = output (write on file)
ifstraem  = input (read file)

for( ; ; ) =  infinite loop

*/

int main()
{
   /* ofstream phone_file("phone.txt");

    long number;
    string name;

    cout << "Enter number for each name(0 for quite):" << endl;
    // infinite loop until write 0
    for( ; ; ){
        cout << "Number: ";
        cin >> number;
        if (number == 0)
            break;

        // write number in phone file
        phone_file << number << ' ';

        cout << "Name: ";
        cin >> name;
        phone_file << name << ' ';
        cout << endl;
    }
*/
    //------------------------------------------------------------------
    ifstream phone_file("phone.txt");

    long number;
    string name, search_name;

    bool found = false;     // flag

    cout << " Enter name for search: ";
    cin >> search_name;
    cout << endl;

    // until it is possible: read from phone_file and put in number
    while (phone_file >> number){
         // read name, after read number
        phone_file >> name;

        if( name == search_name){
            cout << name << ": " << number;
            found = true;
            break;
        }

    }
    if (found == false){
        cout << search_name << " is not in this phonebook." << endl;
    }
}
