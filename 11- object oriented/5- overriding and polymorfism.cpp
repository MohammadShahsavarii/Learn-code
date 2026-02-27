#include <iostream>

using namespace std;

/*
Overriding: we have same function(show_message) in parent and child class, but child_class has different behavior towards parent_class(in parent_class
            have "message from parent." but in child_class have "message from child.". IT IS OVERRIDING --> different behavior)

polymorfism: have same show_message function, thay are similar but inside of them are different.


Accessibility in | public | private | protected |
-------------------------------------------------
inside class     |   √   |    √    |     √      |
-------------------------------------------------
outside class    |   √   |    X    |     X      |
-------------------------------------------------
child class      |   √   |    X    |     √      | 

for type '√': holding "Alt" key and type 251.
           
*/


class parent_class{
  
    public:
        void show_message() {

            cout << "This is a message from parent." << endl;
        }
};

class child_class : public parent_class {
    
    public:
        void show_message() {
            
            cout << "This is a message from child." << endl;
        }
};

int main() {

    parent_class parent_obj;
    child_class child_obj;

    parent_obj.show_message();
    child_obj.show_message();
}