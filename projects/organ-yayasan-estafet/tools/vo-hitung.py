"""Hitung durasi naskah VO ber-tag <break>: python3 -I tools/vo-hitung.py [vo/vo-organ.txt]
Suku kata Indonesia ~ huruf vokal ('ai/au/oi' di akhir kata = satu). Jeda dari tag <break>. Kecepatan baca diuji 3 nilai."""
import re, sys
def syl(t):
    return sum(max(1, len(re.findall(r'[aeiou]', re.sub(r'(ai|au|oi)$', 'a', w)))) for w in re.findall(r"[a-zA-Z]+", t.lower()))
path = sys.argv[1] if len(sys.argv) > 1 else 'vo/vo-organ.txt'
lines = []
for ln in open(path).read().strip().splitlines():
    m = re.match(r'(.*?)\s*(?:<break time="([\d.]+)s"\s*/>)?\s*$', ln)
    lines.append((m.group(1), float(m.group(2) or 0)))
for pace in (4.4, 4.8, 5.2):
    t = 0.10; print(f"\n== {pace} suku kata/detik ==")
    for i, (txt, br) in enumerate(lines, 1):
        d = syl(txt) / pace; print(f"{i}. {t:5.2f} - {t+d:5.2f}  ({syl(txt):2} suku)  {txt}"); t += d + br
    print(f"selesai bicara {t-br:.2f} dtk | total jeda {sum(b for _,b in lines):.1f} dtk | suku kata {sum(syl(x) for x,_ in lines)}")
