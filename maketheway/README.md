# Tecnologias:

-Django

-Postgresql

-Docker (compose)


# Instruções:
Para rodar o projeto dockerizado é necessário usar o comando "docker-compose up" no diretório /maketheway (o próprio docker se encarregará de buildar as imagens)

A aplicação rodará na porta 8000 então é necessário tê-la disponível.

O servidor utilizado foi o do próprio Django (não recomendado para ambientes de produção).

O container persistirá as informações inseridas no banco.


# Upload arquivos CSV:
O upload de arquivos CSV contempla todos os registros, inclusive mistos, utilizando o separador '|' como descrito na documentação.

O upload de arquivos é feito na URI:

- /upload_csv


# RESTful:
Dado que o 'tipo' é o tipo de registro (0000, 0150, C100, C170)
O consumo de recursos da API é feito nas URIs:

- /list/tipo

- /edit/tipo/pk

- /delete/tipo/pk

Como é disponibilizado o recurso upload_csv, o projeto não conta com o recurso "create" utilizando do CSV para inserção de dados.
