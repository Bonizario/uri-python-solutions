#include <iostream>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int i, c, L;
    double area;

    cin >> c;
    for (i = 0; i < c; i++) {
        cin >> L;

        area = 1.25 * L * L / tan(M_PI / 5);

        cout.precision(3);
        cout.setf(ios::fixed);
        cout << area << "\n";
    }

    return 0;
}
