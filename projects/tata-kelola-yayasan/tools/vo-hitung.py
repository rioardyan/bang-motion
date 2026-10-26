"""Hitung suku kata dan durasi baca VO: python3 -I tools/vo-hitung.py
Suku kata Indonesia ~ jumlah huruf vokal; 'ai/au/oi' di akhir kata dihitung satu. Angka ditulis dengan huruf."""
import re
def syl(t):
    n = 0
    for w in re.findall(r"[a-zA-Z]+", t.lower()):
        w2 = re.sub(r'(ai|au|oi)$', 'a', w)
        n += max(1, len(re.findall(r'[aeiou]', w2)))
    return n
# (id, adegan, teks VO, mulai jendela visual, akhir jendela visual, keterangan jangkar)
V = [
 ("V1","1 Tanya","Kenapa surplus yayasan kena pajak, padahal harusnya nol?",0.10,3.40,"kata 'nol' meletup di layar 2,12"),
 ("V2","2 Sebab","Tapi surat ke kantor pajak tidak pernah dikirim.",3.40,6.00,"teks 3,5 · kuitansi 3,6 · amplop 4,05"),
 ("V3","3 Akar sebab","Karena cuma Bapak yang ingat aturannya.",6.10,9.30,"teks 6,1 · sertifikat 6,35 · kunci 8,3"),
 ("V4a","4 Jawaban","Surplus punya batas pakai empat tahun.",10.20,11.85,"teks 10,2 · sel kuning diketik 10,85-11,85"),
 ("V4b","4 Jawaban","Excel menghitung mundurnya.",11.90,13.10,"teks 11,9 · batas/sisa/status muncul 11,95-12,35"),
 ("V4c","4 Jawaban","Nol.",14.95,15.40,"surat pajak jadi Rp 0 di 14,95 (opsional)"),
 ("V5","5 Isi map","Seratus tujuh puluh dua dokumen.",15.90,17.80,"hitung naik 16,05-17,4"),
 ("V6a","5 Isi map","Wewenang jelas.",17.85,19.10,"kartu matriks 17,85-19,05"),
 ("V6b","5 Isi map","Aset terdata.",19.10,20.40,"kartu form aset 19,1-20,35"),
 ("V6c","5 Isi map","Selisih harus nol.",20.40,21.70,"kartu laporan 20,4 · angka 0 berdenyut 20,95"),
 ("V7","6 Ajakan","Selamatkan surplus dan aset yayasan sekarang.",22.95,26.00,"teks 22,95-24,0 · segel 24,05"),
]
P = {"tenang":4.0, "normal":4.8, "cepat":5.4}
print(f"{'id':4} {'suku':>4} {'@4,0':>5} {'@4,8':>5} {'@5,4':>5} {'jendela':>8}  verdict")
tot=0
for i,sc,t,a,b,_ in V:
    s=syl(t); tot+=s; w=b-a
    d={k:s/v for k,v in P.items()}
    if d['normal']<=w: vd='PAS'
    elif d['cepat']<=w: vd='MEPET (hanya cepat)'
    else: vd='TIDAK MUAT'
    print(f"{i:4} {s:>4} {d['tenang']:5.2f} {d['normal']:5.2f} {d['cepat']:5.2f} {w:8.2f}  {vd}   | {t}")
print('total suku kata', tot, '| bicara murni @4,8 =', round(tot/4.8,1), 'dtk')
