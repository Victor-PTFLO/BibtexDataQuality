from pybtex.database.input import bibtex

path = "C:\\Users\\victo\\PycharmProjects\\pythonProject\\File\\"
file = "Arquivo.bib"

parser = bibtex.Parser()
bib_data = parser.parse_file(path+file)

for i in bib_data.entries:
    df = i.fields
    print(df)