#!/usr/bin/env python3
#1. Lista de produtos, ordenado por preço

import json
from xmljson import badgerfish as bf
import xml.etree.ElementTree as ET
import os

def main():
    precos = {}
    directory = 'notas_fiscais/'
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file = open(directory + filename)
            JSON_CONTENT = json.load(file)
            json_parse  = JSON_CONTENT['nfeProc']['NFe']['infNFe']['det']
            if type(json_parse) == list:
                for i in range(0, len(json_parse)):
                    nome = json_parse[i]['prod']['xProd']['$']
                    valor = json_parse[i]['prod']['vProd']['$']
                    precos[nome] = valor
            else:
                nome  = JSON_CONTENT['nfeProc']['NFe']['infNFe']['det']['prod']['xProd']['$']
                valor = JSON_CONTENT['nfeProc']['NFe']['infNFe']['det']['prod']['vProd']['$']
                precos[nome] = valor
    precos_sorted = sorted(precos.items(), key=lambda kv: kv[1], reverse=True)
    for k,v in precos_sorted:
        print(k,v)

if __name__ == '__main__':
    main()
    
