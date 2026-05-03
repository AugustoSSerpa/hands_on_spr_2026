# 📋 Prompt Cards — Foundation Models para Radiologia

> As células de **Setup**, **Dataset** e **Embeddings** já estão pré-preenchidas no notebook — os participantes apenas executam essas células.
> Este arquivo contém os **Prompt Cards PC1–PC4** para projetar durante o workshop.

> **Como usar:** Selecione a célula vazia correspondente ao Prompt Card → abra o Gemini (`Ctrl+Shift+I` ou ícone ✦) → cole o prompt → o Gemini insere o código diretamente na célula → Execute a célula.

---

## Prompt Card 1 — Classificador 1: EfficientNetB0 (ImageNet)

Estou em um notebook Google Colab com GPU T4. As células anteriores já rodaram: todas as bibliotecas estão importadas, o dataset PneumoniaMNIST está carregado nos splits de treino, validação e teste, e os embeddings do EfficientNetB0 já foram extraídos e estão disponíveis em memória.

**Faça apenas o seguinte nesta célula — nada além disso:**
- Treine um classificador usando os embeddings do EfficientNetB0
- Plote as curvas de treino (loss e métrica por época)
- Avalie no conjunto de teste: calcule e exiba Acurácia, Sensibilidade, Especificidade, VPP e VPN
- Plote a matriz de confusão

Comente cada bloco de código explicando o que está fazendo e por quê.

Não crie células adicionais, não treine o RAD-DINO, não faça comparações — apenas o classificador do EfficientNetB0.

---

## Prompt Card 2 — Classificador 2: RAD-DINO (Radiologia)

Estou em um notebook Google Colab com GPU T4. As células anteriores já rodaram: todas as bibliotecas estão importadas, os embeddings do RAD-DINO já foram extraídos e estão disponíveis em memória. O classificador do EfficientNetB0 já foi treinado na célula anterior.

**Faça apenas o seguinte nesta célula — nada além disso:**
- Treine um classificador usando os embeddings do RAD-DINO, com a mesma arquitetura e os mesmos hiperparâmetros usados para o EfficientNetB0 (fair comparison)
- Plote as curvas de treino (loss e métrica por época)
- Avalie no conjunto de teste: calcule e exiba as mesmas métricas (Acurácia, Sensibilidade, Especificidade, VPP, VPN)
- Plote a matriz de confusão

Comente cada bloco de código explicando o que está fazendo e por quê.

Não crie células adicionais, não compare os modelos ainda — apenas o classificador do RAD-DINO.

---

## Prompt Card 3 — Comparação de Resultados

Estou em um notebook Google Colab. Os dois classificadores (EfficientNetB0 e RAD-DINO) já foram treinados nas células anteriores e suas métricas estão disponíveis em memória.

**Faça apenas o seguinte nesta célula — nada além disso:**
- Plote um gráfico de barras agrupadas comparando as métricas dos dois modelos (Acurácia, Sensibilidade, Especificidade, VPP, VPN)
- Imprima uma tabela mostrando a diferença entre as métricas, indicando qual modelo foi melhor em cada uma

Comente cada bloco de código explicando o que está fazendo e por quê.

Não faça inferência, não carregue imagens novas — apenas a comparação.

---

## Prompt Card 4 — Inferência em Imagem Própria

Estou em um notebook Google Colab. Os dois modelos (EfficientNetB0 e RAD-DINO) estão treinados e prontos para inferência. Todos os pré-processadores de imagem necessários estão disponíveis em memória.

**Faça apenas o seguinte nesta célula — nada além disso:**
- Permita que o usuário faça upload de uma imagem de raio-X de tórax do próprio computador
- Pré-processe a imagem corretamente para cada modelo
- Rode a inferência com os dois modelos treinados
- Exiba a imagem e o resultado lado a lado: classe predita e confiança em % para cada modelo

Comente cada bloco de código explicando o que está fazendo e por quê.

**⚠️ Inferência puramente demonstrativa — sem validade clínica.**
