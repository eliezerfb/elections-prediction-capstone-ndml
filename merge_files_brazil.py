from glob import glob


fields = ['"DATA_GERACAO"', '"HORA_GERACAO"', '"ANO_ELEICAO"', '"NUM_TURNO"',
           '"DESCRICAO_ELEICAO"', '"SIGLA_UF"', '"SIGLA_UE"', '"DESCRICAO_UE"',
           '"CODIGO_CARGO"', '"DESCRICAO_CARGO"', '"NOME_CANDIDATO"',
           '"SEQUENCIAL_CANDIDATO"', '"NUMERO_CANDIDATO"', '"CPF_CANDIDATO"',
           '"NOME_URNA_CANDIDATO"', '"COD_SITUACAO_CANDIDATURA"',
           '"DES_SITUACAO_CANDIDATURA"', '"NUMERO_PARTIDO"', '"SIGLA_PARTIDO"',
           '"NOME_PARTIDO"', '"CODIGO_LEGENDA"', '"SIGLA_LEGENDA"',
           '"COMPOSICAO_LEGENDA"', '"NOME_LEGENDA"', '"CODIGO_OCUPACAO"',
           '"DESCRICAO_OCUPACAO"', '"DATA_NASCIMENTO"','"NUM_TITULO_ELEITORAL_CANDIDATO"',
           '"IDADE_DATA_ELEICAO"', '"CODIGO_SEXO"', '"DESCRICAO_SEXO"',
           '"COD_GRAU_INSTRUCAO"', '"DESCRICAO_GRAU_INSTRUCAO"', '"CODIGO_ESTADO_CIVIL"',
           '"DESCRICAO_ESTADO_CIVIL"', '"CODIGO_COR_RACA"', '"DESCRICAO_COR_RACA"',
           '"CODIGO_NACIONALIDADE"', '"DESCRICAO_NACIONALIDADE"', '"SIGLA_UF_NASCIMENTO"',
           '"CODIGO_MUNICIPIO_NASCIMENTO"', '"NOME_MUNICIPIO_NASCIMENTO"',
           '"DESPESA_MAX_CAMPANHA"', '"COD_SIT_TOT_TURNO"', '"DESC_SIT_TOT_TURNO"',
           '"NM_EMAIL"']


with open('Data\\consulta_cand_2014_Brazil.csv', 'a') as singleFile:
    singleFile.write(';'.join(fields)+'\n')
    for csvFile in glob('Data\\consulta_cand_2014\\*.txt'):
        print (csvFile)
        for line in open(csvFile, 'r'):
            singleFile.write(line)


fields = ['"DATA_GERACAO"', '"HORA_GERACAO"', '"ANO_ELEICAO"', '"DESCRICAO_ELEICAO"',
          '"SIGLA_UF"', '"SQ_CANDIDATO"', '"CD_TIPO_BEM_CANDIDATO"', '"DS_TIPO_BEM_CANDIDATO"',
          '"DETALHE_BEM"', '"VALOR_BEM"', '"DATA_ULTIMA_ATUALIZACAO"', '"HORA_ULTIMA_ATUALIZACAO"']

with open('Data\\bem_candidato_2014_Brazil.csv', 'a') as singleFile:
    singleFile.write(';'.join(fields)+'\n')
    for csvFile in glob('Data\\bem_candidato_2014\\*.txt'):
        print (csvFile)
        for line in open(csvFile, 'r'):
            singleFile.write(line)
