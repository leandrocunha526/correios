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

## Teste

O teste que foi apresentado é uma forma de teste de unidade. Mais especificamente, trata-se de testes de unidade
automatizados. O termo "unidade" refere-se ao fato de que o teste é projetado para testar a funcionalidade de uma
unidade isolada do código, no caso, a função buscar_cep do módulo correios.py.

Os testes de unidade são uma prática comum no desenvolvimento de software e têm como objetivo verificar se cada parte
individual do código (unidade) funciona corretamente e de acordo com as expectativas. Eles são projetados para serem
rápidos e independentes, garantindo que cada parte do código esteja correta antes de ser integrada a outras partes do
sistema.

Neste caso, os testes foram escritos usando a biblioteca pytest, que é uma popular estrutura de teste em Python. O
pytest torna mais fácil escrever e executar testes, além de fornecer recursos adicionais para a criação de testes mais
complexos.

Os testes de unidade automatizados têm várias vantagens, incluindo:

Rapidez: Como os testes são automatizados, eles podem ser executados rapidamente, permitindo que você teste o código
frequentemente e durante o desenvolvimento.

Confiabilidade: Os testes automatizados são consistentes e executados da mesma maneira toda vez, garantindo resultados
confiáveis.

Facilidade de detecção de erros: Caso uma alteração introduza um erro, os testes de unidade ajudam a identificá-lo
rapidamente, tornando mais fácil a correção antes que o erro se propague para outras partes do sistema.

Documentação viva: Os testes de unidade servem como documentação viva do comportamento esperado do código, facilitando
a compreensão do funcionamento das funções e métodos.

Em resumo, os testes de unidade automatizados são uma prática essencial no desenvolvimento de software moderno,
contribuindo para a qualidade e confiabilidade do código, bem como para a facilidade de manutenção e evolução do
sistema.