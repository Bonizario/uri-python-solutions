#include <iostream>
#define MAXN 100001

using namespace std;

int guilda[MAXN], numeroDeMembros[MAXN], ptsPorGuilda[MAXN];

// acessamos a guilda 'pai' que contém um determinado jogador
int find(int jogador) {
    if (guilda[jogador] == jogador)
        return jogador;

    return guilda[jogador] = find(guilda[jogador]);
}

void join(int A, int B) { // jogador A e jogador B
    A = find(A); // guilda 'pai' em que o jogador A se encontra
    B = find(B); // guilda 'pai' em que o jogador B se encontra

    // 1,2,3,4,5,6,7,8,9,10
    // 1,4,3,4,5,6,4,8,7,10
    if (A == B) {
        return;
    }

    // posição B que contém valor B, posição A que contém valor A
    // guilda[B] apontava para B (tinha valor B)
    // agora guilda[B] vai ser filha da guilda A, ou seja, guilda[B] vai ter valor A
    if (numeroDeMembros[A] > numeroDeMembros[B]) {
        guilda[B] = A;
        ptsPorGuilda[A] += ptsPorGuilda[B];
    } else if (numeroDeMembros[A] < numeroDeMembros[B]) {
        guilda[A] = B;
        ptsPorGuilda[B] += ptsPorGuilda[A];
    } else {
        guilda[A] = B;
        ptsPorGuilda[B] += ptsPorGuilda[A];
        numeroDeMembros[B]++;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int i, N, M, P, Q, A, B, guildaDoRafael, vitorias;

    while (true) {
        cin >> N >> M;
        if (N == 0 && M == 0) break;

        for (i = 1; i <= N; i++) {
            cin >> P;
            guilda[i] = i;
            ptsPorGuilda[i] = P;
        }

        vitorias = 0;
        for (i = 1; i <= M; i++) {
            cin >> Q >> A >> B;
            A = find(A); // guilda que contém o jogador A
            B = find(B); // guilda que contém o jogador B
            if (Q == 1) {
                join(A, B);
            } else {
                guildaDoRafael = find(1);

                if (A == guildaDoRafael && ptsPorGuilda[A] > ptsPorGuilda[B]) {
                    vitorias++;
                }
                if (B == guildaDoRafael && ptsPorGuilda[B] > ptsPorGuilda[A]) {
                    vitorias++;
                }
            }
        }

        cout << vitorias << "\n";
    }

    return 0;
}
