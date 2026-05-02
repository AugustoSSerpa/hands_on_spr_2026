# 🩻 Foundation Models para Radiologia — Hands-on SPR 2026

Workshop prático de **vibe coding** com Gemini para radiologistas: construa do zero um experimento de deep learning comparando um modelo genérico (ImageNet) vs. um modelo especializado em radiologia (RAD-DINO) — sem programar, sem instalar nada.

---

## 🎯 O Experimento

**Pergunta central:** Modelos pré-treinados em dados radiológicos extraem representações melhores de raios-X do que modelos treinados em fotos genéricas?

**Abordagem — Feature Extraction:**
- Os dois backbones ficam **completamente congelados**
- Apenas uma cabeça classificadora linear é treinada em cima dos embeddings
- Isso isola a qualidade das representações, independente do treinamento

| | EfficientNetB0 | RAD-DINO |
|---|---|---|
| **Pré-treinamento** | ImageNet (1,28M fotos naturais) | 880K+ RX de tórax (MIMIC, CheXpert, NIH, PadChest, BRAX) |
| **Arquitetura** | CNN | ViT-B/14 (DINOv2) |
| **Dim. embedding** | 1.280 | 768 |
| **Tamanho** | ~21 MB | ~87 MB |

**Dataset:** PneumoniaMNIST — 1.000 imagens, 64×64px, split 800/100/100 (treino/val/teste), `SEED=42`

---

## 💡 Conceito: Vibe Coding

> **Você descreve em português o que quer que o código faça. O Gemini escreve. Você executa.**

Os participantes nunca editam código manualmente. Para cada bloco do notebook há um **Prompt Card** com a instrução em linguagem natural — basta colar no Gemini e executar o código gerado.

---

## 📂 Estrutura do Projeto

```
hands_on_spr_2026/
├── hands_on_spr_2026.ipynb   # Notebook Colab (100% prompt-driven, sem código pré-preenchido)
├── prompts.md                # Todos os Prompt Cards (PC0–PC6) para o instrutor
├── exemplo_1.jpg                # Imagem de RX de tórax para demo de inferência
├── exemplo_2.jpg    # Imagem de RX de tórax para demo de inferência
├── README.md                 # Este arquivo
└── .gitignore
```

---

## 🗂️ Prompt Cards (PC0–PC6)

| # | Bloco | Conteúdo |
|---|---|---|
| PC0 | Setup e Preparação | Instalar libs, SEED=42, funções auxiliares, configurar GPU |
| PC1 | Carregar o Dataset | PneumoniaMNIST 1000 imagens, subsample 800/100/100, visualizar |
| PC2 | Embeddings + t-SNE | Extrair features dos dois modelos, visualizar separação com t-SNE |
| PC3 | Classificador 1 | Treinar cabeça sobre EfficientNetB0, métricas + matriz de confusão |
| PC4 | Classificador 2 | Treinar cabeça sobre RAD-DINO (mesmos hiperparâmetros) |
| PC5 | Comparação | Gráfico de barras + tabela de diferenças entre os dois modelos |
| PC6 | Inferência Própria | Upload de RX do participante → predição dos dois modelos lado a lado |

---

## 🚀 Como Usar

### Abrir no Colab

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AugustoSSerpa/hands_on_spr_2026/blob/main/hands_on_spr_2026.ipynb)

> Ou acesse: `https://colab.research.google.com/github/AugustoSSerpa/hands_on_spr_2026/blob/main/hands_on_spr_2026.ipynb`

### Fluxo do Participante

1. Abra o notebook no Colab com GPU T4 (Runtime → Change runtime type → T4 GPU)
2. Para cada bloco vazio:
   - Leia o **Prompt Card** projetado pelo instrutor (ou em `prompts.md`)
   - Cole no **Gemini** (sidebar do Colab: ícone ✦ ou `Ctrl+Shift+I`)
   - Cole o código gerado na célula e execute
3. Ao chegar no PC6, use a imagem `m2400651-pneumonia.jpg` ou seu próprio RX

### Para Instrutores

- Projete os Prompt Cards um por vez (arquivo `prompts.md`)
- O gabarito completo está nas últimas células do notebook (seção GABARITO)
- Tempo estimado total: **75 minutos**

---

## 📊 Cronograma (75 min)

| Bloco | Conteúdo | Tempo |
|---|---|---|
| PC0 | Setup, libs, funções | 10 min |
| PC1 | Dataset + visualização | 10 min |
| PC2 | Embeddings + t-SNE | 15 min |
| PC3 | Classificador EfficientNetB0 | 10 min |
| PC4 | Classificador RAD-DINO | 10 min |
| PC5 | Comparação de resultados | 5 min |
| PC6 | Inferência em imagem própria | 5 min |
| — | Discussão clínica | 10 min |

---

## 🔧 Stack Técnica

- **Ambiente:** Google Colab T4 GPU (gratuito)
- **Modelos:** `torchvision` (EfficientNetB0) · `microsoft/rad-dino` (HuggingFace)
- **Dados:** `medmnist` (PneumoniaMNIST)
- **ML:** `torch` · `sklearn` · `matplotlib`
- **Sem instalação local** — tudo roda no browser

---

## ⚠️ Limitações

| Limitação | Implicação |
|---|---|
| Imagens 64×64 px | Resolução muito abaixo do padrão clínico — perda de detalhes diagnósticos |
| Dataset pequeno (1.000 imgs) | Viés geográfico (crianças de Guangzhou, China) |
| Backbone congelado | Não é fine-tuning completo — experimento educacional |
| Sem validação prospectiva | **Protótipo educacional**, não dispositivo médico |
| Inferência PC6 | Demonstrativa apenas — sem validade clínica |

---

## 📖 Referências

- **RAD-DINO:** Pérez-García F et al., *Nature Machine Intelligence*, 2025. [doi:10.1038/s42256-024-00965-w](https://doi.org/10.1038/s42256-024-00965-w)
- **PneumoniaMNIST / MedMNIST v2:** Yang J et al., *Scientific Data*, 2023. [doi:10.1038/s41597-022-01721-8](https://doi.org/10.1038/s41597-022-01721-8)
- **DINOv2:** Oquab M et al., *TMLR*, 2024. [arXiv:2304.07193](https://arxiv.org/abs/2304.07193)
- **EfficientNet:** Tan M, Le QV, *ICML*, 2019. [arXiv:1905.11946](https://arxiv.org/abs/1905.11946)
- **Kermany Dataset original:** Kermany DS et al., *Cell*, 2018. [doi:10.1016/j.cell.2018.02.010](https://doi.org/10.1016/j.cell.2018.02.010)

---

## 👥 Autoria

Desenvolvido por Augusto Sarquis Serpa para a **Jornada Paulista de Radiologia — JPR 2026**  
Formato: Hands-on Vibe Coding com Inteligência Artificial

---

## 📝 Licença

Material educacional. Livre para adaptar, remixar e compartilhar — cite a origem.

---

**Dúvidas?** Pergunte durante a sessão ou mande um e-mail para augusto.esd5@gmail.com.

---

