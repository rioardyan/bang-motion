# Naskah VO: Sistem Tata Kelola Yayasan

Status: **usulan**, menunggu pilihan jalur. Hitungan memakai `tools/vo-hitung.py`.

## Cara menghitung

- Satuan: suku kata. Bahasa Indonesia dihitung dari jumlah huruf vokal (*ai/au/oi* di akhir kata dihitung satu). Angka ditulis dengan huruf, jadi "172" dihitung sebagai "seratus tujuh puluh dua".
- Tiga kecepatan baca: **tenang** 4,0 · **normal** 4,8 · **cepat** 5,4 suku kata per detik. Iklan biasanya dibaca di 4,8–5,4. Di atas 5,4 kata mulai tidak jelas di HP.
- Ini perkiraan. Angka pasti baru ada setelah audio direkam (lihat bagian terakhir).

## 1. Cek: VO penuh vs visual saat ini (26 detik)

VO penuh = semua teks layar dibaca. Hasilnya: **5 dari 11 kalimat muat.**

| Kalimat | Suku kata | @4,8 | Jendela visual | Hasil |
|---|---|---|---|---|
| Kenapa surplus yayasan kena pajak, padahal harusnya nol? | 19 | 3,96 | 3,30 (*nol* meletup di 2,12) | tidak muat |
| Tapi surat ke kantor pajak tidak pernah dikirim. | 16 | 3,33 | 2,60 | tidak muat |
| Karena cuma Bapak yang ingat aturannya. | 14 | 2,92 | 3,20 | **pas** |
| Surplus punya batas pakai empat tahun. | 12 | 2,50 | 1,65 | tidak muat |
| Excel menghitung mundurnya. | 8 | 1,67 | 1,20 | tidak muat |
| Seratus tujuh puluh dua dokumen. | 12 | 2,50 | 1,90 | tidak muat |
| Wewenang jelas. / Aset terdata. / Selisih harus nol. | 5 / 5 / 6 | 1,04 / 1,04 / 1,25 | 1,25 / 1,30 / 1,30 | **pas** |
| Selamatkan surplus dan aset yayasan sekarang. | 15 | 3,12 | 3,05 | mepet (hanya cepat) |

Masalah utamanya ada di 6 detik pertama. Hook dan kalimat sebab butuh 7,3 detik suara. Jendelanya 6 detik.

## 2. Jalur B (rekomendasi): VO ramping, 27,8 detik

Prinsipnya: VO tidak membaca semua teks. Teks layar tetap penuh, jadi penonton tanpa suara tidak kehilangan apa pun. VO hanya membawa kalimat yang paling menjual, dan tepat jatuh di momen visualnya.

Dibuang dari VO: kalimat adegan 2 ("Tapi surat ke kantor pajak...") dan "Excel menghitung mundurnya". Keduanya sudah dijelaskan gambar (amplop belum disegel, baris Excel yang terisi).

Total 89 suku kata, sekitar 18,5 detik bicara dari 27,8 detik (67%). Sisanya jeda untuk gambar.

| Mulai | Kalimat VO | Jatuh di visual | Suku kata | @4,0 | @4,8 | @5,4 | Jendela | Kecepatan pakai |
|---|---|---|---|---|---|---|---|---|
| 0,10 | **Kenapa surplus yayasan kena pajak, padahal harusnya nol?** | kata *nol* meletup di ±3,3 | 19 | 4,75 | 3,96 | 3,52 | 3,60 | **cepat** |
| 6,15 | **Karena cuma Bapak yang ingat aturannya.** | teks muncul 6,1; sertifikat, map, kunci | 14 | 3,50 | 2,92 | 2,59 | 3,20 | normal |
| 10,25 | **Surplus punya batas pakai empat tahun.** | sel kuning diketik | 12 | 3,00 | 2,50 | 2,22 | 2,55 | normal (mepet) |
| 15,65 | **Nol.** (opsional) | angka pajak mendarat di Rp 0 | 1 | 0,25 | 0,21 | 0,19 | 0,40 | normal |
| 16,50 | **Seratus tujuh puluh dua dokumen.** | hitung naik sampai 172 | 12 | 3,00 | 2,50 | 2,22 | 2,55 | normal |
| 19,15 | **Wewenang jelas.** | kartu matriks | 5 | 1,25 | 1,04 | 0,93 | 1,15 | normal |
| 20,45 | **Aset terdata.** | kartu form aset | 5 | 1,25 | 1,04 | 0,93 | 1,15 | normal |
| 21,75 | **Selisih harus nol.** | kartu laporan, angka 0 berdenyut | 6 | 1,50 | 1,25 | 1,11 | 1,30 | normal |
| 24,20 | **Selamatkan surplus dan aset yayasan sekarang.** | CTA muncul kata per kata; segel menutup | 15 | 3,75 | 3,12 | 2,78 | 3,40 | pelan dan tegas (4,6) |

