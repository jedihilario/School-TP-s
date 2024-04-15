#include <iostream>

using namespace std;

bool isPositiveOrZero (int n) {
    return n >= 0;
}

int factorial (int n) {
    if (n == 1) return 1;
    return n * factorial(n - 1);
}

float area (int b, int h) {
    return (float) b * float (h) / 2;
}

bool primo (int n) {
    int mid = n / 2 + 1;

    for (int i = 2; i < mid; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main () {
    int n = 0;
    cout << "Ingresa un numero para saber el factorial: "; cin >> n;
    if (isPositiveOrZero(n)) cout << "Su factorial es: " << factorial(n) << "\n";
    else cout << "El numero no es valido!\n";

    cout << "Ingresa un numero para saber si es primo: "; cin >> n;
    if (isPositiveOrZero(n)) cout << primo(n) ? "Es primo!\n" : "No es primo :(\n";
    else cout << "El numero debe ser natural!\n";

    int b, h;
    cout << "Ingresa los valores de la base y la altura: "; cin >> b >> h;
    if (isPositiveOrZero(b) && isPositiveOrZero(h)) {
        cout << "El area de ese triangulo es: " << area(b, h) << "\n";
    } else cout << "Los valores deben ser positivos!\n";

    return 0;
}