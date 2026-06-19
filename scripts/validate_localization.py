import json,re
from pathlib import Path

ROOT=Path('E-Mails')
LANGS=['DE','EN','TR','RU','AR','IT','ZH','HI','ES','FR','NL','PL']
FILES={l:ROOT/l/('all emails v6.json' if l=='DE' else 'all emails v1.json') for l in LANGS}
REQ={'email_name','subject','preheader','body'}
ph_re=re.compile(r'(\{\{[^{}]+\}\}|\{%[^%]+%\})')
german_tokens=[' und ',' der ',' die ',' das ',' ist ',' nicht ',' für ',' mit ','dein ','deine ','hallo']

def placeholders(s): return set(ph_re.findall(s))

def main():
    data={}
    for l,p in FILES.items():
        data[l]=json.loads(p.read_text())
    n=len(data['DE'])
    for l in LANGS:
        assert len(data[l])==n,f'length mismatch {l}'
    de_ph=placeholders(json.dumps(data['DE'],ensure_ascii=False))
    issues=[]
    for i in range(n):
        base=data['DE'][i]['email_name']
        for l in LANGS:
            o=data[l][i]
            if set(o.keys())!=REQ: issues.append(f'{l} idx {i} keys')
            if o['email_name']!=base: issues.append(f'{l} idx {i} email_name')
            for f in ['subject','preheader','body']:
                if not str(o[f]).strip(): issues.append(f'{l} idx {i} empty {f}')
    for l in LANGS:
        ph=placeholders(json.dumps(data[l],ensure_ascii=False))
        if ph!=de_ph: issues.append(f'{l} placeholder set differs')
    for l in LANGS:
        if l=='DE': continue
        text=json.dumps(data[l],ensure_ascii=False).lower()
        score=sum(text.count(t.strip()) for t in german_tokens)
        if score>40: issues.append(f'{l} appears to contain substantial German text (heuristic score={score})')
    if issues:
        print('FAILED')
        for x in issues: print('-',x)
        raise SystemExit(1)
    print(f'OK: validated {n} emails across {len(LANGS)} languages')

if __name__=='__main__':
    main()
