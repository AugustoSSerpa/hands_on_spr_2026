# 📋 Prompt Cards — Foundation Models para Radiologia

## Prompt Card 0 — Setup e Preparação

Prompt card 0 - Você está rodando um experimento em Google Colab com GPU T4. Vamos comparar dois modelos que extraem características de raios-X de tórax: um treinado em fotos genéricas (ImageNet) e outro fine-tuned para radiologia (RAD-DINO). <button onclick="navigator.clipboard.writeText('Você está rodando um experimento em Google Colab com GPU T4. Vamos comparar dois modelos que extraem características de raios-X de tórax: um treinado em fotos genéricas (ImageNet) e outro fine-tuned para radiologia (RAD-DINO).')">📋 Copiar</button>

Nesta célula, faça o setup inicial:
- Instale e importe as bibliotecas que você achar necessária
- Defina `SEED = 42` para reproducibilidade
- Configure DEVICE para usar GPU se disponível
- Crie funções auxiliares que você vai reutilizar depois
- Deixe tudo pronto para carregar dados nos próximos passos

Não precisa de instruções super detalhadas — crie o que você achar que faz sentido para esse workflow!

---

## Prompt Card 1 — Carregar e Visualizar o Dataset

Prompt card 1 - Carregue o dataset PneumoniaMNIST em três splits com resolução 64×64. Pré-processe as imagens para que os valores fiquem entre 0 e 1 e converta para 3 canais (mesmo que grayscale). <button onclick="navigator.clipboard.writeText('Carregue o dataset PneumoniaMNIST em três splits com resolução 64×64. Pré-processe as imagens para que os valores fiquem entre 0 e 1 e converta para 3 canais (mesmo que grayscale).')">📋 Copiar</button>

---

## Prompt Card 2 - Extração de _embeddings_ + comparação

Prompt card 2 - Extraia os _embeddings_ de todas as 1000 imagens dos três splits para cada um dos modelos (um deles um EfficientNetB0 pré-treinado no ImageNet e o outro o RAD-DINO da Microsoft). <button onclick="navigator.clipboard.writeText('Extraia os _embeddings_ de todas as 1000 imagens dos três splits para cada um dos modelos (um deles um EfficientNetB0 pré-treinado no ImageNet e o outro o RAD-DINO da Microsoft).')">📋 Copiar</button>

Em seguida, usando as funções auxiliares definidas no PC0 (ou recrie-as se precisar) e em seguida plote o t-SNE dos embeddings do conjunto de teste lado a lado para EfficientNetB0 e RAD-DINO, colorindo pelas labels.

---

## Prompt Card 3 — Classificador 1: EfficientNetB0 (ImageNet)

**Prompt card 3 - Use os _embeddings_ do EfficientNetB0 pré-treinado no ImageNet e treine a cabeça classificadora, plote as curvas de treino e avalie no conjunto de teste. Calcule as métricas AUROC, Accuracy, Sensitivity, Specificity e F1-score.** <button onclick="navigator.clipboard.writeText('Use os _embeddings_ do EfficientNetB0 pré-treinado no ImageNet e treine a cabeça classificadora, plote as curvas de treino e avalie no conjunto de teste. Calcule as métricas AUROC, Accuracy, Sensitivity, Specificity e F1-score.')">📋 Copiar</button>

---

## Prompt Card 4 — Classificador 2: RAD-DINO (Radiologia)

Prompt card 4 - Use os _embeddings_ do RAD-DINO e treine a cabeça classificadora, plote as curvas de treino e avalie no conjunto de teste, usando os mesmos hiperparâmetros do EfficientNet para ter uma comparação justa. <button onclick="navigator.clipboard.writeText('Use os _embeddings_ do RAD-DINO e treine a cabeça classificadora, plote as curvas de treino e avalie no conjunto de teste, usando os mesmos hiperparâmetros do EfficientNet para ter uma comparação justa.')">📋 Copiar</button>

---

## Prompt Card 5 — Comparação de resultados

Prompt card 5 - Plotar um gráfico de barras comparando as métricas dos dois modelos, e imprimir uma tabela com a diferença entre eles. <button onclick="navigator.clipboard.writeText('Plotar um gráfico de barras comparando as métricas dos dois modelos, e imprimir uma tabela com a diferença entre eles.')">📋 Copiar</button>

---

## Prompt Card 6 — Inferência em Imagem Própria

Prompt card 6 - Permita que o usuário faça upload de uma imagem de raio-X de tórax do próprio computador. Rode a inferência com os dois modelos treinados, pré-processando a imagem do jeito correto. <button onclick="navigator.clipboard.writeText('Permita que o usuário faça upload de uma imagem de raio-X de tórax do próprio computador. Rode a inferência com os dois modelos treinados, pré-processando a imagem do jeito correto.')">📋 Copiar</button>

**⚠️ Inferência puramente demonstrativa — sem validade clínica.**