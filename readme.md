# Django Animes API

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

- O objetivo da nossa aplicação é criar um streaming de animes com sistema de gerenciamento de perfis. A principal motivação é oferecer aos fãs de animes uma plataforma de reprodução de alto desempenho e de fácil acesso para assistir aos seus animes favoritos.Sabe-se que muitas vezes os fãs de animes enfrentam dificuldades para encontrar todos os episódios de uma determinada série em um único lugar, e por isso criamos a nossa API para resolver esse problema.

- Atualmente, muitos streaming ou sites de  animes apresentam problemas de lentidão ou até mesmo falhas na reprodução dos vídeos, sem contar as inúmeras propagandas que acabam com a diversão. Para garantir uma experiência de reprodução suave e sem interrupções, estamos armazenando os links dos episódios em servidores do AWS. 

- A aplicação contará com uma opção gratuita com anúncios breves, dentro do próprio vídeo, que poderá ser pulado após 5 segundos assistido. E uma opção premium, de faço acesso para todos, o usuário premium terá vários benefícios, como editar livremente o perfil, com customizações únicas, como ganhar “achievements” (conquistas) por assistir ou terminar um determinado anime.   

- A aplicação  contará com tipos de usuarios diferentes, sendo eles FREE, BRONZE, SILVER, GOLD, cada um com seus beneficíos específicos, sendo eles numero de profiles permitidos, conquistas específicas, ícones, fazer comentários, entre outros.

- Com a django animes voce pode utilizar  os profiles simultaneamente em dispositivos diferentes, Caso divida a conta com sua familia e esteja assistindo a mesma serie, uma pessoa nao ira interferir no desenvolvimento na serie de outro profile.


<a name="links"></a>

## 2. Links relevantes

- <a name="deploy-da-aplicação" href ="#" target="_blank">Link da aplicação</a>

- <a name="documentação-api" href="#" target="_blank">Documentação API</a>

 <h3> Diagrama ER da API definindo bem as relações entre as tabelas do banco de dados. </h3>

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

<a name="install"></a>

## 4. Instalação e uso

### 4.1 Requisitos

- Python a partir da versão 3.11.1
- Gerenciador de pacotes pip
- Banco de dados PostgreSQL

### 4.2 Instalação

 4.2.1 - Crie um banco de dados chamado Django_animes_database no PostgreSQL
 4.2.2 - Após o clone no repositório crie um ambiente de desenvolvimento:
 ```
 python -m venv venv
 ```
 
 4.2.3 - Após a criação do ambiente virtual voce terá que ativa-lo com o seguinte comando
 
 para linux:
 ```
 source/venv/bin/activate
 ```
 
 para windows:
 ```
 .\venv\Scripts\activate
 ```
 
 4.2.4 - Crie um arquivo na raiz do projeto chamado .env e faça as configurações das variáveis de ambiente com base no .env.example do projeto

```
SECRET_KEY= chave secreta definida pelo seu time de desenvolvimento
DATABASE_URL=postgresql://seu_usuario:sua_senha@localhost:5432/vibe_database
```

4.2.5 - Agora que ja ativou o ambiênte de desenvolvimento voce terá que instalar as dependências do projeto
```
pip install -r requirements.txt
```

4.2.6 - Após instalar as dependências vamos persistir as migrations no banco de dados
```
python manage.py migrate
```


4.2.7 - Para rodar projeto utilize o comando 
```
python manage.py runserver
``` 

4.2.8 - Caso de tudo certo receberá uma mensagem parecida com essa:

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

- <a name="Gabriel-Fernandes" href="https://github.com/gabriellfernandes" target="_blank">Gabriel Fernandes</a>
- <a name="Gabriel-fray" href="https://www.linkedin.com/in/gabrielfray/" target="_blank">Gabriel Fray</a>
- <a name="Guilherme-teles" href="https://www.linkedin.com/in/guilherme-teles-103853235/" target="_blank">Guilherme Teles</a>
- <a name="Henrique-pires-Bezerra" href="https://www.linkedin.com/in/henrique-pires-bezerra/" target="_blank">Henrique Pires Bezerra</a>
- <a name="Stevan Santos" href="https://www.linkedin.com/in/stevansantos/" target="_blank">Stevan Santos</a>
- <a name="Vinicius-Moreira-Henrique" href="https://www.linkedin.com/in/vinicius-moreira-henrique/" target="_blank">Vinicius Moreira Henrique</a>

<a name="terms"></a>

## 6. Termos de uso

Este é um projeto Open Source para fins educacionais e não comerciais, **Tipo de licença** - <a name="mit" href="https://opensource.org/licenses/MIT" target="_blank">MIT</a>
