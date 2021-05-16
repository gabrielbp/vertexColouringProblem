/* Número de vértices */
param n, integer, >= 2;

/* Conjunto de vértices */
set VERTICES := {1..n};

/* Conjunto de cores */
set CORES := {1..n};

/* Conjunto dos arcos */
set ARCOS within (VERTICES cross VERTICES);

/* Variável se o vértice u é colorido com a cor c: 1 se sim; 0 caso contrário */
var x{u in VERTICES, c in CORES} binary;

/* Variável se a cor c é usada: 1 se sim; 0 caso contrário */
var y{c in CORES} binary;

/* Função Objetivo */
minimize qtdCores: sum{c in CORES} y[c];

/* Restrições */
s.t. verticeTemCor {u in VERTICES}: sum{c in CORES} x[u,c] = 1;
s.t. arcoSemDoisVerticesMesmaCorQueEhUtilizada {(u,v) in ARCOS, c in CORES}: x[u,c] + x[v,c] <= y[c];