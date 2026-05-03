# 📋 Prompt Cards — Foundation Models para Radiologia

> As células de **Setup**, **Dataset** e **Embeddings** já estão pré-preenchidas no notebook — os participantes apenas executam essas células.
> Este arquivo contém os **Prompt Cards PC1–PC4** para projetar durante o workshop.

> **Como usar:** Selecione a célula vazia correspondente ao Prompt Card → abra o Gemini (`Ctrl+Shift+I` ou ícone ✦) → cole o prompt → o Gemini insere o código diretamente na célula → Execute a célula.

---

## Prompt Card 1 — Classificador 1: EfficientNetB0 (ImageNet)

Você está trabalhando em um notebook Google Colab com GPU T4. O ambiente já está configurado com todas as bibliotecas, SEED=42, device, funções auxiliares (`treinar_cabeca`, `avaliar`) e os embeddings do EfficientNetB0 e do RAD-DINO já foram extraídos e armazenados nas variáveis `emb_train_eff`, `emb_val_eff`, `emb_test_eff`, `labels_train`, `labels_val`, `labels_test`.

Insira o código na célula ativa do notebook (logo abaixo do título "Classificador 1: EfficientNetB0 (ImageNet)") que faça o seguinte:
- Use os embeddings `emb_train_eff`, `emb_val_eff`, `emb_test_eff` para treinar a cabeça classificadora com a função `treinar_cabeca`
- Plote as curvas de treino (loss e acurácia por época)
- Avalie no conjunto de teste com a função `avaliar`
- Calcule e exiba as métricas: Acurácia, Sensibilidade, Especificidade, VPP e VPN
- Plote a matriz de confusão

---

## Prompt Card 2 — Classificador 2: RAD-DINO (Radiologia)

Você está trabalhando em um notebook Google Colab com GPU T4. O ambiente já está configurado com todas as bibliotecas, SEED=42, device, funções auxiliares (`treinar_cabeca`, `avaliar`) e os embeddings do EfficientNetB0 e do RAD-DINO já foram extraídos. O classificador do EfficientNetB0 já foi treinado no bloco anterior.

Insira o código na célula ativa do notebook (logo abaixo do título "Classificador 2: RAD-DINO (Radiologia)") que faça o seguinte:
- Use os embeddings `emb_train_rad`, `emb_val_rad`, `emb_test_rad` para treinar a cabeça classificadora com a função `treinar_cabeca`, usando **exatamente os mesmos hiperparâmetros** do classificador anterior (fair comparison)
- Plote as curvas de treino (loss e acurácia por época)
- Avalie no conjunto de teste com a função `avaliar`
- Calcule e exiba as mesmas métricas: Acurácia, Sensibilidade, Especificidade, VPP e VPN
- Plote a matriz de confusão

---

## Prompt Card 3 — Comparação de Resultados

Você está trabalhando em um notebook Google Colab. Os dois classificadores já foram treinados e avaliados: os resultados do EfficientNetB0 estão disponíveis (métricas calculadas no bloco anterior) e os do RAD-DINO também.

Insira o código na célula ativa do notebook (logo abaixo do título "Comparação de Resultados") que faça o seguinte:
- Plote um gráfico de barras agrupadas comparando as métricas dos dois modelos (Acurácia, Sensibilidade, Especificidade, VPP, VPN)
- Imprima uma tabela com a diferença absoluta entre as métricas dos dois modelos, indicando qual modelo foi melhor em cada métrica

---

## Prompt Card 4 — Inferência em Imagem Própria

Você está trabalhando em um notebook Google Colab. Os dois modelos (EfficientNetB0 e RAD-DINO) estão treinados com seus respectivos classificadores. Os preprocessadores de imagem para cada modelo estão disponíveis como `transform_eff` e `processor_rad`.

Insira o código na célula ativa do notebook (logo abaixo do título "Inferência em Imagem Própria") que faça o seguinte:
- Permita que o usuário faça upload de uma imagem de raio-X de tórax do próprio computador (use `google.colab.files.upload()`)
- Pré-processe a imagem corretamente para cada modelo (`transform_eff` para EfficientNetB0 e `processor_rad` para RAD-DINO)
- Rode a inferência com os dois modelos treinados
- Exiba a imagem e o resultado de cada modelo lado a lado (classe predita e confiança em %)

**⚠️ Inferência puramente demonstrativa — sem validade clínica.**
