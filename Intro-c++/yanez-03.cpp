#include <iostream>

using namespace std;

int main () {
    int num;
    cout << "Ingresa un numero: ";
    cin >> num;

    if (num % 2 == 0) {
        cout << "Es par!!";
    } else {
        cout << "Es impar :(";
    }
    
    return 0;
}