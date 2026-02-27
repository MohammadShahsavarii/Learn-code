#include <iostream>

#include <cstring>

using namespace std;

/*
'\0'   -->    End of string character

srtlen  -->  return length of string without '\0', means return real length of string

strchr()  -->  To find the first location of a specific character in a string
    str → The address of the string we want to search in.
    ch → The character we want to find (passed as an int, but actually a char).

    Output → If the character is found, the address of its first occurrence in the string is returned;
             if not found, NULL is returned.


strrchr()  -->   find last character in string( r= revers, that means start from end of string to first)
                like strchr works


strstr()  -->   looking for string


strcmp(str1, str2)  --> compare between two string
            (str1 < str2) -->  return <0
            (str1 == str2) --> return 0
            (str1 > str2) -->  return >0


strcpy(str1, str2)  -->  overwrite seconf string on first string


strncpy(s1, s2, n)      n= which character want to cverwrite on string1


strcat(str1, str2)      catenate str2 at the end of str1


strncat(s1, s2, n)      add n first character of s2 on end of s1 string


return pointer(return address of first character that found)

**NOTE: name of each array is address of first element.

*/

int main()
{
    char s[] = "ABCD";

    cout << s << endl;

    for (int i = 0; i < 5; i++){

        cout << "s[" << i << "] = "<< "'" << s[i] << "'" << endl;
    }

//--------------------------------------------------------------------

    // library function 'strlen'
    char st[] = "ABCDE";

    cout << st << endl;

    cout << strlen(st) << endl;     // for this function should include librsry "cstring"

//----------------------------------------------------------------------

    char s0[] = "hello sinom";

    cout << s0 << endl;

    char* p = strchr(s0, 'o');      // here we have address of 'o'

    cout << p - s0 << endl;                 // minus p from s1(name of array is point to first element, here is 'h' and equall to 0)


    char *p1 = strrchr(s0, 'o');
    cout << p1 - s0 << endl;


    char *p2 = strstr(s0, "ino");
    cout << p2 - s0 << endl;        // answer:7, means string "ino" started from index 7

//----------------------------------------------------------------------

    char s1[] = "abcdefg";
    char s2[] = "xyz";

    cout << s1 << endl;
    cout << s2 << endl;

    int result = strcmp(s1, s2);

    if(result < 0)
        cout << "s1 < s2" << endl;
    if(result == 0)
        cout << "s1 = s2" << endl;
    if(result > 0)
        cout << "s1 > s2" << endl;


    //strcpy(s1, s2);         // copy(overwrite) second string on first string
    cout << s1 << endl;         //  abcdefg
    cout << s2 << endl;         //  ||||
                                //  vvvv
                                //  xyz\0   --> It doesn't take anything after '\0'.

    strncpy(s1, s2, 2);      // First two characters
    cout << s1 << endl;
    cout << s2 << endl;


    strcat(s1, s2);
    cout << s1 << endl;
    cout << s2 << endl;


    strncat(s1, s2, 2);
    cout << s1 << endl;
    cout << s2 << endl;




}
