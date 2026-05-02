# 📋 Prompt Cards — Foundation Models para Radiologia

## Prompt Card 0 — Setup e Preparação

Prompt card 0 - Você está rodando um experimento em Google Colab com GPU T4. Vamos comparar dois modelos que extraem características de raios-X de tórax: um treinado em fotos genéricas (ImageNet) e outro treinado especificamente em imagens radiológicas. Vamos usar essas características para treinar um classificador simples de pneumonia. Vamos usar o dataset PneumoniaMIST. Para cada instrução que eu lhe der, faça APENAS o que foi pedido e cole na célula respectiva do notebook. Não tente advinhar o que colocar nos prompts cards subsequentes, eu lhe passarei essas informações adiante.

Nesta célula, faça o setup inicial:
- Instale e importe as bibliotecas que você achar necessária
- Defina `SEED = 42` para reproducibilidade
- Configure DEVICE para usar GPU se disponível
- Crie funções auxiliares que você vai reutilizar depois
- Deixe tudo pronto para carregar dados nos próximos passos

Não precisa de instruções super detalhadas — crie o que você achar que faz sentido para esse workflow!

---

## Prompt Card 1 — Carregar e Visualizar o Dataset

Prompt card 1 - Carregue o dataset PneumoniaMNIST em três splits com resolução 64×64. Pré-processe as imagens para que os valores fiquem entre 0 e 1 e converta para 3 canais (mesmo que grayscale). Os labels devem ser vetores 1D. Faça um subsample aleatório reproduzível (use `SEED = 42`) para 800 imagens de treino, 100 de validação e 100 de teste. Imprima o shape e a distribuição de classes de cada split, e mostre uma grade com amostras do treino rotuladas pela classe.

---

## Prompt Card 2 - Extração de _embeddings_ + comparação

Prompt card 2 - Extraia os _embeddings_ de todas as 1000 imagens dos três splits para cada um dos modelos (um deles um EfficientNetB0 pré-treinado no ImageNet e o outro o RAD-DINO da Microsoft (`microsoft/rad-dino`), carregado via HuggingFace.
Em seguida, usando as funções auxiliares definidas no PC0 (ou recrie-as se precisar) e em seguida plote o t-SNE dos embeddings do conjunto de teste lado a lado para EfficientNetB0 e RAD-DINO, colorindo por classe. Salve os _embeddings_ pois usaremos depois para treinar os modelos classificadores.

---

## Prompt Card 3 — Classificador 1: EfficientNetB0 (ImageNet)

**Prompt card 3 - Use os _embeddings_ do EfficientNetB0 pré-treinado no ImageNet e treine a cabeça classificadora, plote as curvas de treino e avalie no conjunto de teste. Calcule as métricas AUC, Sensibilidade, Especificidade, Valor Preditivo Positivo, Valor Preditivo Negativo e Acurácica. Salve os resultados finais.
**---

## Prompt Card 4 — Classificador 2: RAD-DINO (Radiologia)

Prompt card 4 - Use os _embeddings_ do RAD-DINO e treine a cabeça classificadora, plote as curvas de treino e avalie no conjunto de teste, usando os mesmos hiperparâmetros do EfficientNet para ter uma comparação justa. Calcule as métricas AUC, Sensibilidade, Especificidade, Valor Preditivo Positivo, Valor Preditivo Negativo e Acurácica. Salve os resultados finais.

---

## Prompt Card 5 — Comparação de resultados

Prompt card 5 - Plotar um gráfico de barras comparando as métricas dos dois modelos, e imprimir uma tabela com a diferença entre eles.

---

## Prompt Card 6 — Inferência em Imagem Própria

Prompt card 6 - Permita que o usuário faça upload de uma imagem de raio-X de tórax do próprio computador. Rode a inferência com os dois modelos treinados, pré-processando a imagem do jeito correto para cada um, e exiba a imagem original junto com as probabilidades e a predição final de cada modelo lado a lado, assim como o tempo necessário para inferência em cada modelo.

**⚠️ Inferência puramente demonstrativa — sem validade clínica.**
