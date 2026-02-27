int main()
{
    int m , n;
    m = 20;
    n = ++m;
    cout << "n = ++m " << ", "<< "m = "<< m << ", " << "n= " << n << endl;

    m = 20;
    n = m++;
    cout << "n = m++ " << ", " << "m = "<< m << ", " << "n= " << n << endl;
    return 0;
}