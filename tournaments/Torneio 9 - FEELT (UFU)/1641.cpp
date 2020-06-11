#include <iostream>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int i, R, largura, altura;
    double diametro, diagonal;

    int pizza = 1;
    while (true) {
        cin >> R;
        if (R == 0) break;

        cin >> largura >> altura;

        diametro = 2*R;
        diagonal = sqrt(largura*largura + altura*altura);

        if (diagonal <= diametro)
            cout << "Pizza " << pizza++ << " fits on the table.\n";
        else
            cout << "Pizza " << pizza++ << " does not fit on the table.\n";
    }

    return 0;
}
