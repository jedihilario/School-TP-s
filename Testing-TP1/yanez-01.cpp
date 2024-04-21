#include <iostream>
#include <cassert>
#include <string>

using namespace std;

float area_triangle (int b, int h) {
    return ((float) b * (float) h / 2);
}

bool isEven (int n) {
    return n % 2 == 0;
}

int factorial (int n) {
    if (n == 1) return 1;
    return n * factorial(n - 1);
}

bool isPrime (unsigned int n) {
    int t = n / 2 + 1;
    while (t > 1) {
        if (n % t == 0) return false;
        t--;
    }

    return true;
}

string concat (string a, string b) {
    return a + b;
}

void test () {
    // Ej. 1
    assert(area_triangle(2, 2) == 2.0);
    assert(area_triangle(2, 5) == 5.0);
    assert(area_triangle(3, 7) == 10.5);
    // Ej. 2
    assert(isEven(2));
    assert(!isEven(3));
    // Ej. 3
    assert(factorial(4) == 24);
    // Ej. 4
    assert(isPrime(7));
    assert(!isPrime(2));
    // Ej. 5
    assert(concat("Hola ", "Mundo") == "Hola Mundo");

    cout << "Todos los test pasaron!!\n";
}

int main () {
    test();

    return 0;
}
