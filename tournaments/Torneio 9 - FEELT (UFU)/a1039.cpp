#include <iostream>
#include <cmath>

using namespace std;

bool rico(int r1,int x1,int y1,int r2,int x2,int y2) {
    double dist;
    if (r1 < r2)
        return false;
    else {
        dist = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
        if ((r1-r2) >= dist)
            return true;
        else
            return false;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int r1,x1,y1,r2,x2,y2;
    double rich;

    while (cin >>r1>>x1>>y1>>r2>>x2>>y2) {
        rich = rico(r1,x1,y1,r2,x2,y2);
        if (rich)
            cout << "RICO\n";
        else
            cout << "MORTO\n";
    }

    return 0;
}
