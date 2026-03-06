
# Sistema de Perguntas e Respostas com TF-IDF

Este projeto implementa um **mini sistema de perguntas e respostas** utilizando técnicas de **Processamento de Linguagem Natural (PLN)** com **TF-IDF** e **similaridade de cosseno**.  

O objetivo é permitir que o usuário faça perguntas e receba respostas previamente cadastradas no banco de dados, com base na similaridade textual.

---

##  Estrutura do Código

### Classes
- **Pergunta**
  - Representa uma pergunta cadastrada.
  - Atributos: `id`, `texto`.

- **Resposta**
  - Representa uma resposta vinculada a uma pergunta.
  - Atributos: `id`, `texto`, `pergunta_id`.

- **BancoDeDadosQA**
  - Armazena listas de perguntas e respostas.
  - Métodos principais:
    - `adicionar_pergunta(pergunta)`
    - `adicionar_resposta(resposta)`
    - `encontrar_resposta(pergunta_texto)`

---

##  Funcionamento

1. **Cadastro de perguntas e respostas**
   - O sistema inicia com algumas perguntas e respostas adicionadas manualmente.

2. **Representação dos textos**
   - As perguntas e respostas são transformadas em vetores numéricos usando **TF-IDF**.

3. **Busca da resposta**
   - O texto da pergunta do usuário é comparado com os textos das respostas.
   - A comparação é feita com **similaridade de cosseno**.
   - A resposta mais semelhante é retornada.

4. **Interação com o usuário**
   - O programa entra em um loop pedindo perguntas.
   - Se o usuário digitar `sair`, o programa encerra.
   - Caso contrário, tenta encontrar a resposta mais próxima.

---

##  Exemplo de Uso

### Perguntas cadastradas:
- "Qual é a capital da França?"
- "Quem escreveu 'Dom Casmurro'?"

### Respostas cadastradas:
- "A capital da França é Paris."
- "Machado de Assis escreveu 'Dom Casmurro'."

### Execução:
```bash
Digite sua pergunta (ou 'sair' para encerrar): Qual é a capital da França?
Resposta encontrada: A capital da França é Paris.

Digite sua pergunta (ou 'sair' para encerrar): Quem escreveu Dom Casmurro?
Resposta encontrada: Machado de Assis escreveu 'Dom Casmurro'.

Digite sua pergunta (ou 'sair' para encerrar): sair
Encerrando o programa.
