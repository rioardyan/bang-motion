"""Cek apakah audio VO hasil generate muat di jendela visualnya.
Pakai: python3 -I tools/vo-cek.py            (membaca vo/cues.csv dan vo/<id>.mp3|wav|m4a)
Tanpa audio: hanya perkiraan dari suku kata. Dengan audio: durasi asli + kecepatan yang perlu dipasang."""
import csv, re, subprocess, pathlib
def syl(t):
    n = 0
    for w in re.findall(r"[a-zA-Z]+", t.lower()):
        n += max(1, len(re.findall(r'[aeiou]', re.sub(r'(ai|au|oi)$', 'a', w))))
    return n
def dur(path):
    out = subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',str(path)],capture_output=True,text=True)
    return float(out.stdout.strip())
rows = list(csv.DictReader(open('vo/cues.csv')))
print(f"{'id':6}{'mulai':>6}{'batas':>7}{'jendela':>8}{'suku':>5}{'perkiraan':>10}{'audio':>7}  hasil")
for r in rows:
    s, e = float(r['start']), float(r['window_end']); win = e - s; n = syl(r['text_tts'])
    est = n / float(r['pace'])
    f = next((p for p in pathlib.Path('vo').glob(r['id'] + '.*') if p.suffix in ('.mp3','.wav','.m4a')), None)
    if f:
        d = dur(f); ok = d <= win + 1e-6
        res = 'PAS' if ok else f"TERLALU PANJANG: pasang speed {d/win:.2f}x (atau potong teks)"
        print(f"{r['id']:6}{s:6.2f}{e:7.2f}{win:8.2f}{n:5}{est:10.2f}{d:7.2f}  {res}")
    else:
        print(f"{r['id']:6}{s:6.2f}{e:7.2f}{win:8.2f}{n:5}{est:10.2f}{'-':>7}  (belum ada audio) perkiraan {'PAS' if est<=win else 'MEPET/TIDAK'}")
