"""Prefix every notebook cell with its 1-based number. Safe to re-run after reordering."""
import json, re, sys
p = sys.argv[1] if len(sys.argv) > 1 else 'Depression_Rest_Dataset.ipynb'
nb = json.load(open(p))
for n, c in enumerate(nb['cells'], 1):
    s = ''.join(c['source'])
    code = c['cell_type'] == 'code'
    s = re.sub(r'\A(# \[Cell \d+\]\n|`\[Cell \d+\]`\n\n)', '', s)
    c['source'] = ((f'# [Cell {n}]\n' if code else f'`[Cell {n}]`\n\n') + s).splitlines(keepends=True)
json.dump(nb, open(p, 'w'), indent=1, ensure_ascii=False)
