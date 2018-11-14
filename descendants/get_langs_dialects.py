"""Use treedb.iterdescendants() to get a long format table of language descendants.

iterdescendants takes optional iterdescendants(parent_level=None, child_level=None

"""

import treedb
import csv

FILE = "language_dialects.csv"

with open(FILE, 'w', encoding='utf-8') as f:
    writer = csv.writer(f, dialect='excel-tab')
    writer.writerow(['Language', 'Dialects'])
    for parent, descendants in treedb.iterdescendants(parent_level="language", child_level="dialect"):
        for d in descendants:
            writer.writerow([parent, d])

