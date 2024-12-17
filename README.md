# Sistema de Gerenciamento de Leads

Este é um sistema CRUD (Create, Read, Update, Delete) para gerenciamento de leads desenvolvido com Django.

## Configuração do Ambiente

1. Primeiro, crie um ambiente virtual: 

No Windows
python -m venv venv

No Linux/Mac
python3 -m venv venv

3. Instale as dependências:

pip install -r requirements.txt

## Estrutura do Projeto

### Arquivos Principais

- `prospect_crud/app/models.py`: Define o modelo de dados Lead com os campos:
  - name (nome)
  - email
  - phone (telefone)
  - whatsapp (opcional)
  - facebook (opcional)

- `prospect_crud/app/views.py`: Contém as funções de visualização para:
  - `lead_list`: Lista todos os leads
  - `lead_create`: Cria novo lead
  - `lead_update`: Atualiza lead existente
  - `lead_delete`: Remove lead
  - `lead_detail`: Mostra detalhes do lead

- `prospect_crud/app/urls.py`: Define as URLs do aplicativo:
  - `/leads/`: Lista de leads
  - `/leads/create/`: Criar novo lead
  - `/leads/<id>/`: Detalhes do lead
  - `/leads/<id>/update/`: Atualizar lead
  - `/leads/<id>/delete/`: Deletar lead

### Templates Necessários

Você precisará criar os seguintes templates na pasta `prospect_crud/app/templates/app/`:

`login.html`
`register.html`
`logout.html`

1. `lead_list.html`: Página principal com lista de todos os leads
2. `lead_form.html`: Formulário para criar/editar leads
3. `lead_detail.html`: Página de detalhes do lead
4. `lead_confirm_delete.html`: Página de confirmação de exclusão

Também é necessário criar um template base em `prospect_crud/templates/base.html`

Use o ChatGPT pra te ajudar. É preciso criar os testes de cada endpoint (cada função das views) 

cada template será mapeado a uma view. geralmente a função da view é chamada no formulário html do template.

## Configuração do Banco de Dados

1. Aplique as migrações:

python manage.py makemigrations
python manage.py migrate

Acesse o sistema em: `http:/localhost:8000/leads/`


