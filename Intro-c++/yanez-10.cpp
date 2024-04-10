#include <iostream>

using namespace std;

int main () {
    float a, b;
    char op;
    cout << "Ingrese el primer numero: "; cin >> a;
    cout << "Ingrese el segundo numero: "; cin >> b;
    cout << "Ingrese la operacion: "; cin >> op;

    switch (op) {
        case '+':
            cout << a + b << "\n"; break;
        case '-':
            cout << a - b << "\n"; break;
        case '*':
            cout << a * b << "\n"; break;
        case '/':
            cout << a / b << "\n"; break;
        default:
            cout << "Error" << "\n"; return -1;
    }

    return 0;
}