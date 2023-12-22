# Entropia de Shannon

A entropia de Shannon é uma medida de incerteza ou quantidade de informação em uma variável aleatória. Proposta por Claude Shannon, um engenheiro elétrico e matemático, em seu trabalho seminal sobre teoria da informação, publicado em 1948.

A entropia de Shannon é definida matematicamente como:

$$
H(X) = -\sum_{i=1}^{n} P(x_i) \log_2 P(x_i)
$$

Este código Python define uma função chamada prob_ocurr que calcula a entropia de Shannon para uma determinada sequência de informações.

```python
import math

def prob_ocurr(info):
    sum_shannon = 0  # Variável para armazenar a soma das contribuições de entropia
    size = len(info)  # Tamanho da sequência de informações

    lax = list(map(chr, range(97, 123)))  # Lista de letras minúsculas de 'a' a 'z'

    for x in lax:
        total_occurrences = info.count(x)  # Conta o número de ocorrências da letra x na sequência
        prob = total_occurrences / size     # Calcula a probabilidade de ocorrência da letra x

        try:
            prob_log = math.log2(round(prob, 1))  # Calcula o logaritmo na base 2 da probabilidade arredondada
            entropy = -prob * prob_log  # Calcula a contribuição da letra x para a entropia
            sum_shannon += entropy  # Adiciona a contribuição à soma total de entropia
        except ValueError:
            print(f"Erro para {x}")

    print(f"Contribuições parciais de entropia: {sum_shannon}")
    print(f"Entropia de Shannon total: {sum_shannon}")

# Exemplo de uso
prob_ocurr("araraquara")
```

O código itera sobre todas as letras minúsculas de 'a' a 'z' e, para cada letra, calcula a probabilidade de ocorrência na sequência fornecida. Em seguida, calcula o logaritmo na base 2 dessa probabilidade arredondada e multiplica pela probabilidade. O resultado é a contribuição dessa letra específica para a entropia de Shannon. Essa contribuição é adicionada a uma lista parcial (sum_shannon), e a lista parcial é exibida a cada iteração.

Ao final da execução da função prob_ocurr("araraquara"), você terá as contribuições parciais para a entropia de Shannon de cada letra na sequência, juntamente com a soma acumulada dessas contribuições. Note que o código tem um bloco except que imprime a letra para lidar com possíveis exceções, mas não fornece muitos detalhes sobre o propósito dessa parte do código.

## Teoria da Informação
A entropia de Shannon é central na teoria da informação, fornecendo uma medida de incerteza ou surpresa associada a uma variável aleatória. Quanto maior a entropia, maior a incerteza e, portanto, maior a quantidade de informação necessária para descrever a variável.

## Compressão de Dados
Em compressão de dados, a entropia é usada para quantificar a "informação média" em uma fonte de dados. Algoritmos de compressão, como o algoritmo de Huffman, utilizam a entropia para atribuir códigos mais curtos às mensagens mais prováveis, economizando espaço de armazenamento.

## Criptografia
Na criptografia, a entropia é usada para medir a aleatoriedade ou imprevisibilidade de chaves criptográficas. Chaves com alta entropia são mais difíceis de serem quebradas por métodos de força bruta, pois não exibem padrões previsíveis.

## Teoria da Comunicação
Em sistemas de comunicação, a entropia é usada para medir a eficiência da transmissão de informação. Quanto maior a entropia de uma fonte de informação, maior a capacidade necessária para transmitir essa informação de forma eficiente.

## Aprendizado de Máquina
Em contextos de aprendizado de máquina e estatística, a entropia é usada em algoritmos de classificação, como as árvores de decisão. Ela é usada para avaliar a impureza ou homogeneidade dos conjuntos de dados e orientar a seleção de atributos durante o treinamento do modelo.

## Processamento de Sinais e Imagens
A entropia também encontra aplicação em processamento de sinais e imagens, onde pode ser usada para caracterizar a complexidade de um sinal ou imagem.




