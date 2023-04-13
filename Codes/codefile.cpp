
#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter a number: ";
    cin>>n;

    // calculate factorial
    int factorial = 1;
    for(int i=2;i<=n;i++){
        factorial *= i;
    }
    cout<<"Factorial of "<<n<<" is: "<<factorial<<endl;

    // print all factors
    cout<<"Factors of "<<n<<": ";
    for(int i=1;i<=n;i++){
        if(n%i==0){
            cout<<i<<" ";
        }
    }
    return 0;
}
