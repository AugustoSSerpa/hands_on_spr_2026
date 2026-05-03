# 📋 Prompt Cards — Foundation Models para Radiologia

> **PC0, PC1 e PC2 já estão pré-preenchidos no notebook** — os participantes apenas executam as células.
> Este arquivo contém os **Prompt Cards PC3–PC6** para projetar durante o workshop.

---

## Prompt Card 3

**Prompt card 3 (Classificador 1: EfficientNetB0 (ImageNet)) - Use os _embeddings_ do EfficientNetB0 pré-treinado no ImageNet e treine a cabeça classificadora, plote as curvas de treino e avalie no conjunto de teste. Calcule as métricas Acurácia, Sensibilidade, Especificidade, Valor Preditivo Positivo e Valor Preditivo Negativo. Plote também a matriz de confusão.**

---

## Prompt Card 4

Prompt card 4 (Classificador 2: RAD-DINO (Radiologia)) - Use os _embeddings_ do RAD-DINO e treine a cabeça classificadora, plote as curvas de treino e avalie no conjunto de teste, usando os mesmos hiperparâmetros e a mesma rede neural do EfficientNet para ter fair comparison. Calcule as mesmas métricas (Acurácia, Sensibilidade, Especificidade, Valor Preditivo Positivo e Valor Preditivo Negativo) e plote a matriz de confusão.

---

## Prompt Card 5

Prompt card 5 (Comparação de Resultados) - Plotar um gráfico de barras comparando as métricas dos dois modelos, e imprimir uma tabela com a diferença entre eles.

---

## Prompt Card 6

Prompt card 6 (Inferência em Imagem Própria) - Permita que o usuário faça upload de uma imagem de raio-X de tórax do próprio computador. Rode a inferência com os dois modelos treinados, pré-processando a imagem do jeito certo, e exiba o resultado lado a lado com a predição de cada modelo.

**⚠️ Inferência puramente demonstrativa — sem validade clínica.**
