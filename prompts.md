# 📋 Prompt Cards — Foundation Models para Radiologia

## Prompt Card 0

Você está rodando um experimento em Google Colab com GPU T4.

Objetivo geral do experimento:
Comparar dois modelos para extração de características de raios-X de tórax:
1. EfficientNetB0 pré-treinada em ImageNet.
2. RAD-DINO da Microsoft, específico para radiologia.

Regra principal:
Você deve executar SOMENTE a instrução do Prompt Card que eu fornecer na mensagem atual.

A cada interação, eu fornecerei apenas um Prompt Card, no formato:
Prompt Card X (título): [instrução]

Sua tarefa será:
1. Ler apenas o Prompt Card recebido na mensagem atual.
2. Gerar apenas o código necessário para cumprir exatamente esse Prompt Card.
3. Inserir o código em uma célula embaixo do título do Prompt Card, que está em markdown no notebook.
4. Não criar, modificar ou preencher células de outros Prompt Cards.
5. Não antecipar etapas futuras.
6. Não inferir próximos comandos.
7. Não criar código preparatório para tarefas que ainda não foram solicitadas.
8. Não adicionar validações, gráficos, treinos, comparações, análises ou salvamentos que não estejam explicitamente pedidos no Prompt Card atual.

Importante:
Mesmo que você consiga prever o próximo passo do experimento, NÃO faça isso.
Mesmo que pareça útil preparar código adicional, NÃO faça isso.
Mesmo que o código atual pudesse ser melhor com etapas futuras, NÃO inclua essas etapas.

Prompt card 0 (Setup e Preparação) - Nesta célula, faça o setup inicial:
- Instale e importe as bibliotecas que você achar necessária
- Defina `SEED = 42` para reproducibilidade
- Configure DEVICE para usar GPU se disponível
- Crie funções auxiliares que você vai reutilizar depois

---

## Prompt Card 1

Prompt card 1 (Carregar e Visualizar o Dataset) - Carregue 500 imagens de pneumonia (label 1) e 500 imagens normais (label 0) do dataset PneumoniaMNIST e em seguida divida as 1000 imagens em três splits (800/100/100), garantindo que cada um dos splits tenha a mesma proporção de 50% para cada classe. Carregue as imagens com resolução 64×64. Pré-processe as imagens para que os valores fiquem entre 0 e 1 e converta para 3 canais (mesmo que grayscale). Faça download automático da medmnist se não estiver presente. Plote 5 imagens aleatórias de cada split mostrando a classe (0=Normal ou 1=Pneumonia). Printe a proporção de casos em cada classe para cada um dos três grupos (treino, teste e validação).

---

## Prompt Card 2

Prompt card 2 (Extração de Embeddings + t-SNE) - Extraia os _embeddings_ de todas as 1000 imagens dos três splits para cada um dos modelos (EfficientNetB0 pré-treinado no ImageNet e RAD-DINO da Microsoft — `microsoft/rad-dino`). Armazene os embeddings.

Dicas arquiteturais:
- O RAD-DINO é um **modelo de extração de features, não de classificação** — carregue-o com `AutoModel`. O embedding global é o **token CLS**: `outputs.last_hidden_state[:, 0, :]`.
- Congele os parâmetros dos dois modelos.
- ⚠️ Pré-processamento independente por modelo: Os dois modelos têm pipelines de normalização diferentes. O EfficientNetB0 usa normalização ImageNet, enquanto o RAD-DINO não.
- Converter imagens para formato PIL para o RAD-DINO

Em seguida, plote o t-SNE dos embeddings do conjunto de **teste** lado a lado para EfficientNetB0 e RAD-DINO, colorindo os pontos pela classe. Coloque títulos indicando qual modelo é qual.

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
