Astronomy Planetarium API 

API REST desenvolvida utilizando Django e Django REST Framework para gerenciamento de espetáculos astronômicos, temas, cúpulas de planetário, sessões, reservas e ingressos. 

A API concede acesso para cadastrar e consultar espetáculos, elaborar sessões em diferentes cúpulas, fazer reservas e gerenciar ingressos, com controle de acesso por autenticação. 

📋 Funcionalidades 

A API disponibiliza as seguintes funcionalidades: 

    Espetáculos astronômicos: cadastro, consulta, atualização e exclusão de espetáculos. 

    Temas: gerenciamento dos temas associados aos espetáculos. 

    Cúpulas do planetário: cadastro e gerenciamento das cúpulas, incluindo quantidade de fileiras, assentos por fileira e capacidade total. 

    Sessões: gerenciamento de sessões, vinculando espetáculos às cúpulas e definindo data e horário. 

    Upload de imagens: permite adicionar imagens às sessões. 

    Reservas: criação e gerenciamento de reservas associadas ao usuário autenticado. 

    Ingressos: gerenciamento de ingressos, com identificação de fileira e assento. 

    Controle de acesso: autenticação por token e restrição de acesso aos recursos privados. 

🛠️ Tecnologias empregadas 

    Python 

    Django 

    Django REST Framework 

    Django REST Framework Token Authentication 

    SQLite (banco de dados padrão do Django, caso não tenha sido substituído) 

    drf-spectacular ou drf-yasg (para documentação Swagger e Redoc, caso configurado) 

⚙️ Requisitos 

Antes de executar o projeto, certifique-se de ter instalado: 

    Python 3.10 ou superior (conforme compatibilidade das dependências). 

    pip. 

    Git. 

    Ambiente virtual Python. 

🚀 Instalação e execução local 

1. Clone o repositório 

bash 

git clone: https://github.com/andrearantes/planetarium-api-service.git  
 

Entre na pasta do projeto: 

bash 

cd <planetarium-api-serice> 
 

2. Crie e ative um ambiente virtual 

Linux/macOS: 

bash 

python3 -m venv venv 
source venv/bin/activate 
 

Windows: 

bash 

python -m venv venv 
.\venv\Scripts\Activate.ps1 
 

3. Instale as dependências 

Se o projeto possuir um arquivo requirements.txt: 

bash 

pip install -r requirements.txt 
 

Caso ainda não possua, as principais dependências são: 

bash 

pip install django djangorestframework pillow 
 

Para usar a autenticação por token, certifique-se de incluir rest_framework.authtoken em INSTALLED_APPS. 

Para elaborar a documentação Swagger e Redoc com drf-spectacular, instale também: 

bash 

pip install drf-spectacular 
 

4. Configure o banco de dados 

Execute as migrações: 

bash 

python manage.py makemigrations 
python manage.py migrate 
 

5. Crie um superusuário 

bash 

python manage.py createsuperuser 
 

Siga as orientações para cadastrar usuário e senha. 

6. Execute o servidor 

bash 

python manage.py runserver 
 

A API estará disponível em: 

text 

http://127.0.0.1:8000/ 
 

🔗 Endpoints disponíveis 

Todos os endpoints usam o prefixo /api/ como exemplo. Ajuste o prefixo conforme a configuração principal de URLs do projeto. 

A API utiliza DefaultRouter do Django REST Framework, disponibilizando automaticamente as operações CRUD. 

Recurso 
	

Endpoint 

Espetáculos 
	

/api/shows/ 

Temas 
	

/api/themes/ 

Cúpulas 
	

/api/domes/ 

Sessões 
	

/api/sessions/ 

Reservas 
	

/api/reservations/ 

Ingressos 
	

/api/tickets/ 

 

 

Métodos HTTP 

Método 
	

Funcionalidade 

GET 
	

Listar ou consultar registros 

POST 
	

Criar um novo registro 

PUT 
	

Atualizar completamente um registro 

PATCH 
	

Atualizar parcialmente um registro 

DELETE 
	

Excluir um registro 

Para consultar um registro específico, utilize seu ID: 

text 

GET /api/shows/1/ 
 

🔍 Filtros disponíveis 

A API possibilita filtrar os resultados por parâmetros enviados na URL. 

Espetáculos (/api/shows/) 

Parâmetro 
	

Descrição 

title 
	

Pesquisa espetáculos pelo título, sem diferenciar maiúsculas e minúsculas 

