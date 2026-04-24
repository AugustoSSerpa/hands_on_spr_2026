# 📋 Prompt Card — Assistente de Laudos com IA
## Hands-on Vibe Coding · SPR 2026
### Imprimir uma folha por participante (ou projetar no telão)

---

## ⚠️ Antes de começar

1. Acesse **aistudio.google.com** → "Get API key" → "Create API key" → copie a chave
2. No Colab: ícone 🔑 **Secrets** na barra lateral → "+ Novo secret" → nome: `GEMINI_API_KEY` → cole a chave → ative o toggle
3. Execute as células pré-preenchidas de instalação e configuração

---

## Prompt 1 — App Básico (Bloco 2)

> Usando Python com as bibliotecas `gradio` e `google.generativeai` (já importadas) e a variável `modelo` (já configurada com gemini-1.5-flash), crie uma interface web simples de assistente de laudos radiológicos. A interface deve ter: (1) uma caixa de texto grande para o médico digitar os achados em texto livre, com placeholder de exemplo; (2) um botão "Gerar Laudo"; (3) uma área de saída mostrando o laudo. O prompt para o Gemini deve instruí-lo a agir como radiologista experiente e estruturar o laudo com três seções em Markdown: ACHADOS (organizados), DIAGNÓSTICOS DIFERENCIAIS (3-5 hipóteses com probabilidade em %), IMPRESSÃO DIAGNÓSTICA (conclusão objetiva). Use `gr.Interface` simples. No final use `app.launch(share=True)` para gerar um link público.

**Resultado esperado:** URL pública tipo `https://xxxx.gradio.live` — app no ar!

---

## Prompt 2 — Modalidade e Região (Bloco 3, iteração 1)

> Reescreva o assistente de laudos com estas melhorias: (1) adicione um dropdown "Modalidade" com as opções: Raio-X, Tomografia Computadorizada, Ressonância Magnética, Ultrassonografia, Mamografia, PET-CT; (2) adicione um dropdown "Região Anatômica" com: Tórax, Abdome, Encéfalo, Coluna Vertebral, Mama, Musculoesquelético, Pelve, Pescoço; (3) passe modalidade e região para o prompt do Gemini para que o laudo inclua também a técnica padrão do exame e a seção "Conduta Sugerida"; (4) mostre a saída como Markdown formatado usando `gr.Markdown` ao invés de Textbox. Mantenha o `app.launch(share=True)` no final.

---

## Prompt 3 — Layout em Duas Colunas (Bloco 3, iteração 2)

> Refatore o app anterior para usar `gr.Blocks` com layout em duas colunas: coluna esquerda (campos de entrada: modalidade, região, caixa de achados e botão "📝 Gerar Laudo"), coluna direita (laudo em Markdown). Adicione no topo um título estilizado com `gr.Markdown` incluindo o nome do seu serviço/hospital. Adicione também um tema visual com `gr.themes.Soft()`. Mantenha o `app.launch(share=True)` no final.

---

## Prompt 4 — Alerta de Achados Críticos (Bloco 3, iteração 3)

> Adicione ao app uma segunda funcionalidade: um botão "⚠️ Verificar Achados Críticos" que envia os mesmos achados ao Gemini com o seguinte prompt específico: "Você é um radiologista. Analise estes achados de [modalidade] de [região]: [achados]. Existem achados críticos que requerem comunicação imediata (emergência radiológica)? Se SIM: liste em ordem de prioridade começando com '⚠️ ACHADOS CRÍTICOS:' e indique a ação urgente. Se NÃO: responda apenas '✅ Sem achados críticos. Comunicação de rotina adequada.' Seja direto e objetivo." Mostre o resultado abaixo do laudo principal em uma caixa separada com label "Verificação de Achados Críticos". Mantenha o botão de gerar laudo funcionando. Mantenha o `app.launch(share=True)`.

---

## Prompt 5 — Especialização (Bloco 4)

**TC de Tórax:**
> Modifique o prompt do Gemini para especializar o assistente em TC de Tórax. O laudo deve avaliar sistematicamente: parênquima pulmonar (densidade, distribuição, padrão — vidro fosco, consolidação, nódulos), estruturas vasculares (calibre da aorta e artéria pulmonar), mediastino, pleura e parede torácica. Se houver nódulos, mencione critérios de Lung-RADS. Se houver achados vasculares, mencione TEP no diferencial quando pertinente. Ajuste os dropdowns para TC de Tórax.

**RM de Encéfalo:**
> Modifique o prompt do Gemini para especializar em RM de Encéfalo. O laudo deve avaliar: parênquima (sinal em T1/T2/FLAIR, restrição à difusão, realce pelo contraste), ventrículos e espaços subaracnóideos, fossa posterior, vascular. No diferencial de lesões encefálicas, sempre considere: neoplasia primária, metástase, desmielinizante, infecciosa e vascular.

**Mamografia / US de Mama:**
> Modifique o prompt para especializar em Mamografia e Ultrassom de Mama. O laudo deve descrever: densidade mamária (A, B, C ou D do BI-RADS), achados (calcificações, nódulos, assimetrias, distorções), e concluir com a categoria BI-RADS (0 a 6) com a recomendação de conduta padrão.

---

## 🔧 Prompts de Correção (se o Gemini errar)

| Situação | O que pedir ao Gemini |
|---|---|
| Erro de import | "O código deu ImportError. Corrija sem mudar a lógica." |
| App não abre no browser | "O app.launch não gerou link público. Certifique-se de usar `share=True`." |
| Erro de API key | "Deu erro de autenticação. O código deve usar a variável `GEMINI_API_KEY` já definida." |
| Layout quebrado | "O layout ficou sobreposto. Use `gr.Row()` e `gr.Column()` corretamente para separar entrada e saída." |
| Gemini não responde | "Adicione tratamento de erro com try/except em volta do `modelo.generate_content()` e mostre a mensagem de erro ao usuário." |

---

## 📊 Referências rápidas

| Item | Detalhe |
|---|---|
| Modelo recomendado | `gemini-1.5-flash` (rápido, gratuito) |
| Cota gratuita | 15 req/min, 1.500 req/dia |
| Modelo mais capaz | `gemini-1.5-pro` (mais lento, mesma cota) |
| Link AI Studio | aistudio.google.com |
| Docs Gradio | gradio.app/docs |

---

## 🔗 Links do evento

- **Notebook Colab:** *(encurtar com bit.ly antes do evento)*
- **AI Studio:** https://aistudio.google.com
