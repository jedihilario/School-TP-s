#include <iostream>
#include <string>

using namespace std;

string reverse (string pal) {
    size_t size = pal.size();
    int mitad = size / 2;
    char aux = '\0';

    for (int i = 0; i < mitad; i++) {
        aux = pal[i];
        pal[i] = pal[size - 1 - i];
        pal[size - 1 - i] = aux;
    }

    return pal;
}

int main () {
    string palabra;
    cout << "Ingrese la palabra para dar vuelta: "; getline(cin, palabra);

    cout << "La palabra dada vuelta es: " << reverse(palabra) << "\n";

    return 0;
}