theme 
	

Filtra espetáculos pelo ID do tema 

Exemplos: 

http 

GET /api/shows/?title=Saturno 
GET /api/shows/?theme=2 
GET /api/shows/?title=Sistema&theme=1 
 

Temas (/api/themes/) 

Parâmetro 
	

Descrição 

name 
	

Pesquisa temas pelo nome 

Exemplo: 

http 

GET /api/themes/?name=Planetas 
 

Cúpulas (/api/domes/) 

Parâmetro 
	

Descrição 

name 
	

Pesquisa cúpulas pelo nome 

Exemplo: 

http 

GET /api/domes/?name=Principal 
 

Sessões (/api/sessions/) 

Parâmetro 
	

Descrição 

planetarium_dome 
	

Filtra sessões pelo ID da cúpula 

astronomy_show 
	

Filtra sessões pelo ID do espetáculo 

Exemplos: 

http 

GET /api/sessions/?planetarium_dome=1 
GET /api/sessions/?astronomy_show=2 
GET /api/sessions/?planetarium_dome=1&astronomy_show=2 
 

Reservas e ingressos 

As reservas e os ingressos são filtrados automaticamente de acordo com o usuário autenticado. 

    Um usuário consulta somente suas próprias reservas. 

    Um usuário consulta somente os ingressos vinculados às suas reservas. 

    Ao criar uma reserva, o usuário é vinculado automaticamente à reserva. 

    Um ingresso só pode usar uma reserva pertencente ao usuário autenticado. 

🔐 Autenticação por token 

A API usa o mecanismo TokenAuthentication do Django REST Framework. 

A autenticação é necessária para acessar recursos protegidos, como reservas e ingressos. 

1. Obter um token 

Para obter um token, é necessário que exista um endpoint de autenticação configurado no projeto. 

Caso ainda não possua, adicione ao urls.py principal: 

python 

from rest_framework.authtoken.views import obtain_auth_token 
 
urlpatterns = [ 
    path("api/token/", obtain_auth_token), 
] 
 

Também precisa adicionar rest_framework.authtoken ao INSTALLED_APPS no settings.py. 

Depois, execute: 

bash 

python manage.py migrate 
 

Envie uma requisição POST com usuário e senha: 

http 

POST /api/token/ 
Content-Type: application/json 
 

Corpo da requisição: 

json 

{ 
    "username": "seu_usuario", 
    "password": "sua_senha" 
} 
 

Resposta esperada: 

json 

{ 
    "token": "seu_token_de_autenticacao" 
} 
 

2. Enviar o token nas requisições 

Após obter o token, inclua-o no cabeçalho HTTP das requisições protegidas: 

http 

Authorization: Token seu_token_de_autenticacao 
 

Exemplo utilizando cURL: 

bash 

curl -X GET http://127.0.0.1:8000/api/reservations/ \ 
-H "Authorization: Token seu_token_de_autenticacao" 
 

Importante: não compartilhe seu token com terceiros. Ele funciona como uma credencial de acesso à API. 

🖼️ Upload de imagens 

O upload de imagens é realizado pelo endpoint de sessões: 

http 

POST /api/sessions/ 
 

O campo image aceita arquivos de imagem e utiliza o armazenamento configurado no Django. 

As imagens são salvas no diretório: 

text 

media/sessions/ 
 

O upload utiliza o formato multipart/form-data. 

Exemplo com Postman 

    Selecione o método POST. 

    Informe a URL http://127.0.0.1:8000/api/sessions/. 

    Acesse a aba Body. 

    Selecione form-data. 

    Adicione os seguintes campos: 

Key 
	

Type 
	

Value 

astronomy_show 
	

Text 
	

1 

planetarium_dome 
	

Text 
	

1 

show_time 
	

Text 
	

2026-12-05T14:00:00Z 

image 
	

File 
	

Selecione uma imagem 

    Na aba Headers, adicione: 

http 

Authorization: Token seu_token_de_autenticacao 
 

    Envie a requisição. 

Exemplo com cURL 

bash 

curl -X POST http://127.0.0.1:8000/api/sessions/ \ 
-H "Authorization: Token seu_token_de_autenticacao" \ 
-F "astronomy_show=1" \ 
-F "planetarium_dome=1" \ 
-F "show_time=2026-12-05T14:00:00Z" \ 
-F "image=@/caminho/da/imagem.jpg" 
 

O cURL configura automaticamente o cabeçalho Content-Type: multipart/form-data com o boundary necessário. 

