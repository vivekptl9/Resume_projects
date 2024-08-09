#include <iostream>
using namespace std;

int main(){
    int hostUserNum, guestUserNum;
    cout << "Host: ";
    cin >> hostUserNum;
    system("cls");

    cout << "Guest: ";
    cin >> guestUserNum;

    //? Normal IF else
    // if (hostUserNum == guestUserNum)
    //     cout << "Correct!";
    // else 
    //     cout << "Failed";
    
    /* 
    ! Ternary Operation:
    ! Syntax: Condition ? output 1 if True : output 2 if false;
     */ 
    (hostUserNum == guestUserNum)?
        cout << "Correct!": cout << "Failed";
    return 0; 

}