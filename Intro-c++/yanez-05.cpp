#include <iostream>

using namespace std;

float promedio (int* nums, size_t n) {
    int sum = 0;

    for (size_t i = 0; i < n; i++) {
        sum += nums[i];
    }

    return sum / n;
}

int main () {
    size_t c;
    cout << "Cuantos numeros queres ingrear?\n"; cin >> c;

    int array[c];

    for (size_t i = 0; i < c; i++) {
        cout << "Ingresa el " << i + 1 << " numero: "; cin >> array[i];
    }

    cout << "El promedio es: " << promedio(array, c) << "\n";

    return 0;
}