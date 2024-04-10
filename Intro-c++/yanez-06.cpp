#include <iostream>

using namespace std;

bool esPrimo (unsigned int n) {
    int mitad = n / 2;

    for (int i = 2; i <= mitad; i++) {
        if (n % i == 0) return false;
    }

    return true;
}

int main () {
    int a = 0;

    cout << "Numero: "; cin >> a;

    for (int i = 1; i <= a; i++) {
        if (esPrimo(i)) cout << i << "\n";
    }

    return 0;
}