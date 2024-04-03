---
layout: post
title:  "Quantidade de caminhos em um grid"
author: danielsaad
excerpt: Quantos caminhos 
tags: dynamic-programming
math: true
---

Quantos caminhos de um ponto a outro podemos ter em um grid se os únicos movimentos possíveis são:

- para baixo;
- para direita;

Por exemplo, na figura abaixo, o número de caminhos possíveis do ponto $A$ ao ponto $B$ é $6$.

![Quantidade de caminhos?]({{ site.baseurl | append: "/static_files/2024-04-02-quantidade-caminhos-grid/grid-numero-caminhos.png" }}){: width="250"}

Quantos são os caminhos de $A$ para $C$?

A resposta é $70$.

Como chegar nesse número?

## Solução por programação dinâmica

Podemos resolver isso através de programação dinâmica. Obviamente o número de caminho a partir da posição $A$ para posição $A$ é $1$. O número de caminhos de $A$ para qualquer célula na linha de $A$ ou na coluna de $A$ também é $1$, pois para chegar nelas, bastar ir apenas para a direita, no primeiro caso, ou para baixo, no segundo caso.
Para uma célula qualquer, na posição $(i,j)$ da matriz, o número de caminhos equivale à soma dos caminhos do ponto inicial até $(i-1,j)$ com o número de caminhos do ponto inicial até $(i,j-1)$, o que nos dá o seguinte algoritmo:

```cpp
matrix[0][0] = 1;
for (i = 1; i < n; i++)
  matrix[i][0] = 1;
for (j = 1; j < n; j++)
  matrix[0][j] = 1;
for (i = 0; i < n; i++) {
  for (j = 0; j < m; j++) {
    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1];
  }
}
```

Usando a figura, o algoritmo computa a seguinte matriz:

```plain
1  1  1  1  1 
1  2  3  4  5 
1  3  6  10 15 
1  4  10 20 35 
1  5  15 35 70
```

A complexidade dessa solução é $\Theta(n\cdot m)$, sendo $n$ o número de linhas e $m$ o número de colunas no grid.