Observações: 

    O campo image é opcional. 

    Os campos astronomy_show e planetarium_dome recebem os IDs dos registros existentes. 

    O horário deve estar em formato compatível com DateTimeField. 

    Para armazenar e servir imagens corretamente, configure MEDIA_ROOT e MEDIA_URL no settings.py. 

Exemplo de configuração: 

python 

MEDIA_URL = "/media/" 
MEDIA_ROOT = BASE_DIR / "media" 
 

No ambiente de desenvolvimento, também é necessário configurar o serviço de arquivos de mídia no urls.py principal. 

📚 Documentação da API — Swagger e Redoc 

A documentação interativa permite visualizar os endpoints, consultar os parâmetros, testar requisições e verificar os formatos de resposta. 

Caso seja utilizado o pacote drf-spectacular, instale-o: 

bash 

pip install drf-spectacular 
 

Adicione ao INSTALLED_APPS: 

python 

INSTALLED_APPS = [ 
    # Aplicativos existentes 
    "rest_framework", 
    "rest_framework.authtoken", 
    "drf_spectacular", 
] 
 

Configure o Django REST Framework no settings.py: 

python 

REST_FRAMEWORK = { 
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema", 
} 
 

No urls.py principal do projeto, adicione: 

python 

from django.urls import path, include 
from drf_spectacular.views import ( 
    SpectacularAPIView, 
    SpectacularSwaggerView, 
    SpectacularRedocView, 
) 
 
urlpatterns = [ 
    path("api/", include("sua_app.urls")), 
 
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"), 
 
    path( 
        "api/docs/swagger/", 
        SpectacularSwaggerView.as_view(url_name="schema"), 
        name="swagger-ui", 
    ), 
 
    path( 
        "api/docs/redoc/", 
        SpectacularRedocView.as_view(url_name="schema"), 
        name="redoc", 
    ), 
] 
 

Após configurar, os links de documentação serão: 

    Swagger UI: http://127.0.0.1:8000/api/docs/swagger/ 

    Redoc: http://127.0.0.1:8000/api/docs/redoc/ 

    OpenAPI Schema: http://127.0.0.1:8000/api/schema/ 

📦 Exemplos de utilização 

Criar um tema 

http 

POST /api/themes/ 
Content-Type: application/json 
 

json 

{ 
    "name": "Sistema Solar" 
} 
 

Criar um espetáculo 

http 

POST /api/shows/ 
Content-Type: application/json 
 

json 

{ 
    "title": "Explorando Saturno", 
    "description": "Uma viagem pelos anéis e luas de Saturno.", 
    "themes": [1, 2] 
} 
 

Criar uma cúpula 

http 

POST /api/domes/ 
Content-Type: application/json 
 

json 

{ 
    "name": "Cúpula Principal", 
    "rows": 10, 
    "seats_in_row": 15, 
    "description": "Cúpula principal do planetário." 
} 
 

A capacidade total será calculada automaticamente: 

text 

capacity = rows × seats_in_row 
capacity = 10 × 15 
capacity = 150 lugares 
 

Criar uma reserva 

http 

POST /api/reservations/ 
Authorization: Token seu_token_de_autenticacao 
Content-Type: application/json 
 

json 

{} 
 

O usuário será associado automaticamente à reserva. 

Criar um ingresso 

http 

POST /api/tickets/ 
Authorization: Token seu_token_de_autenticacao 
Content-Type: application/json 
 

json 

{ 
    "row": 3, 
    "seat": 5, 
    "show_session": 1, 
    "reservation": 1 
} 
 

Cada assento só pode ser reservado uma vez por sessão, devido à restrição de unicidade definida no modelo Ticket. 

🔒 Regras de negócio e permissões 

    Espetáculos, temas e cúpulas possuem operações CRUD sem restrição de autenticação declarada nas respectivas ViewSets. 

    Sessões permitem consultas públicas, mas operações de escrita exigem autenticação. 

    Reservas exigem autenticação em todas as operações. 

    O usuário apenas consegue visualizar suas próprias reservas. 

    O usuário só consegue visualizar ingressos vinculados às suas reservas. 

    O usuário não pode usar uma reserva pertencente a outra pessoa ao cadastrar um ingresso. 

    Um mesmo assento não pode ser cadastrado duas vezes para a mesma sessão. 

    A capacidade da cúpula é calculada automaticamente com base no número de fileiras e assentos por fileira. 