Hasil di kecepatan yang direkomendasikan: **semua baris pas.** Hook hanya pas kalau dibaca cepat. Pada kecepatan normal hook butuh 3,96 detik dan tumpah 0,36 detik ke adegan 2. Itu masih bisa diterima karena adegan 2 tanpa VO.

### Perubahan visual yang dibutuhkan (durasi 26 → 27,8 detik)

| Yang berubah | Sekarang | Jadi |
|---|---|---|
| "padahal harusnya" muncul | 1,8 | 2,5 |
| *nol* meletup | 2,12 | 3,25 |
| Teks hook keluar / teks adegan 2 masuk | 3,1 / 3,5 | 3,7 / 3,8 |
| Teks "Surplus punya batas..." keluar | 11,75 | 12,55 |
| Teks "Excel menghitung mundurnya" masuk / keluar | 11,9 / 13,1 | 12,75 / 13,9 |
| Batas, sisa waktu, status muncul | 11,95–12,45 | 12,8–13,3 |
| Kamera ke surat pajak, odometer, sapuan cahaya | 13,2 / 13,95 / 14,9 | 13,9 / 14,65 / 15,6 |
| Adegan 5 (rak 172) mulai | 15,5 | 16,2 |
| Kartu 1 / 2 / 3 masuk | 17,85 / 19,1 / 20,4 | 19,05 / 20,35 / 21,65 |
| Angka 0 di kartu laporan berdenyut | 20,95 | 22,7 |
| Kamera menembus tab teal | 21,85 | 23,05 |
| CTA muncul / segel | 22,95 / 24,05 | 24,1 / 25,2 |
| Selesai | 26,0 | 27,8 |

Adegan 1 dan 2 tetap berakhir di detik 6,0, sesuai permintaanmu.

## 3. Jalur A: VO penuh

Semua teks layar dibaca. Butuh sekitar **29 detik**: adegan 1 jadi ±4,6 detik, adegan 2 ±3,3 detik, adegan 4 ±1,7 detik lebih panjang. Bicara hampir tanpa jeda (±24 detik dari 29), dan adegan 1–2 jadi ±8 detik. Itu bertentangan dengan permintaanmu memangkas keduanya jadi 6 detik. Tidak saya rekomendasikan.

## 4. Naskah bersih untuk direkam

Tanda: `/` jeda pendek (0,2 detik) · `//` jeda panjang (0,5 detik) atau diam sampai baris berikutnya. Baca dengan nada tenang dan yakin, bukan nada jualan.

```
[0:00]  Kenapa surplus yayasan kena pajak, / padahal harusnya NOL?
        (cepat; nada naik di "nol", tahan sebentar)
//
[0:06]  Karena cuma Bapak yang ingat aturannya.
        (turun, pelan; "Bapak" sedikit ditekan)
//
[0:10]  Surplus punya batas pakai empat tahun.
//      (diam: Excel bekerja, angka menggulung)
[0:15]  Nol.   (opsional, pelan, jatuh)
//
[0:16]  Seratus tujuh puluh dua dokumen.
[0:19]  Wewenang jelas. / Aset terdata. / Selisih harus NOL.
//
[0:24]  Selamatkan surplus dan aset yayasan sekarang.
        (tegas; "sekarang" ditekan)
```

Catatan baca:
- "Excel" dibaca *ék-sél*, bukan *ik-sel*.
- *Nol* tiga kali (hook, "Nol.", "Selisih harus nol"). Tiap kali sedikit lebih tenang. Ini yang mengikat cerita.
- Angka tidak disebut sebagai "Rp". "Rp 0" hanya di layar.
- Tidak ada kalimat baru yang tidak ada di teks layar. Semua kalimat VO adalah teks layar yang sama atau penggalannya, kecuali tiga kartu (Wewenang jelas / Aset terdata / Selisih harus nol). Ketiganya mengulang isi kartu: matriks wewenang, pendataan aset, baris "Selisih (harus nol)".
- "Aset terdata" tidak berarti "aman dari sengketa". Tidak ada janji hukum di naskah ini.

## 5. Mengukur ulang saat audio ada

Perkiraan di atas bisa meleset ±10% tergantung pengisi suara. Setelah rekaman ada:
1. Kirim audionya (wav/mp3/m4a).
2. Saya ukur jeda dan batas kalimat (`scripts/vo-pauses.html` atau `ffmpeg silencedetect`).
3. Waktu visual saya geser ke audio yang sebenarnya, bukan sebaliknya.
