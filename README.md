# Automação de Cadastro com Python

Este projeto foi desenvolvido com o objetivo de **automatizar o cadastro de produtos em um sistema web**, utilizando **Python**, **PyAutoGUI** e **Pandas**. Ele lê uma base de dados em CSV e simula a interação humana com o navegador, preenchendo formulários de forma automática, rápida e eficiente.

## Objetivo do Projeto

O projeto resolve um problema comum no dia a dia de empresas e equipes administrativas: **cadastro manual e repetitivo de produtos**.

Com essa automação, é possível:

* Economizar tempo
* Reduzir erros humanos
* Padronizar cadastros
* Ganhar produtividade

## Como Funciona

1. O script abre o navegador automaticamente
2. Acessa o sistema da empresa
3. Realiza login
4. Lê os dados de um arquivo `produtos.csv`
5. Para cada linha do CSV, preenche os campos do formulário
6. Envia o cadastro e repete o processo até finalizar a base

Toda a automação é feita simulando teclado, mouse e cliques reais.

## Tecnologias Utilizadas

* **Python 3**
* **PyAutoGUI** — automação de mouse e teclado
* **Pandas** — leitura e manipulação de dados
* **CSV** — base de dados dos produtos
* **Virtual Environment (.venv)** — isolamento do ambiente

## 📂 Estrutura do Projeto

```
Pyton PowerUp/
│
├── .venv/              # Ambiente virtual
├── codigo.py           # Script principal de automação
├── produtos.csv        # Base de dados dos produtos
└── README.md           # Documentação do projeto
```

## ⚙️ Pré-requisitos

Antes de rodar o projeto, é necessário:

* Python instalado
* VS Code (recomendado)
* Criar e ativar uma virtual environment

Instalação das dependências:

```
pip install pandas pyautogui
```

## Como Executar

Certifique-se de estar na pasta do projeto e com a `.venv` ativa:

```
.\.venv\Scripts\python.exe codigo.py
```

Ou, após configurar corretamente o interpretador no VS Code:

```
python codigo.py
```

## Observações Importantes

* As coordenadas de clique (`x` e `y`) dependem da resolução da tela
* O navegador deve estar em tela cheia
* O site precisa estar carregado antes das ações (uso de `sleep`)
* O nome das colunas do CSV deve coincidir com o código

## Aprendizados

Este projeto proporcionou aprendizado prático sobre:

* Automação real com Python
* Ambientes virtuais no Windows
* Integração entre dados e interface gráfica
* Debug de erros de ambiente e dependências
Estudante de Análise e Desenvolvimento de Sistemas
Apaixonada por tecnologia, automação e produtividade

---

⭐ Se este projeto te ajudou ou te inspirou, não esqueça de deixar uma estrela!
