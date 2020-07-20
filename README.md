# Central de Erros   [![Build Status](https://travis-ci.com/KarolRodriguespy/CentraldeerrosCodenation.svg?branch=master)](https://travis-ci.com/KarolRodriguespy/CentraldeerrosCodenation)

## Objetivo

Em projetos modernos é cada vez mais comum o uso de arquiteturas baseadas em serviços ou microsserviços. Nestes ambientes complexos, erros podem surgir em diferentes camadas da aplicação (backend, frontend, mobile, desktop) e mesmo em serviços distintos. Desta forma, é muito importante que os desenvolvedores possam centralizar todos os registros de erros em um local, de onde podem monitorar e tomar decisões mais acertadas. Neste projeto vamos implementar um sistema para centralizar registros de erros de aplicações.


### Ferramentas Usadas

* Django
* Django Rest Framework
* Authentication Token
* Postgress


Documentação API:



### Como baixar os arquivos

-  Faça uma cópia do repositório na sua máquina
>

     https://github.com/KarolRodriguespy/CentraldeerrosCodenation.git

- Crie um novo ambiente virtual e ative 

Windows
>

      python -m venv env 
      env\Scripts\activate.bat

 MAC
 >

      python3 -m venv env 
      source env/bin/activate
 
 
- Instale as dependencias do arquivo requirements.txt 

 >

       pip install - r requirements.txt
     
      
      
      
-  Crie as migrations

 >

       python manage.py migrate

-  Crie um usuario

 >

     python manage.py shell 
     from django.contrib.auth.models import User   
     user = User.objects.create_user('<yourname>', password='<password>')
     user.save()   
     
     Ou acesse http://127.0.0.1:8000//rest-auth/registration/  e informe seu username, email e password
     
- Rode o servidor 

 >

       python manage.py runserver
       
- Crie o Token

 >

       http://127.0.0.1:8000//rest-auth/login e informe o seu usuário e senha no body da requisição

### Endpoints

| Endpoints | Ação  |
|---|:---:|
| http://127.0.0.1:8000//rest-auth/registration/  | Cria Um usuário  |
| http://127.0.0.1:8000//rest-auth/login | Retorna o token que deve ser enviado no header da requisição  |
| http://127.0.0.1:8000/events/create  | Cria o Evento  |
| http://127.0.0.1:8000/events/list  |  Lista todos os eventos criados |
| http://127.0.0.1:8000/events/detail/{id} | Detalha um evento através do ID  |
| http://127.0.0.1:8000/events/update/{id}  | Altera um evento através do ID  |
| http://127.0.0.1:8000/events/delete/{id}  | Deleta um evento  |


[Link de produção](https://centraldeerros-projeto.herokuapp.com/)