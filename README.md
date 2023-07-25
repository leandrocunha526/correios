# Correios

## Introdução

Para instalar as dependências do projeto, execute o comando:
`pip install -r requirements.txt`

Se você deseja salvar todos os CEPs em uma determinada faixa de CEPs na API dos Correios, você precisará iterar por essa 
faixa e consultar cada CEP individualmente.

Vamos modificar a função obter_dados_cep para que ela retorne os dados do CEP como um dicionário e lide com erros de
consulta:

Neste exemplo, a função salvar_todos_ceps iterará por todos os CEPs dentro da faixa especificada (do cep_inicial até o
cep_final) e salvará os dados encontrados na tabela do PostgreSQL.

Lembre-se de que a consulta e o salvamento de um grande número de CEPs podem levar algum tempo, dependendo do tamanho da
faixa de CEPs. Certifique-se de testar em uma faixa menor antes de realizar consultas extensas. Além disso, é importante
observar que a API dos Correios tem limites de consultas por minuto, por isso, verifique as políticas e limites de uso
da API para garantir que você esteja dentro das diretrizes fornecidas pelos Correios.