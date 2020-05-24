#include <iostream>

using namespace std;

int main() {
    unsigned short i, N, S, B, A, S1, B1, A1;
    float totalS = 0, totalB = 0, totalA = 0;
    float totalS1 = 0, totalB1 = 0, totalA1 = 0;
    string name;
    cin >> N;
    for (i = 0; i < N; i++) {
        cin >> name;
        cin >> S >> B >> A;
        cin >> S1 >> B1 >> A1;
        totalS += S;
        totalB += B;
        totalA += A;
        totalS1 += S1;
        totalB1 += B1;
        totalA1 += A1;
    }
    float perS = totalS1 / totalS * 100;
    float perB = totalB1 / totalB * 100;
    float perA = totalA1 / totalA * 100;
    cout.precision(2);
    cout.setf(ios::fixed);
    cout << "Pontos de Saque: "<< perS <<" %.\n";
    cout << "Pontos de Bloqueio: "<< perB <<" %.\n";
    cout << "Pontos de Ataque: "<< perA <<" %.\n";

    return 0;
}
