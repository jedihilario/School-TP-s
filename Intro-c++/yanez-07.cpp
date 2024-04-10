#include <iostream>
#include <string>

using namespace std;

int main () {
    string palabra;

    cout << "Ingresa la palabra para saber la longitud: "; cin >> palabra;

    cout << "La longitud es " << palabra.size();

    return 0;
}