## API de Produtos

API de produtos usando Python e Django Rest Framework

Ambiente contendo:

- Python 3.9.10
- Django Rest Framework 3.13.1

```bash
# Clonando o repositório
$ git clone https://github.com/mellyssaStephanny/api-products.git

# Entre na pasta do projeto
$ cd api-products

# Crie um ambiente virtual
$ virtualenv nome_da_virtualenv

# Ative o ambiente virtual (de acordo com seu SO)
$ source nome_da_virtualenv/bin/activate (Linux ou macOS)
$ nome_da_virtualenv/Scripts/Activate (Windows)

# Instale as dependências
$ pip install -r requirements

# Migrar modelo para o banco de dados
$ python manage.py makemigrations

# Enviar os dados para o banco
$ python manage.py migrate

## Executar servidor
$ python manage.py runserver

```

### Rotas

- GET/products/id
  - listar um produto
- GET/products
  - listar todos produtos
- DEL/products/id
  - apagar um produto
- PUT/products/id
  - atualizar um produto
- POST/products
  - criar produto
