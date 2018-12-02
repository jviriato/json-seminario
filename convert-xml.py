#!/usr/bin/env python3
#1. Converter notas fiscais XML para JSON

import json
from xmljson import badgerfish as bf
import xml.etree.ElementTree as ET
import os

def convertXMLtoJSON(filename):
    file = open(filename)
    XML_CONTENT = file.read()
    root = ET.fromstring(XML_CONTENT)
    JSON_CONTENT = bf.data(root)
    if filename.endswith('.xml'):
        filename = filename[:-4]
    saveJSONtoFile(JSON_CONTENT, filename + '.json')
        

def saveJSONtoFile(JSON_CONTENT, filename):
    with open(filename, 'w') as outfile:
        json.dump(JSON_CONTENT, outfile, indent= 4)

def main():
    directory = 'notas_fiscais/'
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            convertXMLtoJSON(directory + filename)


if __name__ == '__main__':
    main()
    
