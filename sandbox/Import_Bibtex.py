#####################################################################################################
##IMPORTANDO ARQUIVOS BIBTEX(Arquivo texto em formato BIBTEX) e EXPORTANDO EM FORMATAÇÃO YAML
# Objetivo: Data quality de arquivos BIBtex
# Extensão: .bib
# Biblioteca: pybtex
#####################################################################################################

from pybtex.database.input import bibtex
from pybtex.database import BibliographyData, Entry
import os


# #################################################################
# #Inicia importanção do arquivo
# #################################################################

##Setando caminho e nome dos arquivos
path = "C:\\Users\\victo\\PycharmProjects\\pythonProject\\File\\"
name_lst = ["Arquivo_Copia1.bib", "Arquivo_Copia2.bib", "Arquivo_Copia3.bib"]

parser = bibtex.Parser()
in_file = parser.parse_file(path + name_lst[0])     #cria base com o primeiro arquivo da lista
lst = []                                            #cria lista vazia para trabalhar os resultados de cada publicação

##Insere as publicações dos arquivos restantes da lista
for f in name_lst[1:]:
    parser = bibtex.Parser()
    file = parser.parse_file(path + f)
    for e in file.entries:
        in_file.add_entry(file.entries[e].key, file.entries[e])

# #################################################################
# #Inicia tratamento dos dados
# #################################################################

#Extraindo e separando o nome dos autores uma lista(Caso a publicação não tenha autor ficará preenchido como 'none')
for i in in_file.entries:
    lst_person = []
    try:
        for person in in_file.entries[i].persons['author'][0:]:
            lst_person.append(person.last_names[0] + ', ' + person.first_names[0])
    except:
        lst_person.append('none')
    # print('Artigo: ' + i + ' Autores: ' + str(lst_person))

    ##Campos necessarios: author, title, keywords, abstract, year, type_publication, doi
    ## para cada topico cria um dicionario com os campos e empilha em uma lista
    result = {
            '1.chave': [int(in_file.entries[i].key)],
            '2.author': lst_person,
            '3.title': [in_file.entries[i].fields['title']],
            '4.keywords': in_file.entries[i].fields['keywords'].split(';'),
            '5.abstract': [in_file.entries[i].fields['abstract']],
            '6.year': [int(in_file.entries[i].fields['year'])],
            '7.type_publication': [in_file.entries[i].type],
            '8.doi': [in_file.entries[i].fields['doi']],
            }
    lst.append(result)
print(lst[1])



# # #################################################################
# # #Verificar se os dados estão corretos em cada coluna
# # #################################################################

# # lst_field = ['chave', 'author', 'title', 'keywords', 'abstract', 'year', 'type_publication', 'doi']
# # for f in lst_field:
# #     for q in lst[0:]:
# #         print(q[f])

# # #################################################################
# # #Exporta arquivo YAML
# # #################################################################

# import yaml

# file_yaml = 'output.yaml'
# lst_field = ['author', 'title', 'keywords', 'abstract', 'year', 'type_publication', 'doi']

# with open(path+file_yaml, 'w') as yamlfile:
#     for data in lst:
#         yaml.dump(data, yamlfile)  # insere os dados na configuração YAML
#         # print(yaml.dump(data))
# # print(open(path+file_yaml).read())


