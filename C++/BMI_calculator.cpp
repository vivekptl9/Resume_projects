#include <iostream>
using namespace std;

int main(){
    float weight,height, bmi;
    cout << "Weight (kg), Height (m)"<< endl;
    cin >> weight >> height;
    bmi = weight / (height*height);

    if (bmi <18.5)
        cout <<"Your BMI is: "<< bmi <<  "You are 'Underweight'"<< endl;
    else if (bmi >25)
        cout << "Your BMI is: "<< bmi << "You are 'Overweight'" << endl;
    else
        cout << "Your BMI is: "<< bmi << "You are fit, 'Keep it up!'"<< endl;

    
    //cout << bmi;

    return 0;


}
