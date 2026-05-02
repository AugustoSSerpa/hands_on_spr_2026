import json

# Ler o notebook
with open('hands_on_spr_2026.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Atualizar cronograma no header (célula 0)
cronograma_novo = """### ⏱️ Cronograma (75 minutos)

| | Bloco | Tempo |
|---|---|---|
| 🔧 | Setup e Preparação | 8 min |
| 📦 | Carregar e Visualizar o Dataset | 7 min |
| 🎬 | Extração de Embeddings + t-SNE | 12 min |
| 🏗️ | Classificador 1: EfficientNetB0 (ImageNet) | 12 min |
| 🏗️ | Classificador 2: RAD-DINO (Radiologia) | 12 min |
| 📊 | Comparação de Resultados | 8 min |
| 🔎 | Inferência em Imagem Própria | 10 min |
| 💬 | Discussão Clínica | 6 min |"""

# Encontrar e substituir o cronograma no markdown do header
header_content = ''.join(nb['cells'][0]['source'])
header_content = header_content.replace(
    "### ⏱️ Cronograma (60 minutos)\n\n| | Bloco | Tempo |\n|---|---|---|\n| 🔧 | Setup + Funções (PC0) | 8 min |\n| 📦 | Dataset (PC1) | 7 min |\n| 🏗️ | Extrator 1: EfficientNetB0 (PC2) | 12 min |\n| 🏗️ | Extrator 2: RAD-DINO (PC3) | 12 min |\n| 📊 | t-SNE + Comparação de métricas (PC4) | 8 min |\n| 🔬 | Bônus — Inferência em imagem própria | 8 min |\n| 💬 | Discussão clínica | 5 min |",
    cronograma_novo
)

nb['cells'][0]['source'] = [header_content]

# Adicionar títulos ANTES de cada código cell
titles = [
    "## 🔧 Setup e Preparação\n\n✦ Cole aqui o código gerado pelo Gemini",
    "## 📦 Carregar e Visualizar o Dataset\n\n✦ Cole aqui o código gerado pelo Gemini",
    "## 🎬 Extração de Embeddings + t-SNE\n\n✦ Cole aqui o código gerado pelo Gemini",
    "## 🏗️ Classificador 1: EfficientNetB0 (ImageNet)\n\n✦ Cole aqui o código gerado pelo Gemini",
    "## 🏗️ Classificador 2: RAD-DINO (Radiologia)\n\n✦ Cole aqui o código gerado pelo Gemini",
    "## 📊 Comparação de Resultados\n\n✦ Cole aqui o código gerado pelo Gemini",
    "## 🔎 Inferência em Imagem Própria\n\n✦ Cole aqui o código gerado pelo Gemini"
]

# Inserir markdown cells com títulos ANTES de cada code cell (de trás pra frente)
for i in range(len(titles)-1, -1, -1):
    title_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [titles[i]],
        "id": f"title-{i}"
    }
    # Inserir ANTES da célula de código (na posição i+1, porque célula 0 é o header)
    nb['cells'].insert(i+1, title_cell)

# Salvar
with open('hands_on_spr_2026.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print('✅ Cronograma e títulos atualizados!')
