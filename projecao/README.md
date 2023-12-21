Os arquivos exemplo_de_entrada_caso_x são dividido em múltiplas linhas.
A primeira linha descreve qual problema está sendo resolvido. Se na primeira linha estiver escrito "caso1" (sem as aspas), então está sendo resolvido o problema 1, que é: "Dado um poliedro P(A, b) e uma direção c, calcular o poliedro P(D, d) tal que a projeção P_H de P(A, b) sobre um conjunto H na direção c é tal que P_H = H ∩ P(D, d)".

Se você tiver escrito "caso1" (sem as aspas) na primeira linha, na linha subsequente você deve fornecer um conjunto de números de ponto flutuante separados por espaço. Esses números irão compor o vetor de direção c.

Se na primeira linha estivesse escrito "caso2" (sem as aspas), então está sendo resolvido o problema 2, que é: "Dado um poliedro P(A, b), decidir se ele é vazio ou não.".

Nesse caso, na linha subsequente você não precisaria fornecer o vetor c, diferentemente de como é feito no "caso1" (sem as aspas).

Nas linhas subsequentes, tanto para o "caso1" quanto para o "caso2", você deve fornecer as equações do poliedro conforme explicitado no enunciado do laboratório. Por exemplo:
-1x1 + 0x2 <= -1
-1x1 + -1x2 <= -5
2x1 + 1x2 <= 8
E na última linha você escrever "fim" (sem as aspas) e pressionar enter.




Seguem exemplos de como executar o programa com arquivos fornecidos:

Como executar o programa para dado um poliedro P(A, b) e uma direção c, calcular o poliedro P(D, d) tal que a projeção P_H de P(A, b) sobre um conjunto H na direção c é tal que P_H = H ∩ P(D, d):

python3 projecao.py cat < exemplo_de_entrada_caso_1


Como executar o programa para dado um poliedro P(A, b), decidir se ele é vazio ou não:

python3 projecao.py cat < exemplo_de_entrada_caso_2
