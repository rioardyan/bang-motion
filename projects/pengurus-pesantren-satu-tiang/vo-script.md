# Naskah VO: Pengurus Yayasan Pesantren, Satu Tiang (siap ElevenLabs)

Satu naskah utuh, satu kali generate. Berkas siap tempel: `vo/vo-pesantren.txt`. Model **eleven_v4**, suara **Bram** (sama dengan audio proyek lain), atau Finn bila kamu mau.

## Tempel ini ke ElevenLabs

```
Santri bertambah. Unit bertambah. Semua keputusan masih menunggu satu orang. [pause]
Bukan cuma keputusan. Laporan dan tanah wakaf juga lewat satu orang. [pause]
Semuanya bisa ditulis. Mulai dari keputusan. [short pause]
Dua puluh sembilan keputusan, jelas siapa yang berwenang. [short pause]
Lalu, laporan semua unit terbaca di satu tempat. [short pause]
Terakhir, tanah wakaf tercatat, bukan cuma diingat. [pause]
Ini Sistem Tata Kelola Yayasan, seratus tujuh puluh dua dokumen. [pause]
Unit bertambah, keputusan tetap jalan. [short pause]
Rapikan kerja pondok sekarang.
```

Tag `[short pause]` dan `[pause]` jalan di v4 (model ini tidak membaca `<break>`). Kalau tag ikut terbaca keras, hapus semua tag.

## Kenapa disusun begini

Tiap kalimat menyambung dari kalimat sebelumnya, tanpa loncat.

| Kalimat | Perannya |
|---|---|
| Santri bertambah. Unit bertambah. Semua keputusan masih menunggu satu orang. | Hook, teks layar persis (hook pilihanmu). Sapaan "PENGURUS YAYASAN PESANTREN," tidak dibaca, cukup di layar. |
| Bukan cuma keputusan. Laporan dan tanah wakaf juga lewat satu orang. | Dua masalah tambahan. Menyebut **laporan** dan **wakaf**, supaya kalimat jembatan sesudahnya bisa berdiri sendiri di telinga. Di layar dua butir ini tertulis terpisah. |
| **Semuanya** bisa ditulis. Mulai dari keputusan. | Jembatan. "Semuanya" merujuk ke keputusan, laporan, wakaf yang baru disebut. |
| Dua puluh sembilan keputusan, jelas siapa yang berwenang. | Jawaban pertama (matriks). |
| **Lalu**, laporan semua unit terbaca di satu tempat. | Jawaban kedua (dashboard). |
| **Terakhir**, tanah wakaf tercatat, bukan cuma diingat. | Jawaban ketiga (berita acara). Jatuh saat matahari terbit. |
| **Ini** Sistem Tata Kelola Yayasan, seratus tujuh puluh dua dokumen. | Produk sekilas. "Empat belas kategori" cukup di layar. |
| Unit bertambah, keputusan tetap jalan. | Teks hasil. Mengulang "unit bertambah" dari hook, jadi cerita menutup. |
| Rapikan kerja pondok sekarang. | CTA, **sama persis dengan tombol**. |

Yang tidak dibaca (cukup di layar): sapaan pembuka, "14 kategori", chip dan label dokumen. Dua baris masalah digabung jadi satu kalimat.

## Cara baca

- Hook: tenang dan berat, tiga ketukan. "satu orang" ditahan sebentar.
- Tiga jawaban: ringan dan rapat, seperti membuka daftar. "Lalu" dan "Terakhir" jangan ditekan.
- "tercatat, bukan cuma diingat" turun, yakin. Ini titik lega, saat fajar.
- "Unit bertambah, keputusan tetap jalan." hangat. "Rapikan kerja pondok sekarang." tegas, tanpa nada jualan.

## Durasi: 169 suku kata, jeda 3.7 detik

| Kecepatan baca | Selesai di |
|---|---|
| 5,4 suku kata/dtk | **34.9 dtk** |
| 5,8 | 32.8 dtk |
| 6,2 | 30.9 dtk |

Video sekarang 28,8 detik. Waktu visual akan mengikuti audio, bukan sebaliknya. Audio ini sedikit lebih panjang, jadi video v2 kemungkinan 30–33 detik. Kalau audio melewati 33 detik, jedanya kupangkas di pascaproduksi (suara tidak diubah).

## Perkiraan jatuh di suara (@5,4 / @6,2)

| Kalimat | @5,4 | @6,2 | Visual |
|---|---|---|---|
| Santri bertambah. Unit bertambah. Semua keputusan masih menunggu satu orang. | 0.1–4.9 | 0.1–4.3 | hook (layar 0–3,8) |
| Bukan cuma keputusan. Laporan dan tanah wakaf juga lewat satu orang. | 5.5–9.9 | 4.8–8.7 | adegan 2: tiga baris masalah |
| Semuanya bisa ditulis. Mulai dari keputusan. | 10.5–13.6 | 9.3–12.0 | jembatan |
| Dua puluh sembilan keputusan, jelas siapa yang berwenang. | 14.0–17.7 | 12.4–15.6 | dokumen 1: matriks |
| Lalu, laporan semua unit terbaca di satu tempat. | 18.0–21.3 | 15.9–18.8 | dokumen 2: dashboard |
| Terakhir, tanah wakaf tercatat, bukan cuma diingat. | 21.7–24.8 | 19.2–21.9 | dokumen 3: berita acara, fajar |
| Ini Sistem Tata Kelola Yayasan, seratus tujuh puluh dua dokumen. | 25.4–29.8 | 22.5–26.3 | angka 172 |
| Unit bertambah, keputusan tetap jalan. | 30.4–32.8 | 26.9–29.0 | teks hasil |
| Rapikan kerja pondok sekarang. | 33.2–35.0 | 29.4–31.0 | tombol |

Meleset ±10% tergantung suara. Kuukur ulang setelah audio ada.

## Setelah audio jadi

1. Generate satu kali, simpan sebagai `vo/vo-pesantren.mp3`.
2. Kirim ke aku. Aku ukur batas kalimat (silencedetect + Whisper), geser waktu visual mengikuti suara, lalu bangun versi bersuara. MP4 kurender setelah kamu bilang "render".

Pengaturan awal: Stability 50–60, Similarity 75–80, Style rendah.
