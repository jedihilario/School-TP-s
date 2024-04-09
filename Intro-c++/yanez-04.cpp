#include <iostream>

using namespace std;

int main () {
    int n;
    cout << "Ingresa un numero: "; cin >> n;

    cout << "La tabla del " << n << "es:\n";
    for (int i = 1; i < 11; i++) {
        cout << n * i;
    }

    return 0;
}