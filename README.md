# projeto-concorrencia
projeto teste de contagem de palavras em múltiplos arquivos de texto.


# Projeto de Concorrência - Contagem de Palavras com Threads

## 📖 Sobre

Este projeto foi desenvolvido para a disciplina de Concorrência e Paralelismo.

O objetivo é realizar a contagem de palavras em múltiplos arquivos de texto utilizando **multithreading**, permitindo que vários arquivos sejam processados simultaneamente.

A solução demonstra conceitos fundamentais de:

* Concorrência
* Paralelismo
* Threads
* Sincronização
* Comunicação entre threads
* Tratamento de falhas
* Condição de corrida (Race Condition)

---

## Problema 

Dada uma pasta contendo vários arquivos de texto, o programa deve:

1. Ler todos os arquivos `.txt`.
2. Distribuir os arquivos entre múltiplas threads.
3. Contar a quantidade de palavras de cada arquivo.
4. Somar os resultados individuais.
5. Exibir o total geral de palavras encontradas.

---

## 🏗️ Estrutura

```text
ProjetoConcorrencia/
│
├── arquivos/
│   ├── texto1.txt
│   ├── texto2.txt
│   ├── texto3.txt
│
├── main.py
├── README.md
└── relatorio.pdf
```

---

## ⚙️ Tecnologias

* Python 3
* Threading
* Queue
* OS

Bibliotecas utilizadas:

```python
import threading
import queue
import os
```

---

## 🔄 Estratégia de Decomposição

O projeto utiliza **decomposição por dados**.

Cada thread recebe um arquivo diferente para processar.

Exemplo:

```text
Thread 1 → texto1.txt
Thread 2 → texto2.txt
Thread 3 → texto3.txt
```

Todas executam a mesma tarefa:

```text
Contar palavras
```

---

## 🧵 Concorrência e Paralelismo

### Concorrência

Múltiplas threads trabalham sobre diferentes arquivos ao mesmo tempo, compartilhando recursos do programa.

### Paralelismo

Em processadores com múltiplos núcleos, as threads podem ser executadas simultaneamente, reduzindo o tempo total de processamento.

---

## Comunicação Entre Threads

A comunicação é realizada através de uma fila compartilhada (`Queue`).

Os arquivos são inseridos na fila principal e consumidos pelas threads de trabalho.

```python
fila = queue.Queue()
```

Essa abordagem evita conflitos na distribuição das tarefas.

---

## Sincronização

O total geral de palavras é armazenado em uma variável compartilhada:

```python
total_palavras = 0
```

Como várias threads podem acessar essa variável simultaneamente, existe o risco de uma **condição de corrida (Race Condition)**.

Para evitar esse problema foi utilizado um mecanismo de exclusão mútua:

```python
lock = threading.Lock()
```

Trecho protegido:

```python
with lock:
    total_palavras += qtd
```

Dessa forma apenas uma thread altera o total por vez.

---

## Tratamento de Falhas

O programa trata falhas relacionadas à leitura dos arquivos.

Exemplos:

* Arquivo inexistente
* Arquivo corrompido
* Permissão negada

As exceções são capturadas e registradas sem interromper o processamento das demais tarefas.

```python
try:
    ...
except Exception as e:
    ...
```

Isso garante que o processamento continue mesmo quando ocorre algum erro.

---

## Padrão Utilizado

A solução segue uma abordagem semelhante ao padrão **MapReduce**.

### Map

Cada thread processa um arquivo individualmente.

### Reduce

Os resultados são agregados em uma variável compartilhada contendo o total de palavras.

---

##  Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/ryamback001/ProjetoConcorrencia.git
```

### 2. Entrar na pasta

```bash
cd ProjetoConcorrencia
```

### 3. Adicionar arquivos de texto

Coloque os arquivos `.txt` dentro da pasta:

```text
arquivos/
```

### 4. Executar o programa

```bash
python main.py
```

---

## 📊 Exemplo de Saída

```text
arquivos/texto1.txt: 250 palavras
arquivos/texto2.txt: 180 palavras
arquivos/texto3.txt: 320 palavras

===== RESULTADO =====
Total de palavras: 750
```

---

## 👨‍💻 Autor

Rian Almeida 2306852


