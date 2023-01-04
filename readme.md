# DjangoAnimes README API

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

- <a name="deploy-da-aplicação" href ="#" target="_blank">Link da aplicação</a>

- <a name="documentação-api" href="#" target="_blank">Documentação API</a>

- Diagrama ER da API definindo bem as relações entre as tabelas do banco de dados.

<img height="700" align="center" src="https://i.imgur.com/55gGw4d.png"></img>

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

- Python a partir da versão 3.11.1
- Gerenciador de pacotes pip
- Banco de dados PostgreSQL

### 4.2 Instalação

4.2.1 - Crie um banco de dados chamado Django_animes_database no PostgreSQL
4.2.2 - Após o clone no repositório crie um ambiente de desenvolvimento:
`python -m venv venv`
4.2.3 - Após a criação do ambiente virtual voce terá que ativa-lo com o seguinte comando
 para linux:`source/venv/bin/activate`
 para windows: `.\venv\Scripts\activate`

4.2.4 - Agora que ja ativou o ambiênte de desenvolvimento voce terá que instalar as dependências do projeto
`pip install -r requirements.txt`

4.2.5 - Após instalar as dependências vamos persistir as migrations no banco de dados
`python manage.py migrate`

4.2.3 - Crie um arquivo na raiz do projeto chamado .env e faça as configurações das variáveis de ambiente com base no .env.example do projeto

```
SECRET_KEY= chave secreta definida pelo seu time de desenvolvimento
DATABASE_URL=postgresql://seu_usuario:sua_senha@localhost:5432/vibe_database
```

4.2.4 - Para rodar projeto utilize o comando `python manage.py runserver` no terminal, caso de tudo certo receberá uma mensagem parecida com essa:

```
System check identified no issues (0 silenced).
January 04, 2023 - 13:53:34
Django version 4.1.5, using settings 'djangoAnimes.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

<a name="devs"></a>

## 5. Desenvolvedores

[Voltar para o topo](#tabela-de-conteúdos)

- <a name="Gabriel-Fernandes" href="https://www.linkedin.com/in/gabriel-lima-fernandes/" target="_blank">Gabriel Fernandes</a>
- <a name="Gabriel-fray" href="https://www.linkedin.com/in/gabrielfray/" target="_blank">Gabriel Fray</a>
- <a name="Guilherme-teles" href="https://www.linkedin.com/in/guilherme-teles-103853235/" target="_blank">Guilherme Teles</a>
- <a name="Henrique-pires-Bezerra" href="https://www.linkedin.com/in/henrique-pires-bezerra/" target="_blank">Henrique Pires Bezerra</a>
- <a name="Stevan Santos" href="https://www.linkedin.com/in/stevansantos/" target="_blank">Stevan Santos</a>
- <a name="Vinicius-Moreira-Henrique" href="https://www.linkedin.com/in/vinicius-moreira-henrique/" target="_blank">Vinicius Moreira Henrique</a>

<a name="terms"></a>

## 6. Termos de uso

Este é um projeto Open Source para fins educacionais e não comerciais, **Tipo de licença** - <a name="mit" href="https://opensource.org/licenses/MIT" target="_blank">MIT</a>
