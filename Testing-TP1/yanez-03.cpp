#include <iostream>
#include <string>

using namespace std;

bool secure_password (string password) {
    return password.size() > 7;
}

bool userValid (string s) {
    for (char c : s) {
        if (!isalnum(c)) return false;
    }

    return true;
}

bool isPositiveOrZero (int n) {
    return n >= 0;
}

int factorial (int n) {
    if (n == 1) return 1;
    return n * factorial(n - 1);
}

float area_triangulo (int b, int h) {
    return (float) b * float (h) / 2;
}

bool primo (int n) {
    int mid = n / 2 + 1;

    for (int i = 2; i < mid; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

void test () {
    int n = 0;
    cout << "Ingresa un numero para saber el factorial: "; cin >> n;
    while (!isPositiveOrZero(n)) {
        cout << "Error: El número debe ser positivo o cero!\n"; cin >> n;
    }
    cout << "El factorial de " << n << " es: " << factorial(n) << '\n';

    cout << "Ingresa un numero para saber si es primo: "; cin >> n;
    while (!isPositiveOrZero(n)) {
        cout << "Error: El número debe ser positivo!\n"; cin >> n;
    }
    cout << "El " << n;
    if (primo(n)) cout << " es primo!\n";
    else cout << " no es primo!\n";

    int b, h;
    cout << "Ingresa los valores de la base y la altura: "; cin >> b >> h;
    while (!(isPositiveOrZero(b) && isPositiveOrZero(h))) {
        cout << "Los valores deben ser positivos!\nIngresa los valores nuevamente: ";
        cin >> b >> h;
    }
    cout << "El area de ese triangulo es: " << area_triangulo(b, h) << '\n';

    string user;
    cout << "Ingrese un nombre de usuario (solo letras y/o numeros): "; cin >> user;
    while (!userValid(user)) {
        cout << "El usuario no es valido!\nIntente de nuevo: "; cin >> user;
    }
    cout << "Usuario guardado\n";

    string passwd;
    cout << "Ingrese la contraseña del usuario: "; cin >> passwd;
    while (!secure_password(passwd)) {
        cout << "La contraseña no es segura, ingrese otra: "; cin >> passwd;
    }
    cout << "Contraseña guardada\n";
}

int main () {
    test();
    cout << "Programa finalizado!\n";

    return 0;
}