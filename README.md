# Análise de Sentimentos de Avaliações de Instrumentos Musicais

## Descrição do Projeto

Este projeto tem como objetivo classificar análises de produtos de instrumentos musicais em positivas ou negativas. Utilizamos técnicas de aprendizado de máquina, incluindo redes neurais convolucionais (CNN) e redes neurais recorrentes (LSTM), para entender melhor as opiniões dos clientes e oferecer insights valiosos para fabricantes e consumidores.

## Contexto do Problema

No mercado de instrumentos musicais, as opiniões dos clientes desempenham um papel fundamental na decisão de compra. Compreender o sentimento por trás dessas análises pode ajudar os fabricantes a melhorar seus produtos e serviços, além de ajudar os consumidores a tomar decisões mais informadas.

## Tecnologias Utilizadas

- Python
- TensorFlow/Keras
- Scikit-learn
- NLTK (Natural Language Toolkit)
- Streamlit (para visualização)

## Estrutura do Projeto

│   └── Musical_instruments_reviews.csv  
│   └── amazon_review.ipynb  # Análise exploratória dos dados
└── README.md

## Execute o aplicativo Streamlit

streamlit run src/streamlit_app.py

## Resultados Esperados

Após a execução do modelo, esperamos obter:
    - Uma acurácia média de pelo menos 90% na classificação das análises.
    - Insights sobre os sentimentos predominantes nas análises de produtos.

## Melhorias Futuras

    - Testar diferentes arquiteturas de redes neurais e hiperparâmetros.
    - Aumentar o conjunto de dados com mais análises de produtos.
    - Implementar técnicas de aumento de dados para melhorar a robustez do modelo.
