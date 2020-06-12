#include <iostream>
#include <cmath>

using namespace std;

struct Planeta {
    int x, y, h;
};

int checaPlaneta(double m, int x1, int y1, int x2, int y2) {
    int y = m * (x1 - x2) + y2;
    if (y > y1)
        return -1;
    else if (y < y1)
        return 1;
    else
        return 0;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    double x1, y1, x2, y2, d;
    int i, n;
    cin >> x1 >> y1 >> x2 >> y2;

    d = sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));

    int esquerda = 0, direita = 0, hab_esquerda = 0, hab_direita = 0, em_cima = 0;

    cin >> n;
    Planeta planetas[n];
    for (i = 0; i < n; i++)
        cin >> planetas[i].x >> planetas[i].y >> planetas[i].h;


    double m = (y2-y1) / (x2-x1);
    int result;
    for (i = 0; i < n; i++) {
        Planeta p = planetas[i];
        result = checaPlaneta(m, x2, y2, p.x, p.y);
        if (result == -1) {
            esquerda++;
            hab_esquerda += p.h;
        } else if (result == 1) {
            direita++;
            hab_direita += p.h;
        } else {
            em_cima++;
        }
    }


    cout << "Relatorio Vogon #35987-2\n";
    cout.precision(2);
    cout.setf(ios::fixed);
    cout << "Distancia entre referencias: " << d << " anos-luz\n";
    cout << "Setor Oeste:\n";
    cout << "- " << esquerda << " planeta(s)\n";
    cout << "- " << hab_esquerda << " bilhao(oes) de habitante(s)\n";
    cout << "Setor Leste:\n";
    cout << "- " << direita << " planeta(s)\n";
    cout << "- " << hab_direita << " bilhao(oes) de habitante(s)\n";
    cout << "Casualidades: " << em_cima << " planeta(s)\n";

    return 0;
}
