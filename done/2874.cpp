// 2874 - Frase Binária
#include <iostream>
#include <cmath>

using namespace std;

unsigned binaryToDecimal(unsigned n) {
    unsigned decimalNumber = 0, i = 0, remainder;
    while (n != 0) {
        remainder = n % 10;
        n /= 10;
        decimalNumber += remainder*pow(2, i);
        i++;
    }
    return decimalNumber;
}

int main() {
    unsigned i, N, binary;
    string message = "";
    char letter;

    while (true) {
        cin >> N;
        if (!cin) break;
        for (i = 0; i < N; i++) {
            cin >> binary;
            letter = char(binaryToDecimal(binary));
            message += letter;
        }
        cout << message << "\n";
        message = "";
    }
    return 0;
}
