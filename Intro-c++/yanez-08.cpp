#include <iostream>

using namespace std;

int mcd (int a, int b) {
    int resto;

    while (b != 0) {
        resto = a % b;
        a = b;
        b = resto;
    }

    return a;
}

int main () {
    int a, b;

    cout << "Ingrese los dos numeros para calcular el mcd:" << "\n";
    cin >> a >> b;

    cout << "El mcd es " << mcd(a,b) << "\n";

    return 0;
}