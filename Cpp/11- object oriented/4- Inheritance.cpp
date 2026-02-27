#include <iostream>

using namespace std;

/*
sign ':' front of the class is for inheritance, and level of access can be private or public.
*/




class parent_class{
    private:  int x;

    protected: int y;

    public:
        void public_function() {
            x = 10;
            cout << "x= " << x << endl;

            y = 20;
            cout << "y= " << y << endl;
        }
};

class child_class : private parent_class {
    public:
        // constructor
        child_class() {
            
            //x = 10;                             we can not access private members
            //cout << "x= " << x << endl;         from child class

            y = 12;                             // we access protected members
            cout << "y= " << y << endl;         // from child class

            public_function();              // with call this public function from parent class
                                            // we can access to public members

        }
};

int main() {

    parent_class obj;

    // cout << obj.x << endl;      error: parent_class::x' is private
    // cout << obj.y << endl;      error: parent_class::y' is protected

    obj.public_function();
    
    //-------------------------------------------
    // define object and automatically call constructor
    child_class child;


    // child.public_function();       Error:  because of access level of child_class is private, we can not access public members of parent_class
                                          //  if it was public: we can access public members of parent_class
}