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
├── hands_on_spr_2026.ipynb   # Notebook Colab (PC0–PC2 pré-preenchidos; PC3–PC6 via Gemini)
├── prompts.md                # Prompt Cards PC3–PC6 para projetar durante o workshop
├── exemplo_1.jpg                # Imagem de RX de tórax para demo de inferência
├── exemplo_2.jpg    # Imagem de RX de tórax para demo de inferência
├── README.md                 # Este arquivo
└── .gitignore
```

---

## 🗂️ Prompt Cards (PC0–PC6)

| # | Bloco | Conteúdo |
|---|---|---|
| PC0 | Setup e Preparação | **Pré-preenchido** — instala libs, define SEED=42, funções auxiliares |
| PC1 | Carregar o Dataset | **Pré-preenchido** — PneumoniaMNIST 1000 imagens, subsample 800/100/100 |
| PC2 | Embeddings + t-SNE | **Pré-preenchido** — extrai features dos dois modelos + visualização t-SNE |
| PC3 | Classificador 1 | **Gemini** — treinar cabeça sobre EfficientNetB0, métricas + matriz |
| PC4 | Classificador 2 | **Gemini** — treinar cabeça sobre RAD-DINO (mesmos hiperparâmetros) |
| PC5 | Comparação | **Gemini** — gráfico de barras + tabela de diferenças |
| PC6 | Inferência Própria | **Gemini** — upload de RX → predição dos dois modelos lado a lado |

---

## 🚀 Como Usar

### Abrir no Colab

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AugustoSSerpa/hands_on_spr_2026/blob/main/hands_on_spr_2026.ipynb)

> Ou acesse: `https://colab.research.google.com/github/AugustoSSerpa/hands_on_spr_2026/blob/main/hands_on_spr_2026.ipynb`

### Fluxo do Participante

1. Abra o notebook no Colab com GPU T4 (Runtime → Change runtime type → T4 GPU)
2. **PC0, PC1, PC2** — execute as células diretamente (código pré-preenchido)
3. **PC3 a PC6** — para cada bloco:
   - Leia o **Prompt Card** projetado pelo instrutor
   - Cole no **Gemini** (sidebar do Colab: ícone ✦ ou `Ctrl+Shift+I`)
   - Cole o código gerado na célula vazia e execute
4. No PC6, use `exemplo_1.jpg` ou `exemplo_2.jpg` disponíveis no repositório, ou seu próprio RX

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

---
---
# 💬 Discussão Clínica

## O que aconteceu?

Ambos os backbones ficaram **completamente congelados** durante o experimento. Apenas a cabeça classificadora foi treinada — e era idêntica para os dois:

| | EfficientNetB0 | RAD-DINO |
|---|---|---|
| **Pré-treinamento** | ImageNet (1,28M fotos naturais) | 880K+ RX de tórax (MIMIC, CheXpert, NIH, PadChest, BRAX) |
| **Arquitetura** | CNN (EfficientNet) | ViT-B/14 com DINOv2 |
| **Dim. embedding** | 1.280 | 768 |
| **Parâmetros treinados** | ~262K (só head) | ~262K (só head) |
| **Tamanho do modelo** | ~21MB | ~87MB |

## Perguntas para reflexão

**1. Por que o t-SNE do RAD-DINO mostra clusters mais separados?**
> Os embeddings do RAD-DINO já codificam padrões clínicos radiológicos (opacidades, consolidações, textura pulmonar anormal). O EfficientNetB0 ImageNet codifica bordas e texturas de imagens naturais — parcialmente útil, mas sem especificidade clínica.

**2. Por que treinamos APENAS a cabeça (feature extraction)?**
> Fine-tuning completo com 5.856 imagens em um backbone de 86M+ parâmetros causaria overfitting severo. Feature extraction é a abordagem padrão quando o dataset clínico é pequeno.

**3. O RAD-DINO foi treinado em pneumonia especificamente?**
> Não. Foi treinado de forma auto-supervisionada (DINOv2) em raios-X gerais — sem labels de diagnóstico. A separação que vemos vem do conhecimento geral de radiologia de tórax aprendido de forma não-supervisionada.

**4. Isso é suficiente para uso clínico real?**
> Não. Imagens 64×64 perdem detalhes diagnósticos críticos. O dataset tem viés geográfico (crianças de Guangzhou). Sem validação prospectiva nem aprovação regulatória. Este é um experimento educacional para demonstrar o princípio da **transferência de domínio**.

**5. Qual é a implicação prática para radiologia?**
> Ao escolher um modelo pré-treinado para fine-tuning em uma tarefa radiológica, modelos treinados em dados clínicos radiológicos tendem a superar modelos de propósito geral — mesmo quando apenas a cabeça é treinada.

---

## Referências

- **PneumoniaMNIST:** Kermany DS et al., *Cell*, 2018. doi: 10.1016/j.cell.2018.02.010
- **RAD-DINO:** Pérez-García F et al., *Nature Machine Intelligence*, 2025. doi: 10.1038/s42256-024-00965-w
- **DINOv2:** Oquab M et al., *TMLR*, 2024. arXiv: 2304.07193
- **MedMNIST v2:** Yang J et al., *Scientific Data*, 2023. doi: 10.1038/s41597-022-01721-8
- **EfficientNet:** Tan M, Le QV, *ICML*, 2019. arXiv: 1905.11946

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

