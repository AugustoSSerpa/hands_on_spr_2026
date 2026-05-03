# 📋 Prompt Cards — Foundation Models para Radiologia

> As células de **Setup**, **Dataset** e **Embeddings** já estão pré-preenchidas no notebook — os participantes apenas executam essas células.
> Este arquivo contém os **Prompt Cards PC1–PC4** para projetar durante o workshop.

> **Como usar:** Selecione a célula vazia correspondente ao Prompt Card → abra o Gemini (`Ctrl+Shift+I` ou ícone ✦) → cole o prompt → o Gemini insere o código diretamente na célula → Execute a célula.

---

## Prompt Card 1 — Classificador 1: EfficientNetB0 (ImageNet)

Estou em um notebook Google Colab com GPU T4. O ambiente já está configurado: bibliotecas importadas, embeddings do EfficientNetB0 extraídos para treino, validação e teste, e as labels correspondentes disponíveis.

Nesta célula, treine um classificador usando os embeddings do EfficientNetB0. Plote as curvas de treino e avalie no conjunto de teste calculando Acurácia, Sensibilidade, Especificidade, VPP e VPN. Plote a matriz de confusão.

---

## Prompt Card 2 — Classificador 2: RAD-DINO (Radiologia)

Estou em um notebook Google Colab com GPU T4. O ambiente já está configurado: bibliotecas importadas, embeddings do RAD-DINO extraídos para treino, validação e teste. O classificador do EfficientNetB0 já foi treinado no bloco anterior.

Nesta célula, treine um classificador usando os embeddings do RAD-DINO com os mesmos hiperparâmetros e arquitetura do classificador anterior. Plote as curvas de treino e avalie no teste calculando as mesmas métricas (Acurácia, Sensibilidade, Especificidade, VPP, VPN). Plote a matriz de confusão.

---

## Prompt Card 3 — Comparação de Resultados

Estou em um notebook Google Colab. Os dois classificadores (EfficientNetB0 e RAD-DINO) já foram treinados e suas métricas calculadas nos blocos anteriores.

Nesta célula, compare os dois modelos: plote um gráfico de barras agrupadas com as métricas de ambos e imprima uma tabela mostrando a diferença entre eles, indicando qual foi melhor em cada métrica.

---

## Prompt Card 4 — Inferência em Imagem Própria

Estou em um notebook Google Colab. Os dois modelos (EfficientNetB0 e RAD-DINO) estão treinados e prontos para inferência.

Nesta célula, permita que o usuário faça upload de uma imagem de raio-X de tórax do próprio computador. Pré-processe a imagem corretamente para cada modelo e rode a inferência com os dois. Exiba a imagem e o resultado lado a lado — classe predita e confiança em % para cada modelo.

**⚠️ Inferência puramente demonstrativa — sem validade clínica.**
