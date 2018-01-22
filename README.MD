Projeto de conclusão do curso de Engenheiro de Machine Learning - Udacity.

Tem como objetivo realizar a previsão de deputados estaduais e federais eleitos nas eleições de 2014, utilizando apenas os dados dos candidatos, bens declarados e doações recebidas.

Para mais detalhes, veja o relatório completo no arquivo Capstone Report - Machine Learning Engineer Nanodegree.pdf.

Quanto ao dataset, você pode baixar os dados utilizados diretamente do repositório Kaggle disponível em:
https://www.kaggle.com/eliezerfb/candidatos-deputado-federal-e-estadual-2014
Salvar em /Data com o nome: dados_tratados.csv


Ou se preferir pode montar o dataset:


1) Baixar os seguintes datasets no diretório /Data
	Candidatos: 
	http://agencia.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2014.zip
	
	Bens: 
	http://agencia.tse.jus.br/estatistica/sead/odsele/bem_candidato/bem_candidato_2014.zip
	
	Receitas: 
	https://www.kaggle.com/felipeleiteantunes/electoral-donations-brazil2014/downloads/receitas_candidatos_2014_brasil.txt

2) Descompactar o arquivo consulta_cand_2014.zip no diretório /Data/consulta_cand_2014

3) Descompactar o arquivo bem_candidato_2014.zip no diretório /Data/bem_candidato_2014.zip

4) Executar o script merge_files_brazil.py
	Este script vai gerar dois arquivos: bem_candidato_2014_Brazil.csv e consulta_cand_2014_Brazil.csv

5) Executar o Notebook Capstone_Project_Preparacao.ipynb
	Este notebook prepara os dados para posterior utilização, ele gera um arquivo: dados_tratados.csv

6) Executar o Notebook Capstone_Project_Eleicoes.ipynb
