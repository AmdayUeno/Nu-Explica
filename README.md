# 💜 Nu Explica

Um agente de IA que ensina investimentos do zero, sem jargão, uma etapa de cada vez, e chama uma pessoa de verdade quando você pede.

Protótipo feito em **Agentforce** (Salesforce) para o desafio **AI Builder Interns**, explorando não só a construção de um agente, mas também decisões de produto, segurança e uso responsável de inteligência artificial.

> Protótipo de demonstração, **não oficial e sem vínculo com o Nubank**. O conteúdo é educativo e não constitui recomendação de investimento. Todos os valores e a persona são fictícios.

## 🔗 Experimente o Agente

**[Abrir o Nu Explica](https://orgfarm-821eaec6c3-dev-ed.develop.my.site.com/nuexplica/)**

Clique no botão de chat no canto da página para conversar com o agente.  
Não envie dados reais (CPF, senhas, saldos).

## Ideia do Projeto

Quem nunca investiu esbarra em três barreiras:

* **Jargão:** CDI, liquidez e renda fixa aparecem antes de qualquer explicação
* **Ordem:** a pessoa não sabe que a reserva de emergência vem antes de qualquer aplicação
* **Confiança:** promessas como "rende 5% ao mês, garantido" circulam e confundem

A proposta foi ir além de um FAQ.  
O Nu Explica conversa no ritmo da pessoa, ensina com exemplos do dia a dia e protege quando a situação pede (golpe, roubo, endividamento, crise).

Ele foi pensado a partir da **Júlia**, persona fictícia de 26 anos, assistente administrativa, que sobra uns R$ 300 por mês e travou em "100% do CDI".  
Frase dela: *"Só queria saber por onde começar sem me sentir burra."*

## O que o Nu Explica faz

* Trilha de **7 etapas**, com uma ideia por mensagem
* Respostas ancoradas numa **base de conhecimento aprovada** (PDF na Data Library)
* **Triagem educativa** calculada por um Flow, nunca pela IA
* **Proteção** em golpe, roubo, dívida e situações de crise
* **Transbordo** para uma pessoa do time quando a pessoa pede

### O que ele não faz

* Recomendar produto de investimento (isso é *suitability*, atividade regulada pela Resolução CVM 30)
* Informar taxas ou dados reais em tempo real
* Operar a conta ou aplicar dinheiro
* Resolver fatura e fraude, que seguem pelos canais oficiais

## IA no Desenvolvimento

A IA foi usada como aliada em várias frentes:

* Pesquisa e construção do agente, com apoio do **Claude** e das skills públicas `sf-skills` da Salesforce
* Escrita e revisão do prompt, das regras de segurança e da base de conhecimento
* Criação de roteiros de teste e análise dos resultados
* Revisão de decisões do próprio projeto

Uma decisão que revisei no caminho: pedi uma triagem que indicasse o melhor investimento para cada perfil.  
Revisando, percebi que isso é recomendação.  
Mudei o desenho: o perfil é explicado só por características (liquidez, oscilação, prazo), com aviso de que não é recomendação, e a conta é feita por um **Flow**, não pela IA.

## Tecnologias

* Salesforce Developer Edition (gratuita)
* Agentforce com **Agent Script**
* Data Library (base de conhecimento em PDF)
* Flow (triagem e roteamento)
* Omni-Channel e Service Console (atendimento humano)
* Experience Cloud (site público com chat)
* Lightning Web Components (página inicial)
* Salesforce CLI (`sf`) e Salesforce DX (API 68.0)
* Python (script que gera o PDF da base)

## Identidade Visual

* Roxo como cor principal (`#820AD1`), com tema claro e escuro
* Tipografia **DM Sans**
* Interface de chat simples, com respostas rápidas ("Começar pelo básico", "O que é CDI?")
* Avisos claros de que é um protótipo educativo, em todas as telas

## Experiência

* Página inicial com chat integrado e temas para começar: renda fixa, CDI, Tesouro Direto, reserva de emergência, risco e liquidez, fundos
* Uma ideia por mensagem, com no máximo uma pergunta por vez
* Layout pensado para o celular
* Transbordo simples: basta escrever *"quero falar com um atendente"* e a conversa continua com alguém do time, que já vê o que foi conversado

## Testes e Resultados

Foram registradas cerca de **30 conversas de teste**, em preview e no site público:

* **5 de 5** casos do Flow de triagem corretos
* **3 de 3** frases de crise encaminhadas à proteção, após ajuste
* Mensagens com duas perguntas: de **3/10** para **0/6**

> Amostras pequenas: evidência de comportamento, não prova estatística.

### Metas (hipóteses de piloto)

| Meta | O que medir | Hipótese |
| --- | --- | --- |
| CSAT | Nota de 1 a 5 ao fim da conversa | Média ≥ 4,0 |
| NPS | Piloto × grupo controle, 60 dias | +5 pontos |
| Retenção | Clientes ativos após 90 dias | +2 p.p. |
| Apoio | % resolvidas sem transbordo | Definir no piloto |

Todas as metas são hipóteses: nenhuma melhoria foi comprovada.

## Como funciona

```
Site (Experience Cloud) → Widget de chat → Canal de mensagens → Agente Nu Explica
                                                                      │
        ┌───────────────────┬─────────────────────┬───────────────────┤
        ▼                   ▼                     ▼                   ▼
  trilha_investimentos   protecao        fora_do_escopo        transbordo
  (entrada e trilha)  (golpe, crise)    (recusa gentil)    (fila humana via Omni-Channel)
        │
        ├── Base de conhecimento (Data Library)
        └── Flow calcular_perfil (triagem)
```

## Estrutura do Repositório

```
Documentos/          Base de conhecimento (PDF), roteiros de teste e de demonstração
Projeto/nu-explica/  Projeto Salesforce DX completo, pronto para deploy
V1/ V2/ V3/          Prints dos testes de cada versão
```

Dentro de `Projeto/nu-explica/`:

| Pasta | O que é |
| --- | --- |
| `force-app/.../aiAuthoringBundles/Nu_Explica/` | O agente (rascunho atual, editável) |
| `force-app/.../aiAuthoringBundles/Nu_Explica_1/` | Versão 1 publicada (somente leitura) |
| `force-app/.../flows/Nu_Explica_Calcular_Perfil.flow-meta.xml` | Flow que calcula o perfil da triagem |
| `data-library/` | PDF da base de conhecimento e o script que o gera |
| `backup/` | Agente original, antes das mudanças |
| `scripts-de-teste/` | Scripts de preview e o teste do Flow em Apex |

## Como Rodar

**Pré-requisitos:** [Salesforce CLI](https://developer.salesforce.com/tools/salesforcecli) com comandos `sf agent`, e uma org com Agentforce e Data Cloud habilitados.

```bash
cd Projeto/nu-explica
sf org login web --alias minha-org --set-default

# Validar o agente
sf agent validate authoring-bundle --api-name Nu_Explica -o minha-org --json

# Deploy do agente e do Flow
sf project deploy start -m "AiAuthoringBundle:Nu_Explica" -m "Flow:Nu_Explica_Calcular_Perfil" -o minha-org --json

# Publicar o agente
sf agent publish authoring-bundle --api-name Nu_Explica -o minha-org --json
```
## Próximos Passos

* Botões de tema da página abrindo o chat já no assunto certo
* Widget de chat totalmente em português
* Rota para quando nenhum atendente estiver online
* Gravar a nota de satisfação (CSAT) de cada conversa
* Bateria de testes automática a cada versão

## Aprendizados

* Segurança vem em camadas: regra no prompt, base aprovada, estrutura do agente, cálculo fora da IA e filtros da plataforma
* O que não pode dar errado deve virar **estrutura**, não apenas instrução em texto
* Educar não é recomendar, e essa fronteira precisa estar desenhada desde o início
* Testar com poucas conversas ajuda a ajustar, mas não prova que o agente acerta sempre

## Autora

Amanda Ueno · https://www.linkedin.com/in/amanda-ueno/
