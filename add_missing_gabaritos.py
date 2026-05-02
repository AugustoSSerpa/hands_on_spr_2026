import json

with open('hands_on_spr_2026.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Células para adicionar ao final (PC4, PC5, PC6)
new_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### 🏗️ Classificador 2: RAD-DINO (Radiologia)"],
        "id": "gabarito-pc4-title"
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": ["# GABARITO — Classificador 2: RAD-DINO (Radiologia)\n# Use os embeddings do RAD-DINO e treine a cabeça classificadora\n# com os mesmos hiperparâmetros do EfficientNet para comparação justa\n\nprint('Treinar cabeça classificadora com RAD-DINO...')\nhead_raddino, hist_raddino = treinar_cabeca(\n    emb_train_raddino, y_train, emb_val_raddino, y_val, in_features=768\n)\n\n# Plotar curvas de treino\nfig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))\nax1.plot(hist_raddino['loss'])\nax1.set_title('Loss')\nax1.set_xlabel('Época')\nax1.grid(True)\nax2.plot(hist_raddino['val_auc'], color='orange')\nax2.set_title('Val AUC')\nax2.set_xlabel('Época')\nax2.grid(True)\nplt.suptitle('RAD-DINO — Treino da Cabeça', fontweight='bold')\nplt.tight_layout()\nplt.show()\n\n# Avaliação\nresultados_raddino = avaliar(head_raddino, emb_test_raddino, y_test, 'RAD-DINO (Radiologia)')"],
        "id": "gabarito-pc4-code"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### 📊 Comparação de Resultados"],
        "id": "gabarito-pc5-title"
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": ["# GABARITO — Comparação de Resultados\n# Plotar comparação de métricas entre os dois modelos\nplotar_comparacao_metricas(resultados_effnet, resultados_raddino)"],
        "id": "gabarito-pc5-code"
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### 🔎 Inferência em Imagem Própria"],
        "id": "gabarito-pc6-title"
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": ["# GABARITO — Inferência em Imagem Própria\n# Permite fazer upload de imagem e inferência com ambos os modelos\n\ntry:\n    from google.colab import files\n    import io\n    \n    print('Faça upload de uma imagem de raio-X de tórax:')\n    uploaded = files.upload()\n    \n    for filename in uploaded.keys():\n        # Carregar imagem\n        img = Image.open(io.BytesIO(uploaded[filename]))\n        img = img.convert('RGB').resize((64, 64))\n        img_array = np.array(img).astype('float32') / 255.0\n        \n        # Inferência com EfficientNetB0\n        emb_eff = extrair_embeddings_cnn(extrator_effnet, img_array[np.newaxis, :])\n        with torch.no_grad():\n            prob_eff = head_effnet(torch.from_numpy(emb_eff).float().to(DEVICE)).item()\n        pred_eff = 'Pneumonia' if prob_eff > 0.5 else 'Normal'\n        \n        # Inferência com RAD-DINO\n        img_pil = Image.fromarray((img_array * 255).astype('uint8'))\n        emb_rad = extrair_embeddings_raddino(extrator_raddino, processor_raddino, [img_pil])\n        with torch.no_grad():\n            prob_rad = head_raddino(torch.from_numpy(emb_rad).float().to(DEVICE)).item()\n        pred_rad = 'Pneumonia' if prob_rad > 0.5 else 'Normal'\n        \n        # Visualizar resultados\n        fig, axes = plt.subplots(1, 3, figsize=(14, 4))\n        axes[0].imshow(img, cmap='gray')\n        axes[0].set_title('Imagem Original')\n        axes[0].axis('off')\n        \n        axes[1].bar(['Normal', 'Pneumonia'], [1-prob_eff, prob_eff], color=['blue', 'red'], alpha=0.7)\n        axes[1].set_title(f'EfficientNetB0: {pred_eff}')\n        axes[1].set_ylim([0, 1])\n        axes[1].set_ylabel('Probabilidade')\n        \n        axes[2].bar(['Normal', 'Pneumonia'], [1-prob_rad, prob_rad], color=['blue', 'red'], alpha=0.7)\n        axes[2].set_title(f'RAD-DINO: {pred_rad}')\n        axes[2].set_ylim([0, 1])\n        axes[2].set_ylabel('Probabilidade')\n        \n        plt.tight_layout()\n        plt.show()\n        \nexcept ImportError:\n    print('Função de upload disponível apenas no Google Colab')"],
        "id": "gabarito-pc6-code"
    }
]

# Adicionar ao final do notebook
nb['cells'].extend(new_cells)

# Salvar
with open('hands_on_spr_2026.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print('✅ Gabaritos PC4, PC5, PC6 adicionados!')
