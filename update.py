import pandas as pd

# DataFrame Cidades Es
df_cid = pd.read_csv("cidades_es.csv")
cidades_es = list()
for i in df_cid['Municipio'].unique():
    cidades_es.append(i.capitalize())


def UpdateCsv():
    global dados
    #Alterar estrutura
    dados = pd.read_csv("https://bi.s3.es.gov.br/covid19/MICRODADOS.csv", delimiter=";", encoding="latin1")
    dados['Municipio'] = dados['Municipio'].str.lower()
    dados = dados.merge(df_cid[['Municipio', 'Latitude', 'Longitude']], on='Municipio')
    dados['Municipio'] = dados['Municipio'].str.capitalize()
    dados = dados[dados['Municipio'].isin(cidades_es)]
    dados['Bairro'] = dados['Bairro'].str.capitalize()
    col_drop = ['DataCadastro', 'DataDiagnostico',
                'DataColeta_RT_PCR', 'DataColetaTesteRapido', 'DataEncerramento',
                'DataObito', 'Classificacao', 'Evolucao', 'CriterioConfirmacao',
                'IdadeNaDataNotificacao', 'Sexo', 'RacaCor', 'Escolaridade', 'ViagemBrasil',
                'ViagemInternacional', 'MoradorDeRua']

    dados = dados.drop(col_drop, axis=1)
    dados = dados.replace("Não Informado", "Não")
    dados['DataNotificacao'] = pd.to_datetime(dados['DataNotificacao'], format="%Y/%m/%d")
    dados['DataNotificacao'] = dados['DataNotificacao'].dt.strftime("%d/%m/%Y")
    dados.to_csv("dados.csv", index=False, encoding="latin1")


def CidadesEs():
    return cidades_es
