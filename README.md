## Conversor de real para dollar

### 1. Visão geral

Projeto realizado na linguagem python que utiliza a biblioteca flask para criar um sistema que, através de requisições de uma API, retorna dados de conversões de real para dollar pelos endpoints de buscar
cotações por data e obter última cotação. O projeto utiliza a biblioteca Flask que é um framework python que permite o desenvolvimento de sistemas que consumem dados de API's de forma simples e eficaz.
As informações retornadas pela API são armazenadas num banco de dados Mysql.

### 2. Arquitetura

2.1 Backend: Contém a aplicação python, um arquivo de serviços onde estão hospedadas as funções chamadas pela aplicação, um arquivo de teste e os arquivos docker(dockerfile e docker-compose)

2.2 Banco de dados: Se trata de um banco Mysql que armazena as informações do valor da cotação, da data de requisição e da data da taxa cotada.

2.3 Containers docker: A aplicação está hospedada em containers(o banco e a aplicação) que são executadas através de um arquivo docker-compose.

### 3. Como excutar o projeto

Para executar o projeto basta acessar a pasta do ambiente virtual(venv) e executar o comando 'docker-compose up --build'. Lembrando que se o projeto for executado no windows, é necessário que o docker desktop
esteja rodando.

Após executar essas instruções, o projeto pode ser acessado nos endereços http://127.0.0.1:5000/cotacao-atual, para buscar a última cotação da API e 
http://127.0.0.1:5000/cotacao-por-data?data_inicial=09/10/2024&data_final=14/10/2024, para buscar cotações por data(para escolher as datas, basta alterar na própria URL). Existem alguns programas que podem
realizar os testes de API's como o insomnia e o postman que podem ser usados nos testes dessa API e as URLS também podem ser acionadas diretamente em um navegador localmente.

Para executar o arquivo de teste basta rodar o comando 'pytest test_app.py' dentro da pasta 'venv'

Após essas instruções, o projeto vai estar em execução. os prints abaixo mostram o sistema em funcionamento:

![image](https://github.com/user-attachments/assets/8c9c6c77-9442-4f76-bff6-7f43f06dcdd3)
A imagem acima mostra o retorno da API na requisição que busca a última cotação

![image](https://github.com/user-attachments/assets/d9a4f4c9-2f4e-4b3c-89c2-3f6fc81804b1)
Esse print mostra a resposta da API quando a requisição é enviada com as datas de inicio e a data final.

### 4. Considerações finais

Essa documentação fornece uma visão geral de configuração e execução da API utilizando docker compose para orquestrar os serviços do backend e do banco de dados.





