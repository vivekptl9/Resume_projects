#include<iostream>
using namespace std;
int main()
{
    // int a =20;
    // int b = 10;
    // cout << "old a: "<< a <<" old b: "<< b<< endl;
    // int temp = a;
    // a = b;
    // b= temp;
    // cout << "New a: "<< a<<  " New b: "<< b << endl; 
    int a = 20;
    int b = 10;
    cout << "old a: "<< a <<" old b: "<< b<< endl;
    a = a+b;
    b = a-b;
    a = a-b;
    cout << "New a: "<< a<<  " New b: "<< b << endl;
    return 0;
}
