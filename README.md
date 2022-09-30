# Bot Telegram para consulta de dados da Covid19 no Espírito Santo


* Este foi um projeto realizado nos anos de 2020/2021, durante a pandemia, para que seja possível consultar o número de casos por cidade no estado
do Espírito Santo. Para isso, foi utilizado a [base de dados](https://coronavirus.es.gov.br/painel-covid-19-es) fornecidade pelo Governo do Estado que possui todas as informações dos casos de Covid. Sendo realizado a coleta e o tratamento destes dados para o fornecimento de informações ao usuário.

## :scroll:	Funcionalidades
- Consulta dos dados via **CEP**.
- Consulta dos dados por meio do **nome da cidade**.
- Consulta dos dados por meio da **listagem de todas as cidades** do estado do Espírito Santo.
- Geração de um **mapa de calor** de acordo com o número de casos ativos por cidade.

## :desktop_computer: Tecnologias e Conceitos utilizados 
- Linguagem **Python**. 
- Biblioteca **Telegram** para implementação do bot.
- Consulta a API **ViaCep** para obter a cidade do CEP digitado.
- **Pandas** para consultar e tratar os dados. 
- **Folium** para geração do mapa de calor (HeatMap).
- **Selenium** para abrir o HTML do mapa de calor.
- **PIL** e **Pyscreenshot** para tirar e salvar o print do mapa de calor.

---

## :computer_mouse: Demonstração do Sistema

<img src="https://user-images.githubusercontent.com/101357910/193175175-a032579e-c4b3-4b80-af28-a91ad0150e19.gif" width="45%" height="45%"/>

---

## :keyboard: Comandos
- **_/start_** : Inicializa a conversa com o bot.
- **_/dados_** : Exibe as formas de consulta de dados.
- **_/nome_** : Exibe todas as cidades do estado para seleção.
- **_/mapa_** : Envia o Mapa de Calor dos casos do Estado.
- **_/atualizar_** : Atualiza os dados no site do Governo do Estado (**_Somento o ADMIN definido no arquivo .env pode executar esse comando_**).
- **_/atmap_**: Gera um novo mapa de calor (**_Somento o ADMIN definido no arquivo .env pode executar esse comando_**).

## :man_technologist: Como executar o Sistema

- Faça um clone deste repositório.
- Abra o projeto em sua IDE de preferência (PyCharm, VsCode, etc).
- Instale as dependências (_requirements.txt_):
```
pip install -r requirements.txt
```
- Instale o webdriver de acordo com a versão de seu navegador.
- Crie um arquivo **_.env_** com as seguintes informações:
```
TOKEN=Token Bot Telegram
ADMIN=Seu ID de usuário
```

- Execute o arquivo _bot.py_
- Atualize os dados ( **_/atualizar_** ) 
- Realize a geração do Mapa ( **_/atmap_** )
