# 🏥 Assistente de Laudos com IA — Hands-on SPR 2026

Um workshop prático de **vibe coding** com Gemini para radiologistas construirem um assistente inteligente de estruturação de laudos — **sem programar, sem instalar nada**.

---

## 📋 Sobre o Hands-on

**Objetivo:** Cada participante sai com um app funcional rodando no browser, construído com Gemini (gratuito) + Google Colab.

**O que vão aprender:**
- Vibe coding: descrever em português, a IA escreve o código
- Chamar a API do Gemini em Python
- Construir UIs web com Gradio em minutos
- Iterar sobre uma ideia clínica via prompts

**Duração:** 90 minutos  
**Requisitos:** Conta Google + Browser atualizado

---

## 📂 Estrutura do Projeto

```
hands_on_spr_2026/
├── hands_on_spr_2026.ipynb       # Notebook Colab completo (5 blocos)
├── prompt_card_instrutor.md      # Prompts prontos para imprimir/projetar
├── README.md                     # Este arquivo
└── .gitignore                    # Arquivos ignorados pelo git
```

---

## 🚀 Como Usar

### Para Participantes

1. Abra o link do Colab (será encurtado com bit.ly):
   ```
   https://colab.research.google.com/github/[seu-usuario]/hands_on_spr_2026/blob/main/hands_on_spr_2026.ipynb
   ```

2. Siga as instruções do **Bloco 1 — Setup:**
   - Crie uma API Key gratuita em [aistudio.google.com](https://aistudio.google.com)
   - Salve no Secrets do Colab

3. Para cada célula de código vazia:
   - Copie o **Prompt Card** da célula anterior (em Markdown)
   - Cole no **Gemini** (ícone ✦ ou `Ctrl+Shift+I`)
   - Cole o código gerado na célula vazia
   - Execute

4. Personalize o app na seção **Bloco 4 — Personalização Livre**

### Para Instrutores

- **Antes do evento:**
  - Teste o notebook no Colab (sem API key é só estrutura)
  - Encurte o link com bit.ly
  - Imprima o `prompt_card_instrutor.md` (1 cópia por mesa)

- **Durante o evento:**
  - Mostre ao vivo a Célula 1 (você copiam e colam)
  - Deixe livre para o Bloco 3-4
  - Recolha 2-3 apps nos últimos 10 min para demo

---

## 📊 Cronograma

| Bloco | Conteúdo | Tempo |
|---|---|---|
| 1 | Setup + instalação + teste Gemini | 15 min |
| 2 | Primeiro prompt → app no ar | 20 min |
| 3 | 3 iterações guiadas (dropdowns → layout → alerta crítico) | 30 min |
| 4 | Personalização para sua subespecialidade | 15 min |
| 5 | Demo + discussão clínica (limitações, LGPD, uso real) | 10 min |

---

## 💡 Conceito: Vibe Coding

> **Você descreve em português o que quer que o código faça. O Gemini escreve. Você executa.**

Regra de ouro: você nunca edita o código manualmente. Se algo não ficou como queria, descreva o problema ao Gemini em linguagem natural.

**Benefício:** radiologistas sem experiência em programação conseguem prototipar ideias clínicas em tempo real.

---

## 🔧 Requisitos Técnicos

- **Python:** 3.8+ (pré-instalado no Colab)
- **Bibliotecas:**
  - `google-generativeai` — SDK para Gemini
  - `gradio` — Framework web
- **Conta:** Google (gratuita)
- **API Gemini:** Gratuita (15 req/min, 1.500 req/dia)

---

## 📚 Especialidades Cobertas (Prompt Card 5)

- 🫁 **TC de Tórax** — Protocolos Lung-RADS, TEP
- 🧠 **RM de Encéfalo** — Classificação de lesões, fossa posterior
- 👩‍⚕️ **Mamografia / US de Mama** — BI-RADS 0-6
- ⭐ **Template livre** — Customize para sua especialidade

---

## ⚠️ Limitações (Discussão Clínica)

| Limitação | Implicação |
|---|---|
| O Gemini não vê a imagem | Ele estrutura o que você descreve — raciocínio clínico é seu |
| Alucinação LLM | Diagnósticos diferenciais podem ser plausíveis mas errados → sempre revise |
| Sem validação clínica | **Protótipo educacional**, não dispositivo médico |
| LGPD / HIPAA | Não use dados reais de pacientes em APIs externas |
| Latência | Depende de conexão + cota gratuita (15 req/min) |

---

## 🏆 Resultado Esperado

Após 90 minutos, cada participante terá:

✅ Um app web rodando no browser (`gradio.live`)  
✅ Capaz de estruturar laudos em texto livre  
✅ Com seleção de modalidade + região anatômica  
✅ Com verificação automática de achados críticos  
✅ Especializado para sua subespecialidade  
✅ Pronto para experimentação local (pode baixar o `.ipynb` e rodar offline)

---

## 📖 Referências

- **MedMNIST Paper** (conceito anterior): https://doi.org/10.1038/s41597-022-01721-8
- **Google AI Studio:** https://aistudio.google.com
- **Gradio Docs:** https://gradio.app/docs
- **Google Generative AI Docs:** https://ai.google.dev/

---

## 👥 Autoria

Desenvolvido para a **Sociedade Paulista de Radiologia — 2026**  
Formato: Hands-on Vibe Coding com Inteligência Artificial

---

## 📝 Licença

Este material é fornecido para fins educacionais.  
Sinta-se livre para adaptar, remixar e compartilhar — cite a origem.

---

**Dúvidas?** Deixe uma issue neste repositório ou fale após a sessão.
