""" Small script from xrotwang to match language (dialect) names by Glottocode and canonical name

    Make sure to:
        `pip install --upgrade --force-reinstall pyglottolog`
        `pip install fuzzywuzzy`

    Usage:
        $ python match.py nyun1247 Bibbulman
        (u'bibb1234', u'Bibbulman', 100)
        $ python match.py nyun1247 Balardung
        None
"""

from fuzzywuzzy import fuzz

def matching_dialect(glottolog, glottocode, name):
    lang = glottolog.languoid(glottocode)
    if fuzz.ratio(lang.name, name) < 95:
        ratios = []
        for dialect in lang.children:
            ratios.append((dialect.id, dialect.name, fuzz.ratio(dialect.name, name)))
        if ratios and max(r[2] for r in ratios) >= 95:
            return sorted(ratios, key=lambda r: r[2], reverse=True)[0]

if __name__ == "__main__":
    import sys
    from pyglottolog.api import Glottolog
    print matching_dialect(Glottolog(), *sys.argv[1:])


