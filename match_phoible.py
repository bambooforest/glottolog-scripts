import pandas as pd
from fuzzywuzzy import fuzz
from pyglottolog.api import Glottolog

api = Glottolog('/Users/stiv/Github/glottolog')


def matching_dialect(glottocode, name):
    print(type(glottocode), glottocode, type(name), name)

    if glottocode == "NA":
        return glottocode
    lang = api.languoid(glottocode)

    if lang is None:
        # print("glottocode has been updated:", glottocode)
        return glottocode

    if fuzz.ratio(lang.name, name) < 95:
        ratios = []
        for dialect in lang.children:
            ratios.append((dialect.id, dialect.name, fuzz.ratio(dialect.name, name)))
        if ratios and max(r[2] for r in ratios) >= 95:
            return sorted(ratios, key=lambda r: r[2], reverse=True)[0]
        else:
            return glottocode
    else:
        return glottocode


def get_code(glottocode, name):
    result = matching_dialect(glottocode, name)
    if type(result) is tuple:
        return result[0]
    return result


if __name__ == "__main__":
    # Usage on Claire's data
    df = pd.read_csv("claire-language-names.csv", delimiter='\t', na_filter=False)

    # Usage on borrowed sounds database
    # df = pd.read_csv("borrowed.txt", delimiter='\t', na_filter=False)
    
    # Usage on phoible:
    # Production data
    # url = "https://raw.githubusercontent.com/phoible/dev/master/mappings/InventoryID-LanguageCodes.tsv"
    # df = pd.read_csv(url, delimiter='\t', na_filter=False)

    # Test data
    # df = pd.read_csv("test.csv", delimiter='\t', na_filter=False)

    # Output
    # df['New'] = df.apply(lambda row: matching_dialect(row['Glottocode'], row['LanguageName']), axis=1)
    df['Glottocode'] = df.apply(lambda row: get_code(row['Glottocode'], row['LanguageName']), axis=1)
    df.to_csv("test.tsv", sep='\t', encoding='utf-8', index=False)
