# ?? Prompt Card — Fine-tuning para Radiologia
## Hands-on Vibe Coding · SPR 2026
### Imprimir uma folha por participante (ou projetar no telão)

---

## ?? Antes de começar

1. Ative o **GPU T4**: Menu `Ambiente de execução` ? `Alterar tipo de hardware` ? T4 GPU ? Salvar
2. Execute as duas células pré-preenchidas de **Setup** (instalação + funções auxiliares)
3. Siga os Prompt Cards na ordem

---

## Prompt 1 — Carregar e Visualizar o Dataset (8 min)

> Usando a biblioteca `medmnist` (já importada), carregue o `PneumoniaMNIST` com `download=True` e `size=64` para os splits de treino, validação e teste. Em seguida:
> 1. Converta as imagens para float32 no intervalo [0, 1], shape `(N, 64, 64, 3)` — repita o canal cinza 3 vezes usando `np.repeat` (necessário para o EfficientNetB0).
> 2. Converta os labels para arrays 1D de inteiros.
> 3. Imprima shape e distribuição de classes (Normal vs Pneumonia) de cada split.
> 4. Plote uma grade 4×4 com 16 imagens aleatórias do treino. Use `cmap='gray'` e coloque o label (Normal/Pneumonia) como título de cada imagem. Use `np.random.default_rng(42)` para selecionar as imagens.

**Resultado esperado:** shape (4708, 64, 64, 3) para treino + grade de imagens

---

## Prompt 2 — Construir o Modelo com EfficientNetB0 (8 min)

> Usando TensorFlow/Keras e a variável `efficientnet_base` já carregada (EfficientNetB0 sem topo, pesos ImageNet, pooling='avg', trainable=False), construa um modelo Sequential para classificação binária de imagens 64×64×3:
> 1. Use `efficientnet_base` como primeira camada (base congelada — não altere o trainable).
> 2. Adicione BatchNormalization.
> 3. Adicione Dense(256, activation='relu').
> 4. Adicione Dropout(0.4, seed=42).
> 5. Adicione Dense(1, activation='sigmoid') — classificação binária.
> 6. Compile com Adam(learning_rate=1e-3), loss='binary_crossentropy', metrics=['accuracy', tf.keras.metrics.AUC(name='auc')].
> 7. Mostre o summary do modelo. Imprima também quantos parâmetros são treináveis vs congelados.

**Resultado esperado:** ~262K treináveis vs ~4.05M congelados

---

## Prompt 3 — Treinar o Modelo (12 min)

> Treine o modelo criado anteriormente usando `X_train`, `y_train`, `X_val`, `y_val`. Use:
> - `epochs=25`, `batch_size=64`
> - Pré-processe as entradas com `tf.keras.applications.efficientnet.preprocess_input(X * 255.0)` dentro de uma função de treino ou passando os dados já pré-processados.
> - Callbacks: `EarlyStopping(monitor='val_auc', patience=6, restore_best_weights=True, mode='max')` e `ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3)`.
> - Após o treino, plote dois gráficos lado a lado: curva de loss (treino vs validação) e curva de AUC (treino vs validação) por época.
> - Imprima a AUC final no conjunto de validação.

**Resultado esperado:** AUC validação = 0.92 com T4 em ~3–5 min

---

## Prompt 4 — Grad-CAM: o que o modelo "olha"? (8 min)

> Chame a função `plotar_gradcam()` que já está definida, passando os seguintes argumentos:
> - `modelo`: o modelo treinado
> - `X_test`: o array de imagens de teste (já pré-processadas como float [0,1] com 3 canais)
> - `y_test`: os labels reais
> - `y_pred`: as predições binárias já calculadas
> - `y_proba`: as probabilidades brutas do modelo
> - `n_corretos=3, n_errados=3`
>
> Antes de chamar a função, pré-processe X_test com `tf.keras.applications.efficientnet.preprocess_input(X_test * 255.0)` e salve em uma variável `X_test_prep_gcam`. Passe `X_test_prep_gcam` como o argumento `X_test` da função.

**Resultado esperado:** Grade com imagem original, heatmap e sobreposição para 6 imagens

---

## ?? Prompts de Correção

| Situação | O que pedir ao Gemini |
|---|---|
| Erro de shape | "O shape das imagens está errado. Corrija para que seja (N, 64, 64, 3) com dtype float32." |
| `efficientnet_base` não encontrado | "A variável `efficientnet_base` não está definida nesta célula. Ela foi criada na célula de t-SNE. Carregue-a novamente com EfficientNetB0 sem topo, pesos ImageNet, pooling='avg', trainable=False." |
| Treino não inicia | "O model.fit() retornou erro. Verifique se X_train_prep e y_train estão definidos e se o modelo foi compilado." |
| Grad-CAM com erro de layer | "A função plotar_gradcam deu erro ao buscar a última camada Conv2D. Adicione um print das camadas do modelo com `[l.name for l in modelo.layers]` para debug." |
| GPU não ativa | "O treino está lento. Verifique com `tf.config.list_physical_devices('GPU')` se o GPU está disponível." |

---

## ?? Valores de Referência (SEED=42, T4 GPU)

| Métrica | Esperado |
|---|---|
| AUC-ROC (teste) | 0.92 – 0.96 |
| Sensibilidade | 0.88 – 0.95 |
| Especificidade | 0.80 – 0.90 |
| Épocas até convergir | 8 – 18 |
| Tempo de treino (T4) | 3 – 5 min |
| Tempo de treino (CPU) | 15 – 25 min |
| Params treináveis | ~262K |
| Params congelados | ~4.05M |

---

## ?? Links do evento

- **Notebook Colab:** https://colab.research.google.com/github/AugustoSSerpa/hands_on_spr_2026/blob/main/hands_on_spr_2026.ipynb
- **GitHub:** https://github.com/AugustoSSerpa/hands_on_spr_2026
- **MedMNIST:** https://medmnist.com
