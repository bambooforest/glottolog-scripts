"""Use treedb iterdescendants to get a long format table of language descendants"""

import treedb
import csv

FILE = "descendants.csv"

with open(FILE, 'w', encoding='utf-8') as f:
    writer = csv.writer(f, dialect='excel-tab')
    writer.writerow(['Parent', 'Daughters'])
    for parent, descendants in treedb.iterdescendants(child_level="language"):
        for d in descendants:
            writer.writerow([parent, d])

