#################################################################
##IMPORTANDO ARQUIVOS BIBTEX(Arquivo texto em formato BIBTEX)
# Objetivo: Data quality de arquivos BIBtex
# Extensão: .bib
# Biblioteca: pybtex
#################################################################

#bibliotecas
from pybtex.database.input import bibtex
from pybtex.database import BibliographyData, Entry, Person

#Setando caminho e nome do arquivo
path = "C:\\Users\\victo\\PycharmProjects\\pythonProject\\File\\"
file = "Arquivo.bib"

parser = bibtex.Parser()
in_file = parser.parse_file(path+file)

#Testes
b = in_file                                                                  #Arquivo Completo
# b = in_file.entries['8935096']                                               #Somente o artigo 8935096
# b = in_file.entries['8935096'].persons['author']                             #Lista dos autores do arquigo 8935096
# b = len(in_file.entries['8935096'].persons['author'])                        #Quantidada de elementos da lista
# b = in_file.entries['8935096'].persons['author'][0:]                         #Autores da lista a partir do primeiro elemento(0)
print(b.entries['8935096'].key)


###INPUT 01: para trazer a lista dos autores utilizei funçao RANGE para limitar o LOOP e LEN para definir o final do loop
# for i in in_file.entries:
#     for c in in_file.entries[i].persons:
#         lst_person = str('')
#         for person in range(0, len(in_file.entries[i].persons[c])):
#             b = str(in_file.entries[i].persons[c][person])
#             lst_person = lst_person + '/ ' + b
#     print('Artigo: ' + i + ' Autores: ' + lst_person)

###INPUT 02: Me lembrei que estava utilizando lista... Utilizei os proprios elementos da lista para definir o inicio e fim do loop
# for i in in_file.entries:
#     for c in in_file.entries[i].persons:
#         lst_person = str('')
#         for person in in_file.entries[i].persons[c][0:]:
#             # print(person)
#             lst_person = lst_person + ' - ' + str(person)
#         print('Artigo: ' + i + ' Autores: ' + lst_person)

###INPUT 03: Retirei o segundo loop que estava percorrendo as chave da lista de autores, pois a chave era a mesma para todos artigos('author')
# for i in in_file.entries:
#     lst_person = str('')
#     for person in in_file.entries[i].persons['author']:
#         print(person)
    #     lst_person = lst_person + ' - ' + str(person)
    # print('Artigo: ' + i + ' Autores: ' + lst_person)

###INPUT 04:
for i in in_file.entries:
    lst_person = []
    for person in in_file.entries[i].persons['author'][0:]:
        lst_person.append(person.last_names[0] + ', ' +person.first_names[0])
        # print(lst_person)
    print(lst_person)

################################################################
################################################################

