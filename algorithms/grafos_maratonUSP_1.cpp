/*
    Grafos podem ser escritos como um
    conjunto de vértices e arestas.

    G = (V, A);

    Self-loop;

    Grafos direcionados;

    Conexidade:
    - Para todo vértice, é possível
    traçar um caminho para os demais (continuamente).

    - Não é necessário testar todos os vértices,
    basta que em 1 vértice seja possível chegar nos demais.

    - Exemplos: internet, rede elétrica;

    Conexidade em grafos direcionados;

    Ciclo: dado um vértice, traçamos um caminho
    que retorna nele mesmo.

    Circuito: em um circuito, existem 2 caminhos
    possíveis de A para B. Caso 1 aresta seja retirada,
    restará somente 1 caminho.

    Árvores:
    - Grafos conexos e acíclicos, com o menor número
    possível de arestas. Ao retirar uma aresta,
    o grafo se torna desconexo. "Acíclico maximal".

    - Uma árvore de N vértices tem N-1 arestas.

    - Ao colocar 1 vértice, só é possível conectá-lo
    com 1 aresta. Qualquer outra aresta acarretará em
    um ciclo.

    Árvore geradora minimal;

    Bipartição;

    Aresta de corte: aresta que ao ser retirada torna
    o grafo desconexo;

    Caminho: ir de um vértice ao outro sem repetir arestas
    com um custo mínimo;
*/

/*
    Representação de grafos:
    - Matriz de adjacência: 0, 1;
    Checar valor M[i][j]: O(1);
    Armazenar todos os valores: O(n^2);
    Chega adjacência de um vértice: O(n);

    - Vetor de adjacência: vector<int> adj[n];

    Em um grafo completo K, existem
    C(n,2) arestas, ou ainda, n(n - 1)/2.
    Nesse caso específico, matriz é melhor pois
    procurar aresta é em O(1) e no vetor de
    adjacência é O(d), nesse caso O(n);

    - Representação implícita: tabuleiro de xadrez;
*/

/*
    Depth-First-Search (DFS);
    É um algoritmo que faz back-tracking,
    ao chegar em um "beco sem saída", ele retorna
    a algum vértice anterior, até percorrer todo o grafo;

    Em uma árvore existe o conceito de Pai;
    Os vértices mais externos possíveis, de grau 1, são chamados
    de "folha";

    No grafo não-direcionado o grau de um vértice é a
    quantidade de arestas que incidem nele;

    No grafo direcionado, existe o grau de entrada, quantidade
    de arestas que chegam no vértice, e o grau de saída,
    quantidade de arestas que saem do vértice;
    Os loops são tanto arestas de entradas quanto de saída,
    ou seja, contribuem em 2 para o grau de um vértice;

    Uma DFS gera uma árvore a partir do grafo original;
*/

void DFS(int v) {
    int visited[v] = 1;
    for (int x : adj[v]) {
        if (visited[x]) continue;
        pai[x] = v;
        DFS(x);
    }
}

/* Função roda em O(n) */
