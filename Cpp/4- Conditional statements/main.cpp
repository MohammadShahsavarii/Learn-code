#include <iostream>

using namespace std;

/*
if(condition){
    statement;
}


if(condition){
    statement1
}else{
    statement2;
}



(condition) ? expression1 : expression2;



else..if




switch    ---> better used instead of else..if

*/

int main()
{
    int number = 6;
    if(number < 10)
        cout << number << " is less than 10" << endl;
    else
        cout << number << " is greater than 10" << endl;

    //-----------------------------------------------

    int m = 10;
    int n = 15;
    int min = (m < n) ? m : n;
    cout << "min(" << m << "," << n << ") = " << min << endl;

    //-------------------------------------------------

    char country;
    cout << "England, Germany, Italy, France, Russia ? (E | G | I | F | R) :";
    cin >> country;
    if (country == 'E')
        cout << " country : England" << endl;
    else if(country == 'G')
        cout << "country : Germany" << endl;
    else if(country == 'I')
        cout << "country : Italy" << endl;
    else if(country == 'F')
        cout << "country : France" << endl;
    else if(country == 'R')
        cout << "country : Russia" << endl;
    else
        cout << "Error..." << endl;


    //---------------------------------------------------

    //char country;
    cout << "England, Germany, Italy, France, Russia ? (E | G | I | F | R) :";
    cin >> country;
    switch(country) {
        case 'E' : cout << "country: England" << endl; break;
        case 'G' : cout << "country: Germany" << endl; break;
        case 'I' : cout << "country: Italy" <<   endl; break;
        case 'F' : cout << "country: France" <<  endl; break;
        case 'R' : cout << "country: Russia" <<  endl; break;

        default : cout << "Error..." << endl;  break;
    }
}
