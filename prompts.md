# 📋 Prompt Cards — Foundation Models para Radiologia

## Prompt Card 0 — Setup e Preparação (8 min)

Você está rodando um experimento em Google Colab com GPU T4. Vamos comparar dois modelos que extraem características de raios-X de tórax: um treinado em fotos genéricas (ImageNet) e outro treinado especificamente em imagens radiológicas. Vamos usar essas características para treinar um classificador simples de pneumonia.

Nesta célula, faça o setup completo:
- Instale e importe as bibliotecas que você achar necessária (medmnist, torch, transformers, sklearn, matplotlib, etc)
- Defina `SEED = 42` para reproducibilidade
- Configure DEVICE para usar GPU se disponível
- Crie funções auxiliares que você vai reutilizar depois (por exemplo: funções para extrair embeddings, treinar um classificador simples, fazer gráficos de comparação, etc)
- Deixe tudo pronto para carregar dados nos próximos passos

Não precisa de instruções super detalhadas — crie o que você achar que faz sentido para esse workflow!

---

## Prompt Card 1 — Carregar e Visualizar o Dataset (7 min)

Carregue o dataset PneumoniaMNIST em três splits com resolução 64×64. Pré-processe as imagens para que os valores fiquem entre 0 e 1 e converta para 3 canais (mesmo que grayscale). Os labels devem ser vetores 1D. Faça um subsample aleatório reproduzível (use `SEED = 42`) para 800 imagens de treino, 100 de validação e 100 de teste. Imprima o shape e a distribuição de classes de cada split, e mostre uma grade com amostras do treino rotuladas pela classe.

---

## Prompt Card 2 — Extrator 1: EfficientNetB0 (ImageNet) (12 min)

Use o EfficientNetB0 pré-treinado no ImageNet como extrator de features completamente congelado. Extraia os embeddings dos três splits usando as funções auxiliares definidas no PC0 (ou recrie-as se precisar), treine a cabeça classificadora, plote as curvas de treino e avalie no conjunto de teste.

**⏳ Extração: ~5s | Treino: ~30s no T4.**

---

## Prompt Card 3 — Extrator 2: RAD-DINO (Radiologia) (12 min)

Repita o processo do PC2 com o RAD-DINO da Microsoft (`microsoft/rad-dino`), carregado via HuggingFace. Congele o backbone, extraia os embeddings, treine a mesma cabeça classificadora e avalie no teste, usando os mesmos hiperparâmetros do EfficientNet para ter uma comparação justa.

**⏳ Download (~87MB): ~30s | Extração: ~3s | Treino: ~20s no T4.**

---

## Prompt Card 4 — t-SNE + Comparação de Métricas (8 min)

Use os embeddings e resultados de avaliação dos dois modelos já calculados para: (1) plotar o t-SNE dos embeddings do conjunto de teste lado a lado para EfficientNetB0 e RAD-DINO, colorindo por classe; (2) plotar um gráfico de barras comparando AUC, F1, Sensibilidade, Especificidade e Acurácia dos dois modelos, e imprimir uma tabela com a diferença entre eles.

---

## Bônus — Inferência em Imagem Própria

Permita que o usuário faça upload de uma imagem de raio-X de tórax do próprio computador. Rode a inferência com os dois modelos treinados, pré-processando a imagem do jeito correto para cada um, e exiba a imagem original junto com as probabilidades e a predição final de cada modelo lado a lado.

**⚠️ Inferência puramente demonstrativa — sem validade clínica.**
