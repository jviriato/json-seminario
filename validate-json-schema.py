#!/usr/bin/env python3
import json
import jsonschema
from pprint import pprint

def validateJSON(filename):
    with open(filename) as file:
        JSON_CONTENT = json.load(file)


def main():
    directory = 'notas_fiscais/'
    validateJSON('notas_fiscais/nota1.json')

if __name__ == "__main__":
    main()