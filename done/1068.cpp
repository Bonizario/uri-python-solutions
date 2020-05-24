#include <iostream>
#include <stack>

using namespace std;

int main() {
    string expressao;
    stack< char > pilha;
    bool ok;
    while (cin >> expressao) {
        ok = true;
        for (int i = 0; i < (int)expressao.size(); i++) {
            if (expressao[i] == '(') {
                pilha.push('(');
            } else if (expressao[i] == ')') {
                if (pilha.empty()) {
                    ok = false;
                    break;
                } else {
                    pilha.pop();
                }
            }
        }

        if (!pilha.empty()) {
            ok = false;
        }

        if (ok) {
            cout << "correct\n";
        } else {
            cout << "incorrect\n";
        }

        while (!pilha.empty()) {
            pilha.pop();
        }
    }
    return 0;
}
