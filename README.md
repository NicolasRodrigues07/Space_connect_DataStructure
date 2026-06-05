#  GS2026 — Monitoramento de Missão Espacial

Sistema de monitoramento de dados operacionais simulados de uma missão espacial, desenvolvido em **Python** como parte da atividade GS2026.1 — Programação Aplicada ao Monitoramento de Missão Espacial.

---

## Funcionalidades

- Cadastro de dados dos sensores (temperatura, energia, comunicação)
- Visualização do status operacional mais recente
- Análise automática com emissão de alertas
- Histórico completo de todas as leituras
- Interface de menu interativa no terminal com cores ANSI

---

## Condições de Alerta

| Temperatura > 80°C | 🔴 Superaquecimento detectado |
| Energia < 20% | 🟡 Energia crítica — modo de economia ativado |
| Comunicação = 0 | 🔴 Falha de comunicação com a base |

---

##  Estrutura do código

| Função | Responsabilidade |
=================================
| `menu_principal()` | Laço principal do sistema, mostra as opções do menu |
| `inserir_dados()` | Lê e valida os valores dos sensores, salva no histórico |
| `visualizar_status()` | Exibe a leitura mais recente |
| `executar_analise()` | Verifica as condições de alerta, emite notificações |
| `exibir_historico()` | Lista todas as leituras anteriores |
| `limpar_tela()` | Utilitário para limpar o terminal |

---

##  Lógica implementada

### Estrutura geral

O programa é organizado em **funções independentes**, cada uma responsável por uma ação do sistema. A função `menu_principal()` é o ponto de entrada e controla o fluxo com um laço `while True`, que mantém o programa rodando até que o usuário escolha a opção `[5] Encerrar`.

### Estruturas de dados

- **Lista (`historico`):** è um vetor global que armazena todas as leituras da sessão. Cada leitura é um **dicionário** com três chaves: `temperatura`, `energia` e `comunicacao`, simulando o registro de um sensor.
- A última leitura é sempre acessada via `historico[-1]` — o índice `-1` em Python retorna o último elemento de uma lista. é uma lógica que aprendemos durante as aulas de data structure.

### Lógica de alertas

Os três alertas são verificados com `if` **independentes** (não `elif`), permitindo que múltiplos alertas sejam disparados ao mesmo tempo. Um contador `alertas` acumula quantos foram ativados — se permanecer em `0` ao final, o sistema exibe a mensagem de operação normal.

```python
if ultima["temperatura"] > 80:   # alerta de superaquecimento
if ultima["energia"] < 20:       # alerta de energia crítica
if ultima["comunicacao"] == 0:   # alerta de falha de comunicação
```

### Tratamento de erros

A função `inserir_dados()` usa `try/except ValueError` para capturar entradas não numéricas e exibir uma mensagem de erro sem encerrar o programa.

### Terminal colorido

O sistema utiliza **códigos ANSI** para colorir as mensagens no terminal:

| Código | Cor | Uso |
|---|---|---|
| `\033[91m` | Vermelho | Alertas críticos |
| `\033[93m` | Amarelo | Avisos de atenção |
| `\033[92m` | Verde | Status normal / sucesso |

---

## 🔀 Fluxograma

```
[fluxograma.pdf](https://github.com/user-attachments/files/28647909/fluxograma.pdf)

```
---

## 👥 Integrantes do grupo

- Nicolas Andrade Rodrigues RM572782
- Lucas Caram
-
