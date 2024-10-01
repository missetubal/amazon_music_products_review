# Documetação sobre a Análise de Reviews de produtos musicais da Amazon

1. Análise do Negócio
    - Contexto
    A análise de sentimentos em avaliações de produtos musicais pode ajudar as empresas a entender melhor a percepção dos consumidores sobre seus produtos. Isso pode ser utilizado para melhorar produtos, direcionar marketing e aumentar a satisfação do cliente.
    - Objetivo
    O objetivo é classificar as avaliações como positivas, negativas ou neutras, permitindo uma análise mais profunda das opiniões dos clientes sobre instrumentos musicais.

2. Compreensão de Dados
    - Descrição das Variáveis
    reviewerID: ID do revisor -> Categórica;
    asin: ID do porduto -> Categórica;
    reviewerName: Nome do revisor -> Categórica;
    helpful: Classificação de utilidade -> Pode ser classificada entre útil/não útil;
    reviewText: Texto da revisão do produto -> Categórica;
    overall: Avaliação do produto (1 a 5) -> Numérica;
    summary: Resumo da revisão -> Categórica;
    unixReviewTime: Data da revisão em formato Unix;
    reviewTime: Data da revisão em formato legível;

3. Método
    - Qual o contexto do problema?
        O projeto envolve a análise de avaliações de produtos, particularmente instrumentos musicais, com o objetivo de classificar cada avaliação em duas categorias: positiva ou negativa. Esses dados vêm de avaliações textuais feitas por clientes. A ideia é extrair insights das opiniões dos consumidores, auxiliando nas decisões de negócios e compreensão de feedback.

    - Qual o problema?
        O problema consiste em classificar automaticamente as avaliações dos produtos com base no texto, utilizando algoritmos de aprendizado supervisionado. O objetivo é determinar se uma avaliação é positiva ou negativa, o que pode auxiliar empresas a melhorar seus produtos, serviços e estratégias de marketing.

    - Qual o experimento proposto?
        O experimento proposto envolve o uso de diferentes modelos de aprendizado de máquina, incluindo redes neurais simples, convolucionais (CNN), LSTM e bidirecionais LSTM, para comparar seu desempenho na tarefa de classificação de sentimentos. Foram testados diversos modelos e hiperparâmetros para identificar a solução que oferece o melhor equilíbrio entre precisão, recall e F1-score.

    - Quais resultados são esperados?
        Os resultados esperados são que, após o ajuste de hiperparâmetros e a aplicação de diferentes arquiteturas de redes neurais, será identificado um modelo capaz de atingir alta precisão e recall na classificação de sentimentos. A expectativa é que as redes neurais mais complexas, como CNN e LSTM, ofereçam um melhor desempenho, especialmente em termos de precisão na classe minoritária (negativa), que historicamente apresenta dificuldades em classificadores de aprendizado de máquina.

    - Como os dados são preparados?
        Os dados são preparados por meio de limpeza textual e tokenização. O texto das avaliações passa por um processo de pré-processamento que envolve:
            - Remoção de stopwords,
            - Lematização ou stemming,
            - Tokenização
            - Conversão em sequências numéricas (representação vetorial) para alimentar os modelos de redes neurais.

    - Qual modelo computacional foi escolhido? Por quê?
        O modelo computacional escolhido foi o CNN.
            - Apresentou uma acurácia de 90% com um bom equilíbrio entre precisão e recall, especialmente para a classe positiva;
            - A CNN é bem-sucedida em tarefas de processamento de linguagem natural (NLP) porque pode aprender padrões espaciais e temporais;
            - De acordo com os resultados, a CNN parece ter um desempenho estável em relação ao modelo LSTM e ao modelo simples, que mostraram sinais de sobreajuste, especialmente com a classe negativa. A capacidade de generalização do CNN pode ser um fator positivo;
            - O CNN é menos complexo em termos de recursos computacionais comparado aos modelos LSTM;
            - Os hiperparâmetros, como o número de filtros e o tamanho do kernel, podem ser facilmente ajustados, permitindo otimizar o modelo para o desempenho desejado sem a complexidade adicional de um modelo recurrente

4. Conclusão
    - Os resultados esperados foram encontrados?
        Os resultados indicam que alguns modelos, especialmente as Redes Neurais Convolucionais (CNN) e LSTM, alcançaram uma precisão considerável. O modelo CNN teve uma precisão em torno de 90%, enquanto o modelo LSTM teve uma precisão um pouco menor, em torno de 87%. No entanto, a classificação da classe negativa (0) apresentou precisão mais baixa em comparação à classe positiva (1), o que sugere que o modelo pode estar tendencioso em relação à classe positiva.
        Após testes de validação cruzada foi possível encontrar uma média de acurácia de 0.97 e um desvio padrão de 0.03.

    - Quais são as possíveis melhorias no modelo?
        - Ajustes de Hiperparâmetros;
        - Aumento de dados
        - Adição de mais camadas
        - Melhorar o refinamento de limpeza e pré-processamento de dados
        - Combinar diferentes modelos, por exemplo CNN e LSTM, para melhorar os resultados;

    - Próximos Passos
        -Implementar melhorias;
        - Analisar os casos em que o modelo erra;
        - Melhorar visualização de desempenho;
        - Além da acurácia, avaliar outras métricas;
        - Preparar para produção;
