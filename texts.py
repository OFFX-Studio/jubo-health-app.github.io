#!/usr/bin/env python3
"""Extract / re-apply the Chinese (ZH) i18n texts of the Jubo Viva page.

  python3 texts.py extract   # index.html -> texts.json   (en = reference only)
  python3 texts.py apply     # texts.json -> index.html + files/jubo_viva_concept-refined.html

texts.json format, keys in page order (dict-only keys last):

  { "<i18n-key>": { "en": "<English, for reference>", "zh": "<editable text>" }, ... }

Only the "zh" values are written back into the HTML; "en" is context for
editing. An empty "zh" means the page falls back to the English text.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'index.html'
TARGETS = [ROOT / 'index.html', ROOT / 'files' / 'jubo_viva_concept-refined.html']
TEXTS = ROOT / 'texts.json'

DICT_RE = re.compile(r'var ZH = (\{.*?\});')


def read_zh(html):
    m = DICT_RE.search(html)
    if not m:
        sys.exit('error: `var ZH = {...};` not found')
    return json.loads(m.group(1))


def read_en(html):
    """innerHTML of every element carrying data-i18n, in document order."""
    en = {}
    for m in re.finditer(r'<([a-zA-Z0-9]+)\b[^>]*\bdata-i18n="([^"]+)"[^>]*>', html):
        tag, key = m.groups()
        pos, depth, end = m.end(), 1, m.end()
        tag_re = re.compile(r'</?%s\b[^>]*>' % tag)
        while depth and (m2 := tag_re.search(html, pos)):
            depth += -1 if m2.group(0).startswith('</') else 1
            pos = m2.end()
            if depth == 0:
                end = m2.start()
        en[key] = ' '.join(html[m.end():end].split())
    return en


def extract():
    html = SOURCE.read_text(encoding='utf-8')
    zh = read_zh(html)
    en = read_en(html)
    out = {}
    for key in en:                                    # rendered keys, page order
        out[key] = {'en': en[key], 'zh': zh.get(key, '')}
    for key, val in zh.items():                       # dict-only keys (not rendered)
        if key not in out:
            out[key] = {'en': '', 'zh': val}
    TEXTS.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('extracted %d keys -> %s (%d rendered on page, %d dict-only)'
          % (len(out), TEXTS.name, len(en), len(out) - len(en)))


def apply():
    texts = json.loads(TEXTS.read_text(encoding='utf-8'))
    zh = {k: v['zh'] for k, v in texts.items() if v.get('zh')}
    payload = 'var ZH = ' + json.dumps(zh, ensure_ascii=False) + ';'
    for target in TARGETS:
        if not target.exists():
            print('skip (missing): %s' % target)
            continue
        html = target.read_text(encoding='utf-8')
        new, n = DICT_RE.subn(lambda _: payload, html, count=1)
        if not n:
            print('skip (no ZH dict): %s' % target)
            continue
        target.write_text(new, encoding='utf-8')
        print('applied %d zh strings -> %s' % (len(zh), target.relative_to(ROOT)))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'extract':
        extract()
    elif cmd == 'apply':
        apply()
    else:
        sys.exit(__doc__.strip())
