#!/usr/bin/env python3

import json
from xmljson import badgerfish as bf
import xml.etree.ElementTree as ET
import os
from jinja2 import *

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def toHTML(JSON_CONTENT, filename):
    # filename = 'nota5.html'
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR + '/template'), trim_blocks=True)
    template = j2_env.get_template('nota-fiscal.html')

    precos = {}
    json_parse = JSON_CONTENT['nfeProc']['NFe']['infNFe']['det']
    if type(json_parse) == list:
        for i in range(0, len(json_parse)):
            nome_produto = json_parse[i]['prod']['xProd']['$']
            valor_produto = json_parse[i]['prod']['vProd']['$']
            precos[nome_produto] = valor_produto
    else:
        nome_produto  = JSON_CONTENT['nfeProc']['NFe']['infNFe']['det']['prod']['xProd']['$']
        valor_produto = JSON_CONTENT['nfeProc']['NFe']['infNFe']['det']['prod']['vProd']['$']
        precos[nome_produto] = valor_produto

    produtos = []
    produtos.append(precos)
    for item in produtos:
        valor_total = sum(item.values())


    output_parsed = template.render(
        nome_loja = JSON_CONTENT['nfeProc']['NFe']['infNFe']['emit']['xFant']['$'],
        data = JSON_CONTENT['nfeProc']['NFe']['infNFe']['ide']['dEmi']['$'],
        nome_cliente = JSON_CONTENT['nfeProc']['NFe']['infNFe']['dest']['xNome']['$'],
        cpf_cliente = JSON_CONTENT['nfeProc']['NFe']['infNFe']['dest']['CPF']['$'],

        lista_produto = produtos,
        valor_total = valor_total,
        outros = JSON_CONTENT['nfeProc']['NFe']['infNFe']['infAdic']['infCpl']['$']
    )
    file = open('html/' + filename[:-5] + '.html', 'w')
    file.write(output_parsed)


def main():
    directory = 'notas_fiscais/'
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file = open(directory + filename)
            JSON_CONTENT = json.load(file)
            toHTML(JSON_CONTENT, filename)


if __name__ == "__main__":
    main()