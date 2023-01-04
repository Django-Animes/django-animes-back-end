# Vibefy documentation API

## Tabela de Conteúdos

1. [Sobre](#sobre)
2. [Links Relevantes](#links)
3. [Techs](#techs)
4. [Instalação](#install)
5. [Desenvolvedores](#devs)
6. [Termos de uso](#terms)

---

<a name="sobre"></a>

## 1. Sobre

<a name="links"></a>

## 2. Links relevantes

- <a name="deploy-da-aplicação" href ="https://vibefyproject.herokuapp.com/" target="_blank">Link da aplicação</a>

- <a name="documentação-api" href="https://vibefyproject.herokuapp.com/api-docs" target="_blank">Documentação API</a>

- Diagrama ER da API definindo bem as relações entre as tabelas do banco de dados.

<img height="700" align="center" src="https://i.imgur.com/Z7Zolmy.png"></img>

<a align="left" name="techs"></a>

## 3. Techs

Visão Geral das tecnologias usadas no projeto.

- [Python](https://docs.python.org/3/)
- [DJANGO](https://www.djangoproject.com/)
- [django rest_framework](https://www.django-rest-framework.org/)
- [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---
<a align="left" name="techs"></a>

---
<a name="install"></a>

## 4. Instalação e uso

### 4.1 Requisitos

- NodeJs a partir da versão 16.14.1
- Gerenciador de pacotes yarn ou npm
- Banco de dados PostgreSQL

### 4.2 Instalação

4.2.1 - Crie um banco de dados chamado vibe_database no PostgreSQL
4.2.2 - Após o clone no repositório para adicionar todas as dependências do package json execute o comando:
`yarn install`

4.2.3 - Crie um arquivo na raiz do projeto chamado .env e faça as configurações das variáveis de ambiente com base no .env.example do projeto

```
SECRET_KEY= chave secreta definida pelo seu time de desenvolvimento
DATABASE_URL=postgresql://seu_usuario:sua_senha@localhost:5432/vibe_database
ADM_HASH= hash de administrador definida pela equipe de desenvolvimento
AWS_ACCESS_KEY_ID= id de acesso da aws para salvar seus arquivos
AWS_SECRET_ACCESS_KEY= chave de acesso da aws para salvar seus arquivos
```

4.2.4 - Para rodar projeto utilize o comando `yarn dev` no terminal, caso de tudo certo receberá uma mensagem parecida com essa:

```
[INFO] 17:23:18 ts-node-dev ver. 2.0.0 (using ts-node ver. 10.9.1, typescript ver. 4.8.4)
query: SELECT * FROM current_schema()
query: CREATE EXTENSION IF NOT EXISTS "uuid-ossp"
query: SELECT version();
Servidor executando.
```

<a name="devs"></a>

## 5. Desenvolvedores

[Voltar para o topo](#tabela-de-conteúdos)

- <a name="Gabriel-Fernandes" href="https://www.linkedin.com/in/gabriel-lima-fernandes/" target="_blank">Gabriel Fernandes</a>
- <a name="Gabriel-fray" href="https://www.linkedin.com/in/gabrielfray/" target="_blank">Gabriel Fray</a>
- <a name="Guilherme-teles" href="https://www.linkedin.com/in/guilherme-teles-103853235/" target="_blank">Guilherme Teles</a>
- <a name="Henrique-pires-Bezerra" href="https://www.linkedin.com/in/henrique-pires-bezerra/" target="_blank">Henrique Pires Bezerra</a>
- <a name="Victor-Ávila" href="https://www.linkedin.com/in/victor-avila-br/" target="_blank">Victor Ávila</a>
- <a name="Vinicius-Moreira-Henrique" href="https://www.linkedin.com/in/vinicius-moreira-henrique/" target="_blank">Vinicius Moreira Henrique</a>

<a name="terms"></a>

## 6. Termos de uso

Este é um projeto Open Source para fins educacionais e não comerciais, **Tipo de licença** - <a name="mit" href="https://opensource.org/licenses/MIT" target="_blank">MIT</a>
