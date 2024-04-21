#include <iostream>
#include <string>
#include <stdexcept>

using namespace std;

float from_frac_to_dec (int num, int den) {
    return (float) num / (float) den;
}

int string_length (string s) {
    return s.size();
}

void test () {
    int a = 3, b = 0;

    try {
        if (b == 0) throw "División por cero no permitida!";
        cout << from_frac_to_dec(a, b) << "\n";
    } catch (const char* msg) {
        cout << msg;
    }

    string text;
    cout << "Ingresa el texto para saber la longitud: "; cin >> text;

    try {
        if (text.size() == 0) throw "Error: la cadena debe contener caracteres";
        cout << "El texto tiene " << string_length(text) << " caracteres\n";
    } catch (const char* msg) {
        cout << msg;
    }

    int size = 0;
    cout << "Ingresa la cantidad de elementos del arreglo: ";
    try {
        cin >> size;
        if (size < 1) throw "El tamaño debe ser al menos 1";
    } catch (const char* msg) {
        cout << msg;
    }

    unsigned int arr[size];

    try {
        for (int i = 0; i < size; i++) {
            cout << "Ingresa el elemento " << i << ": "; cin >> arr[i];
            if (arr[i] < 0) throw "El valor debe ser positivo!";
        }
    }  catch (const char* msg) {
            cout << msg;
    }

    try {
        for (int i = -1; i < size; i++) {
            if (i < 0) throw "Error en la ejecucion!\n";
            cout << "Elemento " << i << ": " << arr[i] << "\n";
        }
    } catch (const char* msg) {
        cout << msg;
    }

    cout << "El programa finalizó con exito!\n";
}

int main () {
    test();

    return 0;
}